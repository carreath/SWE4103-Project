<template>
  <div id="schedule">
    <!--
    <div id="button-container">
      <div
        id="new-schedule-button"
        v-if="userCanCreateSchedules">
        <el-button
          type="primary"
          @click="handleCreateScheduleButtonClick">Create New Schedule</el-button>
      </div>
      <div
        id="new-game-button"
        v-if="userCanCreateSchedules">
        <el-button
          type="primary"
          @click="handleCreateGameButtonClick">Create New Game</el-button>
      </div>
    </div>
    -->

    <div v-if="curRoute === 'schedule-game'">
      <ScheduleGameInfo/>
    </div>

    <div
      id="schedule-body"
      v-else>
      <div
        id="calendar-view"
        v-if="scheduleSelectedView === 'Calendar'">
        <div id="calendar-view-left">
          <div id="calendar-view-left-header">
            <span>Game Information</span>
          </div>
          <div v-if="!selectedGame">
            No Game Selected
          </div>
          <div
            id="game-info"
            v-else>
            <table>
              <tr>
                <th>Away</th>
                <td
                @click="teamClicked(selectedGame.awayTeamID)"
                :style="{'cursor': 'pointer'}">
                  <ColorCircleTeamName
                    :team="teamById(selectedGame.awayTeamID)"
                    justifyContent="center"/>
                  <span v-if="selectedGame.status === 'Final'">
                    - {{ selectedGame.awayGoals }}
                  </span>
                </td>
              </tr>
              <tr>
                <th>Home</th>
                <td
                @click="teamClicked(selectedGame.homeTeamID)"
                :style="{'cursor': 'pointer'}">
                  <ColorCircleTeamName
                    :team="teamById(selectedGame.homeTeamID)"
                    justifyContent="center"/>
                  <span v-if="selectedGame.status === 'Final'">
                    - {{ selectedGame.homeGoals }}
                  </span>
                </td>
              </tr>
              <tr>
                <th>Field</th>
                <td>{{ selectedGame.fieldName }}</td>
              </tr>
              <tr>
                <th>Date</th>
                <td>{{ formatDate(selectedGame.gameTime.split(' ')[0]) }}</td>
              </tr>
              <tr>
                <th>Time</th>
                <td>{{ formatTime(selectedGame.gameTime.split(' ')[1]) }}</td>
              </tr>
              <tr>
                <th>Status</th>
                <td
                  :class="{'cancelled-event': selectedGame.status === 'Cancelled'}">
                  {{ selectedGame.status }}
                </td>
              </tr>
            </table>
            <el-button
              size="mini"
              @click='gameInfoClicked()'>
              Game Sheet
              <i class="el-icon-d-arrow-right"></i>
            </el-button>
          </div>
        </div>
        <div
          class="calendar-holder">
          <calendar/>
        </div>
      </div>

      <div
        id="table-view"
        v-if="scheduleSelectedView === 'Table'">
        <div
          class="date-games-container"
          v-for="dateGames in tableViewGamesList"
          :key="dateGames.date">
          <div class="date-games-date">
            {{ formatDate(dateGames.date) }}
          </div>
          <table>
            <tr>
              <th>Away</th>
              <th>Home</th>
              <th>Result</th>
              <th>Field</th>
              <th>Time</th>
              <th>Status</th>
              <th></th>
            </tr>
            <tr
              v-for="gameObj in dateGames.games"
              :key="gameObj.gameID"
              :class="{
                'cancelled-event': gameObj.status === 'Cancelled',
                'open-event': gameObj.status === 'Open',
              }"
              @click="gameTableRowClicked(gameObj.gameID)">
              <td>
                <ColorCircleTeamName
                  :team="teamById(gameObj.awayTeamID)"
                  justifyContent="center"/>
              </td>
              <td>
                <ColorCircleTeamName
                  :team="teamById(gameObj.homeTeamID)"
                  justifyContent="center"/>
              </td>
              <td v-if="gameObj.status === 'Final'">
                {{gameObj.awayGoals}} - {{gameObj.homeGoals}}
              </td>
              <td v-else>-</td>
              <td>{{ gameObj.fieldName }}</td>
              <td>{{ formatTime(gameObj.gameTime.split(' ')[1]) }}</td>
              <td>{{ gameObj.status }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Calendar from '@/components/Calendar.vue';
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';
import ScheduleGameInfo from '@/components/ScheduleGameInfo.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Schedule',
  components: {
    Calendar,
    ColorCircleTeamName,
    ScheduleGameInfo,
  },
  data() {
    return {
      localScheduleSelectedView: 'Calendar',
      tableViewGamesList: [],
    };
  },
  computed: {
    ...mapGetters([
      'selectedGameId',
      'selectedGame',
      'scheduleSelectedView',
      'teamById',
      'gamesByLeagueIdSortedByDate',
      'gamesByTeamIdSortedByDate',
      'selectedLeagueId',
      'selectedTeamId',
      'games',
      'user',
      'selectedLeague',
    ]),
    curRoute() {
      return this.$route.name || '';
    },
    userCanCreateSchedules() {
      if (!this.user) {
        return false;
      }
      const userType = this.user.userType;
      switch (userType) {
        case ('Admin'):
          return true;
        case ('Coordinator'):
          return this.selectedLeague.managerID === this.user.userID;
        default:
          return false;
      }
    },
  },
  methods: {
    ...mapActions([
      'setSelectedGameId',
      'setSelectedTeamId',
    ]),
    formatDate(mDate) {
      const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      const tempDate = (mDate || '').split('-');
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
    formatGamesByLeagueIdSortedByDate() {
      const originalGamesObj = this.selectedTeamId ?
        this.gamesByTeamIdSortedByDate(this.selectedTeamId) :
        this.gamesByLeagueIdSortedByDate(this.selectedLeagueId);
      let gamesArr = [];
      Object.keys(originalGamesObj).forEach((key) => {
        const sortedOriginalGamesObj = originalGamesObj[key].sort((a, b) => {
          return Date.parse(a.gameTime) - Date.parse(b.gameTime);
        });
        let gamesObj = {
          date: `${key}`,
          games: sortedOriginalGamesObj,
        };
        gamesArr.push(gamesObj);
      });
      this.tableViewGamesList = gamesArr.sort((a, b) => Date.parse(a.date) - Date.parse(b.date));
    },
    handleCreateGameButtonClick() {
      this.$router.push('/schedule/game/create');
    },
    handleCreateScheduleButtonClick() {
      this.$router.push('/schedule/create');
    },
    gameInfoClicked() {
      this.$router.push('/schedule/game');
    },
    gameTableRowClicked(gameID) {
      this.setSelectedGameId(gameID);
      this.$router.push('/schedule/game');
    },
    teamClicked(id) {
      this.setSelectedTeamId(id);
      this.$router.push('/teams/page');
    },
  },
  watch: {
    selectedTeamId() {
      this.formatGamesByLeagueIdSortedByDate();
    },
    games() {
      this.formatGamesByLeagueIdSortedByDate();
    },
    selectedLeagueId() {
      this.formatGamesByLeagueIdSortedByDate();
    },
  },
  mounted() {
    this.formatGamesByLeagueIdSortedByDate();
  },
};
</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#schedule{
  display: flex;
  flex-direction: column;
  margin-bottom: 8px;

  #button-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }

  #schedule-header{
  }

  #schedule-body{
    display: flex;
    flex-direction: row;
    justify-content: center;

    #calendar-view{
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      width: 100%;

      .calendar-holder{
        display: flex;
        justify-content: flex-end;
        width: 75%;
      }

      #calendar-view-left{
        display: flex;
        flex-direction: column;
        width: 25%;
        border-left: 1px solid #ddd;
        border-bottom: 1px solid #ddd;

        #calendar-view-left-header{
          background-color: #f7f7f7;
          border-color: #ddd;
          border-style: solid;
          min-height: 48px;
          border-width: 1px 0px 1px 0px;
          display: flex;
          align-items: center;
          justify-content: center;

          span{
            font-size: 1.5rem;
            font-weight: bold;
          }
        }

        #game-info{
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: flex-start;

          table{
            width: 100%;
            transition: 0.2s;
            margin-bottom: 8px;

            tr{
              border-bottom: 1px solid #ddd;

              th{
                border-bottom: 1px solid #ddd;
                border-right: 1px solid #ddd;
                background-color: $VERY_LIGHT_GREY;
              }
              td{
                border-bottom: 1px solid #ddd;
              }
            }
          }
        }

      }
    }

    #table-view{
      display: flex;
      flex-direction: column;
      width: 80%;
      align-self: center;

      @include checkMaxScreenSize(750px){
        width: 90%;
      }

      @include checkMaxScreenSize(650px){
        width: 98%;
        font-size: 0.8rem;
      }

      .date-games-container{
        margin: 16px 0px;

        .date-games-date{
          display: flex;
          font-size: 1.5rem;
          font-weight: bold;

          @include checkMaxScreenSize(650px){
            font-size: 1.3rem;
          }
        }

        table{
          width: 100%;
          border: 1px solid #ddd;
          border-collapse:collapse;

          tr{
            border-bottom: 1px solid #ddd;

            th{
              background-color: $HOVER_LIGHT_GREY;
              width: 18%;
              padding: 8px 0px;
            }

            td{
              width: 18%;
              padding: 8px 0px;

              .teamAndColorContainer{
                display: flex;
                justify-content: center;
                align-items: center;
              }
            }

            &:hover{
              :not(th){
                cursor: pointer;
              }
            }
          }
        }
      }
    }

    .cancelled-event{
      background-color: $LIGHT_CANCELLED_RED;
      transition: 0.2s;
    }

    .open-event{
      background-color: $VERY_LIGHT_GREY;
      transition: 0.2s;
    }
  }
}
#new-schedule-button {
  display: flex;
  align-items: right;
  justify-content: flex-end;
  margin-top: 15px;
  margin-right: 15px;
  margin-bottom: 15px;
}
#new-game-button {
  display: flex;
  align-items: right;
  justify-content: flex-end;
  margin-top: 15px;
  margin-right: 15px;
  margin-bottom: 15px;
}
</style>
