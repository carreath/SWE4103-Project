<template>
  <div id="app">
    <LoginModal v-if='loginModalVisible'/>
    <MainHeader/>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MainHeader from '@/components/MainHeader.vue';
import LoginModal from '@/components/LoginModal.vue';

export default{
  name: 'App',
  components: {
    MainHeader,
    LoginModal,
  },
  computed: {
    ...mapGetters([
      'loginModalVisible',
    ]),
  },
};

</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
