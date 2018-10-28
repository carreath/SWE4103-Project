<template>
  <div id="admin-teams-create">
    <div id="title-container">
      <div id="title">
        Create Team
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminTeamsCreate',
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters([
      'teams',
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
@import '@/style/global.scss';
#admin-teams-create{

}
</style>
