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
        :default-sort = "{prop: 'id', order: 'ascending'}"
        stripe
        style="width: 100%">
        <el-table-column
          prop="id"
          sortable
          label="League Id">
        </el-table-column>
        <el-table-column
          prop="name"
          sortable
          label="League Name">
        </el-table-column>
        <el-table-column
          prop="season"
          sortable
          label="League Season">
        </el-table-column>
        <el-table-column
          label="Action">
          <template slot-scope="scope">
            <el-button
            @click="leagueEditClicked(scope.$index)">
              Edit
            </el-button>
            <el-button
            @click="leagueDeleteClicked(scope.$index)">
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
    leagueCreateClicked() {
      this.$router.push('/admin/leagues/create');
    },
    leagueEditClicked(index) {
      return index;
    },
    leagueDeleteClicked(index) {
      this.$confirm(index, 'Confirm Log Out', {
        confirmButtonText: 'Log Out',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.userLogOut().then(() => {
          this.$message({
            message: 'Logged Out',
            center: true,
          });
          if (this.$route.name.includes('admin')) {
            this.$router.push('/');
          }
        });
      }).catch(() => {
      });
    },
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
