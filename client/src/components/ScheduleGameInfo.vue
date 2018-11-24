<template>
  <div id="schedule-game-info">
    <div id="header-info">
      <div id="back-button-container">
        <el-button
          size="medium"
          @click="backToScheduleClicked()">
          <i class="el-icon-d-arrow-left"></i>
          Back
        </el-button>
      </div>
      <div id="main-game-info">
        <div id="team-names">
          <ColorCircleTeamName
            :team="teamById(localSelectedGame.awayTeamID)"
            justifyContent="center"/>
          <span id="vs-span">vs.</span>
          <ColorCircleTeamName
            :team="teamById(localSelectedGame.homeTeamID)"
            justifyContent="center"/>
        </div>
        <div id="location-info">
          at {{ localSelectedGame.fieldName }}
        </div>
        <div
          id="date-time-info"
          v-if="selectedGame">
          {{ formatDate(localSelectedGame.gameTime.split(' ')[0]) }}
          at
          {{ formatTime(localSelectedGame.gameTime.split(' ')[1]) }}
        </div>
        <div
          id="cancelled-header"
          v-if="localSelectedGame.status === 'Cancelled'">
          CANCELLED
        </div>
      </div>
      <div id="game-actions-container">
        <el-button
          v-if="showCancelButton"
          size="medium"
          @click="cancelGameButtonClicked()"
          type="danger"
          plain>
          <i class="el-icon-circle-close-outline"></i>
          Cancel Game
        </el-button>
      </div>
    </div>

    <!-- TODO This will have to be finished when game objects can be set to 'Final' -->
    <div
      id="game-info-final-score"
      v-if="localSelectedGame.status === 'Final'">
      <div id="final-score-away-team">
        <div class="team-name">
          <ColorCircleTeamName
            :team="teamById(localSelectedGame.awayTeamID)"
            justifyContent="center"/>
        </div>
        <div class="team-score">
          {{localSelectedGame.awayGoals}}
        </div>
        <div>
          FINAL
        </div>
        <div id="final-score-home-team">
          <div class="team-name">
            <ColorCircleTeamName
              :team="teamById(localSelectedGame.awayTeamID)"
              justifyContent="center"/>
          </div>
          <div class="team-score">
            {{localSelectedGame.awayGoals}}
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';

export default {
  name: 'ScheduleGameInfo',
  data() {
    return {

    };
  },
  components: {
    ColorCircleTeamName,
  },
  computed: {
    ...mapGetters([
      'selectedGame',
      'teamById',
      'user',
      'selectedLeagueId',
    ]),
    showCancelButton() {
      if (!this.user) {
        return false;
      }
      if (this.selectedGame.status === 'Cancelled') {
        return false;
      }
      const userType = this.user.userType;
      switch (userType) {
        case ('Admin'):
          return true;
        case ('Coordinator'):
          return (this.selectedLeague || {}).managerID === this.user.userID;
        default:
          return false;
      }
    },
    localSelectedGame() {
      return this.selectedGame || {};
    },
  },
  methods: {
    ...mapActions([
      'editGame',
    ]),
    backToScheduleClicked() {
      this.$router.push('/schedule');
    },
    formatDate(mDate) {
      const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      const tempDate = mDate.split('-');
      return `${months[Number(tempDate[1]) - 1]} ${tempDate[2]}, ${tempDate[0]}`;
    },
    formatTime(mTime) {
      // Check correct time format and split into components
      let time = mTime.toString().match(/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [mTime];
      time[4] = ' ';// Change seconds to just a space
      if (time.length > 1) { // If time format correct
        time = time.slice(1); // Remove full string match value
        time[5] = +time[0] < 12 ? 'AM' : 'PM'; // Set AM/PM
        time[0] = +time[0] % 12 || 12; // Adjust hours
      }
      return time.join(''); // return adjusted time or original string
    },
    cancelGameButtonClicked() {
      this.$confirm('Are you sure you want to cancel this game?', 'Confirm Game Cancellation', {
        confirmButtonText: 'Cancel Game',
        cancelButtonText: 'No',
        type: 'warning',
      }).then(() => {
        const updateGameObj = { ...this.selectedGame };
        updateGameObj.status = 'Cancelled';
        this.editGame(updateGameObj).then((response) => {
          if (response.retVal) {
            this.$message({
              message: 'Game Cancelled',
              center: true,
            });
          } else {
            this.$message.error(response.retMsg);
          }
        });
      }).catch(() => {
      });
    },
  },
  watch: {
    selectedLeagueId() {
      this.$router.push('/schedule');
    },
  },
  mounted() {
    if (!this.selectedGame) {
      this.$router.push('/schedule');
    }
  },
};
</script>

<style lang="scss">
@import '@/style/global.scss';

#schedule-game-info{
  display: flex;
  flex-direction: column;
  margin: 8px 16px;

  #header-info{
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    #back-button-container{

    }

    #main-game-info{
      display: flex;
      flex-direction: column;

      #team-names{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        font-weight: bold;

        #vs-span{
          margin: 0px 8px;
        }
      }

      #cancelled-header{
        font-weight: bold;
        color: $CANCELLED_RED;
      }
    }
  }

  #game-info-final-score{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    #final-score-away-team,
    #final-score-home-team{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
  }
}
</style>
