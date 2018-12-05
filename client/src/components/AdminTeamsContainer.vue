<template>
  <div id="admin-teams-container">
    <div id="title-container">
      <h1>
        {{ leagueTitleName }}
      </h1>
      <div></div>
      <div id="create-team-button-container">
        <el-button
        v-if="(user || {}).userType !== 'Manager'"
        @click="teamCreateClicked"
        type="primary">Create New Team</el-button>
      </div>
    </div>
    <div id="teams-table-container">
      <el-table
        :data="formatTeams"
        stripe
        style="">
        <el-table-column
          width="100px"
          prop="teamID"
          sortable
          label="Team ID">
        </el-table-column>
        <el-table-column
          prop="teamName"
          sortable
          :show-overflow-tooltip="true"
          label="Name">
          <template slot-scope="scope">
            <ColorCircleTeamName
              :team="teamById(scope.row.teamID)"
              justifyContent="flex-start"/>
          </template>
        </el-table-column>
        <el-table-column
          prop="leagueName"
          sortable
          :show-overflow-tooltip="true"
          label="League Name">
        </el-table-column>
        <el-table-column
          prop="managerName"
          :show-overflow-tooltip="true"
          label="Manager">
        </el-table-column>
        <el-table-column
          label="Action">
          <template slot-scope="scope">
            <el-button
            icon="el-icon-edit"
            size="mini"
            :disabled="actionEditDisabled(scope.row)"
            @click='teamEditClicked(scope.row.teamID)'>
            </el-button>
            <el-button
            icon="el-icon-delete"
            size="mini"
            :disabled="actionDeleteDisabled(scope.row)"
            @click="teamDeleteClicked(scope.row.teamID, scope.row.teamName)">
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';

export default {
  name: 'AdminTeamsContainer',
  data() {
    return {
    };
  },
  components: {
    ColorCircleTeamName,
  },
  computed: {
    ...mapGetters([
      'teams',
      'leagueById',
      'leagues',
      'teamById',
      'userById',
      'user',
      'selectedLeagueId',
      'selectedLeague',
    ]),
    leagueTitleName() {
      if (!this.user) {
        return '';
      }
      if (this.user.userType === 'Admin') {
        return this.selectedLeague.leagueName;
      }
      if (this.user.userType === 'Coordinator') {
        return (this.leagues.find(league => {
          return league.managerID === this.user.userID;
        }) || {}).leagueName;
      }
      if (this.user.userType === 'Manager') {
        const leagueId = this.teams.find(team => {
          return team.managerID === this.user.userID;
        }).leagueID;
        return this.leagueById(leagueId).leagueName;
      }
      return '';
    },
    formatTeams() {
      const formatedTeams = this.teams.filter(team => {
        if (!this.user) {
          return false;
        }
        if (this.user.userType === 'Admin') {
          return team.leagueID === this.selectedLeagueId;
        }
        if (this.user.userType === 'Coordinator') {
          return team.leagueID === (this.leagues.find(league => {
            return league.managerID === this.user.userID;
          }) || {}).leagueID;
        }
        if (this.user.userType === 'Manager') {
          return team.leagueID === this.teams.find(team => {
            return team.managerID === this.user.userID;
          }).leagueID;
        }
        return false;
      }).map((team) => {
        const manager = this.userById(team.managerID);
        const managerNameIn = manager ? `${manager.firstName} ${manager.lastName}` : 'None';
        return {
          ...team,
          leagueName: this.leagueById((team || {}).leagueID).leagueName,
          managerName: managerNameIn,
        };
      });
      return formatedTeams;
    },
  },
  methods: {
    ...mapActions([
      'deleteLeague',
      'setEditedTeam',
      'setEditTeamModalVisible',
    ]),
    actionEditDisabled(teamObj) {
      if (!this.user) {
        return true;
      }
      switch (this.user.userType) {
        case ('Admin'): {
          return false;
        }
        case ('Coordinator'): {
          return false;
        }
        case ('Manager'): {
          return teamObj.managerID !== this.user.userID;
        }
        default:
          return true;
      }
    },
    actionDeleteDisabled() {
      if (!this.user) {
        return true;
      }
      switch (this.user.userType) {
        case ('Admin'): {
          return false;
        }
        case ('Coordinator'): {
          return false;
        }
        case ('Manager'): {
          return true;
        }
        default:
          return true;
      }
    },
    teamCreateClicked() {
      this.$router.push('/admin/teams/create');
    },
    teamEditClicked(index) {
      this.setEditedTeam(index);
      this.setEditTeamModalVisible(true);
    },
    teamDeleteClicked(id, name) {
      this.$confirm(`Are you sure you want to delete ${name}?`, 'Confirm Team Deletion', {
        confirmButtonText: 'Delete Team',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.deleteTeam(this.teamById(id)).then((response) => {
          if (response.retVal) {
            this.$message({
              message: `Deleted ${name}`,
              center: true,
            });
          } else {
            this.$message.error(response.retMsg);
          }
          this.$router.push('/admin/teams');
        });
      }).catch(() => {
      });
    },
  },
  watch: {
    team() {
      this.formatedTeams();
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-container{
  #title-container{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;

    h1{
      margin-bottom: 0;
    }

    #create-team-button-container{
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-end;
      height: 61px;
      transition: 0.3s;
    }
  }
}
</style>
