<template>
  <div id="teams">
    TEAMS
    <TeamsContainer v-if="curRoute === 'teams'"/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import TeamsContainer from '@/components/TeamsContainer.vue';

export default {
  name: 'Teams',
  data() {
    return {

    };
  },
  components: {
    TeamsContainer,
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
#teams{

}
</style>
