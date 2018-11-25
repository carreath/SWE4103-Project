<template>
  <div id="standings-container">
    <div id="title-container">
    </div>
    <div id="standings-table-container">
      <el-table
        :data="formatTeams"
        :default-sort = "{prop: 'rank', order: 'descending'}"
        stripe
        style="width: 100%">
        <el-table-column
          prop="rank"
          sortable
          label="Rank">
        </el-table-column>
        <el-table-column
          prop="teamName"
          sortable
          label="Team Name"
          width="165px">
          <template slot-scope="scope">
            <ColorCircleTeamName
              :team="teamById(scope.row.teamID)"
              justifyContent="flex-start"/>
          </template>
        </el-table-column>
        <el-table-column
          prop="pointsPerGame"
          sortable
          label="PPG">
          <template slot-scope="scope">
            <el-tooltip content="Points per Game" :enterable="false" placement="top">
              <span>{{ scope.row.pointsPerGame }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="wins"
          sortable
          label="W">
          <template slot-scope="scope">
            <el-tooltip content="Wins" :enterable="false" placement="top">
              <span>{{ scope.row.wins }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="draws"
          sortable
          label="D">
          <template slot-scope="scope">
            <el-tooltip content="Draws" :enterable="false" placement="top">
              <span>{{ scope.row.draws }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="losses"
          sortable
          label="L">
    <template slot-scope="scope">
            <el-tooltip content="Losses" :enterable="false" placement="top">
              <span>{{ scope.row.losses }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="goalsDifference"
          sortable
          label="GD">
          <template slot-scope="scope">
            <el-tooltip content="Goal Differential" :enterable="false" placement="top">
              <span>{{ scope.row.goalsDifference }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="goalsFor"
          sortable
          label="GS">
          <template slot-scope="scope">
            <el-tooltip content="Goals Scored" :enterable="false" placement="top">
              <span>{{ scope.row.goalsFor }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="goalsAgainst"
          sortable
          label="GA">
          <template slot-scope="scope">
            <el-tooltip content="Goals Against" :enterable="false" placement="top">
              <span>{{ scope.row.goalsAgainst }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="gamesPlayed"
          sortable
          label="GP">
          <template slot-scope="scope">
            <el-tooltip content="Games Played" :enterable="false" placement="top">
              <span>{{ scope.row.gamesPlayed }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column
          prop="leaguePoints"
          sortable
          label="PTS">
          <template slot-scope="scope">
            <el-tooltip content="Points" :enterable="false" placement="top">
              <span>{{ scope.row.leaguePoints }}</span>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'StandingsContainer',
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
          leaguePoints: team.leaguePoints,
          wins: team.wins,
          losses: team.losses,
          draws: team.draws,
          gamesPlayed: team.gamesPlayed,
          goalsFor: team.goalsFor,
          goalsAgainst: team.goalsAgainst,
          goalsDifference: team.goalsDifference,
          pointsPerGame: team.pointsPerGame,
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
