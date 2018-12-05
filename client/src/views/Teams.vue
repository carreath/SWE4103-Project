<template>
  <div id="teams">
    <TeamsContainer v-if="curRoute === 'teams'"/>
    <TeamsPage v-if="curRoute === 'teams-page'"/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import TeamsContainer from '@/components/TeamsContainer.vue';
import TeamsPage from '@/components/TeamsPage.vue';

export default {
  name: 'Teams',
  data() {
    return {

    };
  },
  components: {
    TeamsContainer,
    TeamsPage,
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
  padding: 0px 16px;
}
</style>
