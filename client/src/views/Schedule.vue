<template>
  <div id="schedule">
    <div id="schedule-header">

    </div>
    <div id="schedule-body">
      <div class="calendar-holder">
        <calendar/>
      </div>
      <div id="schedule-options-container">

      </div>
    </div>
  </div>
</template>

<script>
import Calendar from '@/components/Calendar.vue';

export default {
  name: 'Schedule',
  components: {
    Calendar,
  },
  data() {
    return {
    };
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

    .calendar-holder{
      display: flex;
      width: 75%;
      min-width: 800px;
    }

    #schedule-options-container{


    }
  }
}
</style>
