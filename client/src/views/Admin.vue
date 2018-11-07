<template>
  <div id="admin">
    <AdminLeaguesContainer v-if="curRoute === 'admin-leagues'"/>
<<<<<<< HEAD
    <AdminPlayersContainer v-if="curRoute === 'admin-players'"/>
    <CreatePlayerForm v-if="curRoute === 'create-player-form'"/>
=======
    <AdminLeaguesCreate v-if="curRoute === 'admin-leagues-create'"/>
    <AdminTeamsContainer v-if="curRoute === 'admin-teams'"/>
    <AdminTeamsCreate v-if="curRoute === 'admin-teams-create'"/>

>>>>>>> dev-primary
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import AdminLeaguesContainer from '@/components/AdminLeaguesContainer.vue';
<<<<<<< HEAD
import AdminPlayersContainer from '@/components/AdminPlayersContainer.vue';
import CreatePlayerForm from '@/components/CreatePlayerForm.vue';
=======
import AdminLeaguesCreate from '@/components/AdminLeaguesCreate.vue';
import AdminTeamsContainer from '@/components/AdminTeamsContainer.vue';
import AdminTeamsCreate from '@/components/AdminTeamsCreate.vue';
>>>>>>> dev-primary

export default {
  name: 'Admin',
  data() {
    return {

    };
  },
  components: {
    AdminLeaguesContainer,
<<<<<<< HEAD
    AdminPlayersContainer,
    CreatePlayerForm,
=======
    AdminTeamsContainer,
    AdminLeaguesCreate,
    AdminTeamsCreate,
>>>>>>> dev-primary
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
