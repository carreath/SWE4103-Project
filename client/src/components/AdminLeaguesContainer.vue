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
            icon="el-icon-edit"
            size="mini"
            @click='leagueEditClicked(scope.row.id)'>
            </el-button>
            <el-button
            icon="el-icon-delete"
            size="mini"
            @click="leagueDeleteClicked(scope.row.id, scope.row.name)">
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
      'leagueById',
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
      'deleteLeague',
      'setEditedLeague',
      'setEditLeagueModalVisible',
    ]),
    leagueCreateClicked() {
      this.$router.push('/admin/leagues/create');
    },
    leagueEditClicked(index) {
      this.setEditedLeague(index);
      this.setEditLeagueModalVisible(true);
    },
    leagueDeleteClicked(id, name) {
      this.$confirm(`Are you sure you want to delete ${name}? (This will also delete all associated teams and players)`, 'Confirm League Deletion', {
        confirmButtonText: 'Delete League',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.deleteLeague(this.leagueById(id)).then(() => {
          this.$message({
            message: `Deleted ${name}`,
            center: true,
          });
          this.$router.push('/admin/leagues');
        });
      }).catch(() => {
      });
    },
  },
  watch: {
    league() {
      this.formatedLeagues();
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
  .asd {
    background:rgba(0,0,0,0);
    border: 1px solid rgba(0,0,0,0);
    width: 20%;
  }
}
</style>
