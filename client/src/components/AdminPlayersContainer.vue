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
        stripe
        style="width: 100%">
        <el-table-column
          prop="playerID"
          width="110px"
          sortable
          label="Player ID">
        </el-table-column>
        <el-table-column
          prop="fullName"
          label="Name"
          :show-overflow-tooltip="true"
          sortable>
        </el-table-column>
        <el-table-column
          prop="number"
          sortable
          label="Jersey Number">
        </el-table-column>
        <el-table-column
          prop="teamName"
          sortable
          :show-overflow-tooltip="true"
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
      'user',
      'selectedLeagueId',
      'teams',
      'leagues',
    ]),
    formatPlayers() {
      const formatedPlayers = this.players.filter(player => {
        if (!this.user) {
          return false;
        }
        if (this.user.userType === 'Admin') {
          const team = this.teams.find(team => team.teamID === player.teamID);
          return (team || {}).leagueID === this.selectedLeagueId;
        }
        if (this.user.userType === 'Coordinator') {
          const leagueID = (this.leagues.find(league => {
            return league.managerID === this.user.userID;
          }) || {}).leagueID;
          const team = this.teams.find(team => team.teamID === player.teamID);
          return (team || {}).leagueID === leagueID;
        }
        if (this.user.userType === 'Manager') {
          const teamID = (this.teams.find(team => {
            return team.managerID === this.user.userID;
          }) || {}).teamID;
          return teamID === player.teamID;
        }
        return false;
      }).map((player) => {
        return {
          ...player,
          fullName: `${player.firstName} ${player.lastName}`,
          teamName: this.teamById(player.teamID).teamName,
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
        this.deletePlayer(this.playerById(id)).then((response) => {
          if (response.val) {
            this.$message({
              message: `Deleted ${firstName} ${lastName}`,
              center: true,
            });
          } else {
            this.$message.error(response.retMsg);
          }
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
