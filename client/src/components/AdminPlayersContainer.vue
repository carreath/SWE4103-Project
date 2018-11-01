<template>
  <div id="admin-players-container">
    <div id="title-container">
      <div id="title">
        Players
      </div>
    </div>
    <div id="create-player-button-container">
      <el-button
        type="primary"
        @click="handleCreatePlayerButtonClick">Create Player</el-button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminPlayersContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'players',
    ]),
  },
  methods: {
    ...mapActions([

    ]),
    handleCreatePlayerButtonClick() {
      this.$router.push('/admin/players/create');
    },
  },
};

</script>

<style lang="scss" scoped>
#admin-players-container{

  #create-player-button-container{
    padding: 0px 20px;
    font-weight: bold;
    display: flex;
    list-style-type: none;
    margin: 0;
    height: 100%;
}
</style>
