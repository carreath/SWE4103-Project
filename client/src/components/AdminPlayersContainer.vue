<template>
  <div id="admin-players-container">
    <div id="title-container">
      <div id="title">
        Players
      </div>
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
          prop="lastName"
          sortable
          label="Last Name">
        </el-table-column>
        <el-table-column
          prop="firstName"
          sortable
          label="First Name">
        </el-table-column>
        <el-table-column
          prop="teamName"
          sortable
          label="Team Name">
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
  name: 'AdminPlayersContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'players',
      'leagueById',
    ]),
    formatPlayers() {
      const formatedPlayers = this.players.map((player) => {
        return {
          PlayerID: player.playerID,
          lastName: player.lastName,
          firstName: player.firstName,
          teamName: this.teamById(player.teamID).teamName,
        };
      });
      return formatedPlayers;
    },
  },
  methods: {
    ...mapActions([

    ]),
    handleCreatePlayerButtonClick() {
      this.$router.push('/admin/players/create');
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
