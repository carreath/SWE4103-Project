<template>
  <div id="admin-leagues-container">
    <div id="title-container">
    </div>
    <div id="create-league-button-container">
      <el-button
      @click="leagueCreateClicked"
      type="primary">Create New League</el-button>
    </div>
    <div id="leagues-table-container">
      <el-table
        :data="formatLeagues"
        stripe
        style="width: 100%">
        <el-table-column
          prop="id"
          label="League Id">
        </el-table-column>
        <el-table-column
          prop="name"
          label="League Name">
        </el-table-column>
        <el-table-column
          prop="season"
          label="League Season">
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
  name: 'AdminLeaguesContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'leagues',
    ]),
    formatLeagues() {
      const formatedLeagues = this.leagues.map((league) => {
        return {
          id: league.leagueID,
          name: league.leagueName,
          season: league.season,
        };
      });
      return formatedLeagues;
    },
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([

    ]),
    handleKeyUp(e) {
      // Enter key
      if (e.keyCode === 13) {
        this.leagueCreateClicked();
      }
    },
    leagueCreateClicked() {
      this.$router.push('/admin/leagues/create');
    },
  },
  mounted() {
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-leagues-container{

  #create-league-button-container{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    height: 61px;
    transition: 0.3s;
  }
}
</style>
