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
                <th>Home</th>
                <td>{{ selectedGame.homeTeam }}</td>
              </tr>
              <tr>
                <th>Away</th>
                <td>{{ selectedGame.awayTeam }}</td>
              </tr>
              <tr>
                <th>Field</th>
                <td>{{ selectedGame.fieldName }}</td>
              </tr>
              <tr>
                <th>Date</th>
                <td>{{ selectedGame.date }}</td>
              </tr>
              <tr>
                <th>Time</th>
                <td>{{ selectedGame.time }}</td>
              </tr>
            </table>
          </div>
        </div>
        <div
          class="calendar-holder">
          <calendar/>
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
    };
  },
  computed: {
    ...mapGetters([
      'selectedGameId',
      'selectedGame',
      'scheduleSelectedView',
    ]),
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
  }
}
</style>
