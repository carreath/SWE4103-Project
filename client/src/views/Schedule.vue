<template>
  <div id="schedule">
    <div id="schedule-header">
    </div>
    <div id="schedule-body">
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
                <td>
                  {{ teamById(selectedGame.awayTeamID).teamName }}
                  <span v-if="selectedGame.status === 'Final'">
                    - {{ selectedGame.awayGoals }}
                  </span>
                </td>
              </tr>
              <tr>
                <th>Home</th>
                <td>
                  {{ teamById(selectedGame.homeTeamID).teamName }}
                  <span v-if="selectedGame.status === 'Final'">
                    - {{ selectedGame.homeGoals }}
                  </span>
                </td>
              </tr>
              <tr>
                <th>Field</th>
                <td>{{ selectedGame.field }}</td>
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
            </tr>
            <tr
              v-for="gameObj in dateGames.games"
              :key="gameObj.gameID"
              :class="{
                'cancelled-event': gameObj.status === 'Cancelled',
                'open-event': gameObj.status === 'Open',
              }">
              <td>{{ teamById(gameObj.awayTeamID).teamName }}</td>
              <td>{{ teamById(gameObj.homeTeamID).teamName }}</td>
              <td v-if="gameObj.status === 'Final'">
                {{gameObj.awayGoals}} - {{gameObj.homeGoals}}
              </td>
              <td v-else>-</td>
              <td>{{ gameObj.field }}</td>
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
import { mapGetters } from 'vuex';

export default {
  name: 'Schedule',
  components: {
    Calendar,
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
    ]),
  },
  methods: {
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
  },
  watch: {
    selectedTeamId() {
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
          align-items: flex-start;
          justify-content: flex-start;

          table{
            width: 100%;
            transition: 0.2s;

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

      .date-games-container{
        margin: 16px 0px;
        transition: 0.5s;

        .date-games-date{
          display: flex;
          font-size: 1.5rem;
          font-weight: bold;
        }

        table{
          width: 100%;
          border: 1px solid #ddd;
          border-collapse:collapse;
          transition: 0.5s;

          tr{
            border-bottom: 1px solid #ddd;
            transition: 0.5s;

            th{
              background-color: $HOVER_LIGHT_GREY;
              width: 18%;
              padding: 8px 0px;
            }

            td{
              width: 18%;
              padding: 8px 0px;
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
</style>
