<template>
  <div id="admin-players-container">
    <div id="title-container">
    </div>
    <div id="create-player-button-container">
      <el-button
        type="primary"
        @click="handleCreatePlayerButtonClick">Create Player</el-button>
    </div>
    <div id="players-table-container">
      <el-table
        :data="formatPlayers"
        :default-sort = "{prop: 'playerID', order: 'ascending'}"
        stripe
        style="width: 100%">
        <el-table-column
          prop="playerID"
          sortable
          label="Player ID">
        </el-table-column>
        <el-table-column
          prop="number"
          sortable
          label="Jersey Number">
        </el-table-column>
        <el-table-column
          prop="firstName"
          sortable
          label="First Name">
        </el-table-column>
        <el-table-column
          prop="lastName"
          sortable
          label="Last Name">
        </el-table-column>
        <el-table-column
          prop="teamName"
          sortable
          label="Team Name">
        </el-table-column>
        <el-table-column
          label="Action">
          <template slot-scope="scope">
            <el-button
            icon="el-icon-edit"
            size="mini"
            @click='playerEditClicked(scope.row.playerID)'>
            </el-button>
            <el-button
            icon="el-icon-delete"
            size="mini"
            @click="playerDeleteClicked(scope.row.playerID,
            scope.row.firstName, scope.row.lastName)">
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
  name: 'AdminPlayersContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'players',
      'teamById',
      'playerById',
    ]),
    formatPlayers() {
      const formatedPlayers = this.players.map((player) => {
        return {
          playerID: player.playerID,
          lastName: player.lastName,
          firstName: player.firstName,
          teamName: this.teamById(player.teamID).teamName,
          number: player.number,
        };
      });
      return formatedPlayers;
    },
  },
  methods: {
    ...mapActions([
      'deletePlayer',
      'setEditedPlayer',
      'setEditPlayerModalVisible',
    ]),
    handleCreatePlayerButtonClick() {
      this.$router.push('/admin/players/create');
    },
    playerEditClicked(index) {
      this.setEditedPlayer(index);
      this.setEditPlayerModalVisible(true);
    },
    playerDeleteClicked(id, firstName, lastName) {
      this.$confirm(`Are you sure you want to delete ${firstName} ${lastName}?`, 'Confirm Player Deletion', {
        confirmButtonText: 'Delete Player',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.deletePlayer(this.playerById(id)).then(() => {
          this.$message({
            message: `Deleted ${firstName} ${lastName}`,
            center: true,
          });
          this.$router.push('/admin/players');
        });
      }).catch(() => {
      });
    },
  },
  watch: {
    player() {
      this.formatedPlayers();
    },
  },
};

</script>

<style lang="scss" scoped>
#admin-players-container{

  #create-player-button-container{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    height: 61px;
    transition: 0.3s;
  }
}
</style>
