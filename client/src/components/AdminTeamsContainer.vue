<template>
  <div id="admin-teams-container">
    <div id="title-container">
    </div>
    <div id="create-team-button-container">
      <el-button
      @click="teamCreateClicked"
      type="primary">Create New Team</el-button>
    </div>
    <div id="teams-table-container">
      <el-table
        :data="formatTeams"
        :default-sort = "{prop: 'teamID', order: 'ascending'}"
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
          label="Team Name">
        </el-table-column>
        <el-table-column
          prop="leagueID"
          sortable
          label="League Name">
        </el-table-column>
        <el-table-column
          prop="managerID"
          label="Manager ID">
        </el-table-column>
        <el-table-column
          label="Action">
          <template slot-scope="scope">
            <el-button
            @click='teamEditClicked(scope.row.teamID)'>
              Edit
            </el-button>
            <el-button
            @click="teamDeleteClicked(scope.row.teamID, scope.row.teamName)">
              Delete
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminTeamsContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'teams',
      'leagueById',
      'leagues',
      'teamById'
    ]),
    formatTeams() {
      const formatedTeams = this.teams.map((team) => {
        return {
          teamID: team.teamID,
          teamName: team.teamName,
          leagueID: this.leagueById(team.leagueID).leagueName,
          managerID: team.managerID,
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
        this.deleteTeam(this.teamById(id)).then(() => {
          this.$message({
            message: `Deleted ${name}`,
            center: true,
          });
          this.$router.push('/admin/teams');
        });
      }).catch(() => {
      });
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-container{
  #create-team-button-container{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    height: 61px;
    transition: 0.3s;
  }
}
</style>
