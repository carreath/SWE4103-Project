<template>
  <div id="teams-page">
    <div id="title-container">
      <div id="team-button-container">
        <el-button
          size="medium"
          @click="teamsClicked()">
          <i class="el-icon-d-arrow-left"></i>
          Teams
        </el-button>
      </div>
      <div id="team-name">
        <ColorCircleTeamName
          :team="selectedTeam"
          justifyContent="center"/>
          &nbsp;- Player Stats
      </div>
      <span id="playerNameSearch">
          <el-input
            v-model="searchPlayerName"
            size="small"
            placeholder="Filter Name"/>
      </span>
    </div>
    <div id="players-table-container">
      <el-table
        :data="formatPlayers"
        :default-sort = "{prop: 'lastName', order: 'ascending'}"
        stripe
        style="width: 100%">
        <el-table-column
          prop="lastName"
          sortable
          label="Last Name">
        </el-table-column>
        <el-table-column
          prop="number"
          sortable
          label="Number">
        </el-table-column>
        <el-table-column
          prop="goals"
          sortable
          label="Goals">
        </el-table-column>
        <el-table-column
          prop="cleanSheets"
          sortable
          label="Clean Sheets">
        </el-table-column>
        <el-table-column
          prop="yellowCards"
          sortable
          label="Yellow Cards">
        </el-table-column>
        <el-table-column
          prop="redCards"
          sortable
          label="Red Cards">
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
      searchPlayerName: '',
    };
  },
  components: {
    ColorCircleTeamName,
  },
  computed: {
    ...mapGetters([
      'players',
      'leagueById',
      'selectedTeamId',
      'selectedTeam',
      'playersByTeamId',
      'teamById',
      'selectedLeagueId',
    ]),
    formatPlayers() {
      const formatedPlayers = this.playersByTeamId(this.selectedTeamId).filter(player => {
        if (!this.searchPlayerName) {
          return true;
        }
        const lastName = player.lastName.toLowerCase();
        return lastName.includes(this.searchPlayerName.toLowerCase());
      });
      return formatedPlayers;
    },
  },
  methods: {
    ...mapActions([
      'setSelectedTeamId',
    ]),
    teamsClicked() {
      this.setSelectedTeamId(null);
      this.$router.push('/teams');
    },
  },
  watch: {
    selectedLeagueId() {
      this.$router.push('/teams');
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#teams-page{
  #title-container{
    font-size: 1.5rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    flex-direction: row;
    margin-top: 16px;
    justify-content: space-between;
    #team-name{
      display: flex;
      align-items: center;
      justify-content: center;
      margin-left: 20px;
    }
  }
}
</style>
