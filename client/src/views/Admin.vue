<template>
  <div id="admin">
    <AdminLeaguesContainer v-if="curRoute === 'admin-leagues'"/>
    <AdminPlayersContainer v-if="curRoute === 'admin-players'"/>
    <AdminPlayersCreate v-if="curRoute === 'admin-players-create'"/>
    <AdminLeaguesCreate v-if="curRoute === 'admin-leagues-create'"/>
    <AdminTeamsContainer v-if="curRoute === 'admin-teams'"/>
    <AdminTeamsCreate v-if="curRoute === 'admin-teams-create'"/>
    <AdminUsersContainer v-if="curRoute === 'admin-users'"/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import AdminLeaguesContainer from '@/components/AdminLeaguesContainer.vue';
import AdminPlayersContainer from '@/components/AdminPlayersContainer.vue';
import AdminPlayersCreate from '@/components/AdminPlayersCreate.vue';
import AdminLeaguesCreate from '@/components/AdminLeaguesCreate.vue';
import AdminTeamsContainer from '@/components/AdminTeamsContainer.vue';
import AdminTeamsCreate from '@/components/AdminTeamsCreate.vue';
import AdminUsersContainer from '@/components/AdminUsersContainer.vue';

export default {
  name: 'Admin',
  data() {
    return {

    };
  },
  components: {
    AdminLeaguesContainer,
    AdminPlayersContainer,
    AdminPlayersCreate,
    AdminTeamsContainer,
    AdminLeaguesCreate,
    AdminTeamsCreate,
    AdminUsersContainer,
  },
  computed: {
    ...mapGetters([

    ]),
    curRoute() {
      return this.$route.name || '';
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
  padding: 0px 24px;
}
</style>
