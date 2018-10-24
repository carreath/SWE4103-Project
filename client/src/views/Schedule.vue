<template>
  <div id="schedule">
    <div id="schedule-header">
    </div>
    <div id="schedule-body">
      <div id="calendar-view">
        <div id="calendar-view-left">
          <div id="calendar-view-left-header">
          </div>

          <div v-if="!selectedGame">
            No Game Selected
          </div>
          <div
            id="game-info"
            v-else>
            <h2 class="header">
              Game Informaion
            </h2>
            <ul>
              <li>
                Home Team - {{ selectedGame.homeTeam }}
              </li>
              <li>
                Away Team - {{ selectedGame.awayTeam }}
              </li>
              <li>
                Field - {{ selectedGame.fieldName }}
              </li>
              <li>
                Date - {{ selectedGame.date }}
              </li>
              <li>
                Time - {{ selectedGame.time }}
              </li>
            </ul>
          </div>
        </div>

        <div
          v-if="scheduleSelectedView === 'Calendar'"
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
          min-height: 2.5em;
          border-width: 1px 0px 1px 0px;
          flex: 0 1 auto;
          align-items: center;
          display: flex;
          height: 53px;
        }

        #game-info{
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          justify-content: center;
          height: 100%;

          .header{
            display: flex;
            justify-content: center;
          }

          ul{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            list-style: none;


          }
        }

      }
    }
  }
}
</style>
