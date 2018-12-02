from flask import Flask
from flaskext.mysql import MySQL
import config
from pathlib import Path
import filecmp
from shutil import copyfile
import sys
from common import DatabaseConnector
import os


class DatabaseMigrator:
    # Execute an sql command
    def execute(self, cursor, command):
        try:
            cursor.execute(command + ';')

            # Loggin message
            message = "Applied SQL: " + command[0:64] + "..."
            print (message.replace("\n", " "))
        except Exception as e:
            # Print error
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

    # Apply an sql file to the db
    def applySQL(self, filepath, skip):
        # Open file
        fd = open(filepath, 'r')
        sqlFile = fd.read()
        fd.close()


        sqlCommands = ""
        # If there is a delimiter split on it and execute
        if ('DELIMITER' in sqlFile):
            # Remove delimiters
            sqlCommands = sqlFile.replace('DELIMITER //', '')
            sqlCommands = sqlCommands.replace('DELIMITER ;', '')

            # split file
            sqlCommands = sqlCommands.split("//")
        else:
            # split file
            sqlCommands = sqlFile.split(';')

        # Open DB connection
        db = DatabaseConnector()

        # Execute every command from the input file
        for command in sqlCommands:
            try:
                # Skip x number of commands. ie: DROP DATABASE IF EXISTS leagues;
                if (skip > 0):
                    skip = skip - 1
                    raise Exception('skip command')

                # execute a command
                self.execute(db.cursor, command)
            except Exception as e:
                # print error
                if hasattr(e, 'message'):
                    print(e.message)
                else:
                    print(e)

        db.conn.commit()
        db.cursor.close()

    # Migrate DB
    def migrate(self, reset):
        dbDir = ""
        migrationDir = ""

        if (is_posix()):
            # Get DB directories
            dbDir = os.path.join(Path(os.getcwd()).parent.as_posix(), "db")
            migrationDir = os.path.join(dbDir, "migration")
        else:
            # Get DB directories
            dbDir = os.path.join(Path(os.getcwd()).parent, "db")
            migrationDir = os.path.join(dbDir, "migration")

        # if reset is true, rebuild entire database
        if (reset):
            print ("Database Table Defenitions Changed. Resetting Database...")
            self.applySQL(os.path.join(dbDir, 'tables-league_mngmt.sql'), 3)
            copyfile(os.path.join(dbDir, 'tables-league_mngmt.sql'), os.path.join(migrationDir, 'tables-league_mngmt.sql'))
            print ('DB Reset, tables-league_mngmt.sql changed')
        else:
            print ("\nChecking Database for Migrations:")

        # Check if migrations folder exists
        if (os.path.isdir(migrationDir) == False):
            # Make directory and build DB
            os.mkdir(migrationDir)
            self.migrate(True)
        else:
            # Loop through all files in /db
            for file in os.listdir(dbDir):
                filename = os.fsdecode(file)
                # If file is an sql script run it
                if filename.endswith(".sql"): 
                    # If file is not present in the migration then run it
                    if (os.path.isfile(os.path.join(migrationDir, filename)) == False):
                        # Apply file to DB if it hasnt yet been applied
                        self.applySQL(os.path.join(dbDir, filename), 0)
                        copyfile(os.path.join(dbDir, filename), os.path.join(migrationDir, filename))
                    else:
                        # if resetting or the file is different from the current migration run it
                        if (reset or filecmp.cmp(os.path.join(migrationDir, filename), os.path.join(dbDir, filename)) == False):
                            # if DB is in the process of resetting dont rerun table creation
                            # otherwise if table creation file is edited reset DB
                            if (reset == False and filename == 'tables-league_mngmt.sql'):
                                # resetDB and rerun sql files
                                self.migrate(True)
                                break
                            else:
                                # apply file to DB
                                self.applySQL(os.path.join(dbDir, filename), 0)
                                copyfile(os.path.join(dbDir, filename), os.path.join(migrationDir, filename))  
                    continue
                else:
                    continue
            print ("Done Migration check\n")

def is_posix():
    try:
        import posix
        return True
    except ImportError:
        return False