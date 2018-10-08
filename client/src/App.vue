<template>
  <div id="app">
    <ModalWrapper v-if='modalVisible'/>
    <MainHeader/>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
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
