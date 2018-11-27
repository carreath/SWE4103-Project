<template>
  <div id="standings">
    <StandingsContainer v-if="curRoute === 'standings'"/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import StandingsContainer from '@/components/StandingsContainer.vue';

export default {
  name: 'Standings',
  data() {
    return {

    };
  },
  components: {
    StandingsContainer,
  },
  computed: {
    ...mapGetters([

    ]),
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([

    ]),
  },
};
</script>

<style lang="scss" scoped>
#standings{
  padding: 0px 16px;
}
</style>
