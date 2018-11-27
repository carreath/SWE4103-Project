<template>
  <div id="teams-container">
    <div id="title-container">
    </div>
    <div id="teams-table-container">
      <el-table
        :data="formatTeams"
        stripe
        :style="{
          'width': '100%',
          'cursor': 'pointer'
        }"
        @row-click="teamClicked">
        <el-table-column
          prop="teamID"
          sortable
          label="Team ID">
        </el-table-column>
        <el-table-column
          prop="teamName"
          sortable
          label="Team Name">
          <template slot-scope="scope">
            <ColorCircleTeamName
              :team="teamById(scope.row.teamID)"
              justifyContent="flex-start"/>
          </template>
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
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'TeamsContainer',
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
      'selectedLeagueId',
      'teamsByLeagueId',
      'teamById',
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
      'setSelectedTeamId',
    ]),
    teamClicked(row) {
      this.setSelectedTeamId(row.teamID);
      this.$router.push('/teams/page');
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-container{
}
</style>
