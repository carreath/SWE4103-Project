<template>
  <div id="admin">
    <div>
      Admin Panel
    </div>
    <AdminLeaguesContainer v-if="curRoute === 'admin-leagues'"/>
    <AdminPlayersContainer v-if="curRoute === 'admin-players'"/>
    <CreatePlayerForm v-if="curRoute === 'create-player-form'"/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import AdminLeaguesContainer from '@/components/AdminLeaguesContainer.vue';
import AdminPlayersContainer from '@/components/AdminPlayersContainer.vue';
import CreatePlayerForm from '@/components/CreatePlayerForm.vue';

export default {
  name: 'Admin',
  data() {
    return {

    };
  },
  components: {
    AdminLeaguesContainer,
    AdminPlayersContainer,
    CreatePlayerForm,
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
