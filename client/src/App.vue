<template>
  <div id="app">
    <ModalWrapper v-show='modalVisible'/>
    <MainHeader/>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import MainHeader from '@/components/MainHeader.vue';
import ModalWrapper from '@/components/ModalWrapper.vue';

export default{
  name: 'App',
  components: {
    MainHeader,
    ModalWrapper,
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
