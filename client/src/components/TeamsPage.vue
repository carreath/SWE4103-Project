<template>
  <div id="teams-page">
    <div id="title-container">
      <template slot-scope="scope">
        <ColorCircleTeamName
          :team="selectedTeam"
          justifyContent="flex-start"/>
      </template>
    </div>
    <div id="players-table-container">
      <el-table
        :data="formatPlayers"
        :default-sort = "{prop: 'fullName', order: 'descending'}"
        stripe
        style="width: 100%">
        <el-table-column
          prop="playerID"
          sortable
          label="Player ID">
        </el-table-column>
        <el-table-column
          prop="fullName"
          sortable
          label="Full Name">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'TeamsPage',
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
      'selectedTeamId',
      'selectedTeam',
      'playersByTeamId',
      'teamById',
    ]),
    formatPlayers() {
      const formatedPlayers = this.teamsByLeagueId(this.selectedTeamId).map((player) => {
        return {
          playerID: player.playerID,
          fullName: `${player.firstName} ${player.lastName}`,
          number: player.number,
          goals: player.goals,
          cleanSheets: player.cleanSheets,
          yellowCards: player.yellowCards,
          redCards: player.redCards,
        };
      });
      return formatedPlayers;
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
#teams-page{
}
</style>
