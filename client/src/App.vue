<template>
  <div id="app">
    <ModalWrapper v-show='modalVisible'/>
    <UpcomingGamesHeader/>
    <MainHeader/>
    <div id="router-view-outer-wrapper">
      <div id="router-view-inner-wrapper">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import MainHeader from '@/components/MainHeader.vue';
import ModalWrapper from '@/components/ModalWrapper.vue';
import UpcomingGamesHeader from '@/components/UpcomingGamesHeader.vue';

export default{
  name: 'App',
  components: {
    MainHeader,
    ModalWrapper,
    UpcomingGamesHeader,
  },
  computed: {
    ...mapGetters([
      'modalVisible',
      'token',
    ]),
  },
  methods: {
    ...mapActions([
      'setUser',
      'retrieveUserFromToken',
    ]),
  },
  mounted() {
    if (this.token) {
      this.retrieveUserFromToken();
    }
  },
};

</script>

<style lang="scss">
@import '@/style/global.scss';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  #router-view-outer-wrapper{
    padding: 0px 20px;
    /*background-color: #e8e8e8;*/
    background-color: $SECONDARY_COLOR;

    #router-view-inner-wrapper{
      background-color: $SECONDARY_COLOR;
    }
  }
}

</style>
