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
    ]),
  },
  mounted() {
    if (this.token) {
      const base64Url = this.token.split('.')[1];
      console.log('base64Url: ', base64Url);
      const base64 = base64Url.replace('-', '+').replace('_', '/');
      console.log('base64: ', base64);
      const obj = JSON.parse(window.atob(base64));
      console.log('obj: ', obj);

      const tempUser = {
        firstName: obj.sub.split('@')[0],
        lastName: obj.sub.split('@')[1],
        email: obj.sub,
      };
      this.setUser(tempUser);
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
