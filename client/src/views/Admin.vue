<template>
  <div id="admin">
    <AdminLeaguesContainer v-if="curRoute === 'admin-leagues'"/>
    <AdminLeaguesCreate v-if="curRoute === 'admin-leagues-create'"/>
    <AdminTeamsContainer v-if="curRoute === 'admin-teams'"/>
    <AdminTeamsCreate v-if="curRoute === 'admin-teams-create'"/>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import AdminLeaguesContainer from '@/components/AdminLeaguesContainer.vue';
import AdminLeaguesCreate from '@/components/AdminLeaguesCreate.vue';
import AdminTeamsContainer from '@/components/AdminTeamsContainer.vue';
import AdminTeamsCreate from '@/components/AdminTeamsCreate.vue';

export default {
  name: 'Admin',
  data() {
    return {

    };
  },
  components: {
    AdminLeaguesContainer,
    AdminTeamsContainer,
    AdminLeaguesCreate,
    AdminTeamsCreate,
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
#admin{

}
</style>
