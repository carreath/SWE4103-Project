<template>
  <div id="teams-container">
    <div id="title-container">
    </div>
    <div id="teams-table-container">
      <el-table
        :data="formatTeams"
        stripe
        :default-sort = "{prop: 'teamID', order: 'ascending'}"
        style="width: 100%">
        <el-table-column
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
          prop="managerID"
          label="Manager ID">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'TeamsContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'teams',
      'leagueById',
      'selectedLeagueId',
      'teamsByLeagueId',
    ]),
    formatTeams() {
      const formatedTeams = this.teamsByLeagueId(this.selectedLeagueId).map((team) => {
        return {
          teamID: team.teamID,
          teamName: team.teamName,
          managerID: team.managerID,
        };
      });
      return formatedTeams;
    },
  },
  methods: {
    ...mapActions([

    ]),
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-container{
}
</style>
