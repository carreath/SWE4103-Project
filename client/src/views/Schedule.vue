<template>
  <div id="schedule">
    SCHEDULE
    <div class="calendar-holder">
      <calendar/>
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

}
</style>
