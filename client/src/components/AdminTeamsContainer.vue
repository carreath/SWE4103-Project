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
        stripe
        style="">
        <el-table-column
          width="100px"
          prop="teamID"
          label="Team ID">
        </el-table-column>
        <el-table-column
          prop="teamName"
          label="Team Name">
        </el-table-column>
        <el-table-column
          prop="leagueID"
          label="League Name">
        </el-table-column>
        <el-table-column
          prop="managerID"
          label="Manager ID">
        </el-table-column>
        <el-table-column
          label="Action">
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

    ]),
    teamCreateClicked() {
      this.$router.push('/admin/teams/create');
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
