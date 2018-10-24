<template>
  <div id="schedule">
    <div id="schedule-header">

    </div>
    <div id="schedule-body">
      <div id="calendar-view">
        <div class="calendar-holder">
          <calendar/>
        </div>
        <div id="calendar-game-info-container">
          <div v-if="!selectedGame">
            No Game Selected
          </div>
          <div
            id="game-info"
            v-else>
            <div>
              Home Team - {{ selectedGame.homeTeam }}
            </div>
            <div>
              Away Team - {{ selectedGame.awayTeam }}
            </div>
            <div>
              Field - {{ selectedGame.fieldName }}
            </div>
            <div>
              Date - {{ selectedGame.date }}
            </div>
            <div>
              Time - {{ selectedGame.time }}
            </div>
          </div>
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
    };
  },
  computed: {
    ...mapGetters([
      'selectedGameId',
      'selectedGame',
    ]),
  },
};
</script>

<style lang="scss" scoped>
#schedule{
  display: flex;
  flex-direction: column;
  padding: 8px 0px;

  #schedule-header{

  }

  #schedule-body{
    display: flex;
    flex-direction: row;

    #calendar-view{
      display: flex;
      flex-direction: row;

      .calendar-holder{
        display: flex;
        width: 75%;
        min-width: 800px;
      }

      #calendar-game-info-container{
        display: flex;
        flex-direction: column;

        #game-info{
          display: flex;
          flex-direction: column;
          align-items: flex-start;
        }

      }
    }
  }
}
</style>
