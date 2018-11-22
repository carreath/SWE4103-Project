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
    def execute(self, cursor, command):
        try:
            cursor.execute(command + ';')
            message = "Applied SQL: " + command[0:64] + "..."
            print (message.replace("\n", " "))
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)


    def applySQL(self, filepath, skip):
        fd = open(filepath, 'r')
        sqlFile = fd.read()
        fd.close()

        db = DatabaseConnector()

        sqlCommands = ""
        # all SQL commands (split on ';')
        if ('DELIMITER' in sqlFile):
            sqlCommands = sqlFile.replace('DELIMITER //', '')
            sqlCommands = sqlCommands.replace('//', '')
            sqlCommands = sqlCommands.replace('DELIMITER ;', '')
            self.execute(db.cursor, sqlCommands)
            db.conn.commit()
            db.cursor.close()
            return
        else:
            sqlCommands = sqlFile.split(';')

        # Execute every command from the input filepath
        for command in sqlCommands:
            try:
                if (skip > 0):
                    skip = skip - 1
                    raise Exception('skip command')
                self.execute(db.cursor, command)
            except Exception as e:
                if hasattr(e, 'message'):
                    print(e.message)
                else:
                    print(e)

        db.conn.commit()
        db.cursor.close()

    def migrate(self, fresh):
        # Get DB directories
        dbDir = os.path.join(Path(os.getcwd()).parent, "db")
        migrationDir = os.path.join(dbDir, "migration")
        migrate = False

        if (fresh):
            print ("Database Table Defenitions Changed. Resetting Database...")
            self.applySQL(os.path.join(dbDir, 'tables-league_mngmt.sql'), 3)
            copyfile(os.path.join(dbDir, 'tables-league_mngmt.sql'), os.path.join(migrationDir, 'tables-league_mngmt.sql'))
            print ('DB Reset, tables-league_mngmt.sql changed')
        else:
            print ("\nChecking Database for Migrations:")

        # Check if migrations exist
        if (os.path.isdir(migrationDir) == False):
            migrate = True
            os.mkdir(migrationDir)
        else:
            for file in os.listdir(dbDir):
                filename = os.fsdecode(file)
                if filename.endswith(".sql"): 
                    if (os.path.isfile(os.path.join(migrationDir, filename)) == False):
                        # Apply file to DB if it hasnt yet been applied
                        self.applySQL(os.path.join(dbDir, filename), 0)
                        copyfile(os.path.join(dbDir, filename), os.path.join(migrationDir, filename))
                    else:
                        if (fresh or filecmp.cmp(os.path.join(migrationDir, filename), os.path.join(dbDir, filename)) == False):
                            if (fresh == False and filename == 'tables-league_mngmt.sql'):
                                # resetDB and rerun sql files
                                migrate = True
                                break
                            else:
                                self.applySQL(os.path.join(dbDir, filename), 0)
                                copyfile(os.path.join(dbDir, filename), os.path.join(migrationDir, filename))  
                    continue
                else:
                    continue
            print ("Done Migration check\n")
        return migrate