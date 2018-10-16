<template>
  <div id="home">
    <div id="home-left">
      HOME
    </div>
    <div id="home-right">
      <TwitterFeed/>
    </div>
  </div>
</template>

<script>
import TwitterFeed from '@/components/TwitterFeed.vue';

export default {
  name: 'Home',
  components: {
    TwitterFeed,
  },
};
</script>

<style lang="scss" scoped>
#home{
  display: flex;
  flex-direction: row;
  width: 100%;

  #home-left{
    width: 70%;
  }

  #home-right{
    width: 30%;
    display: flex;
    justify-content: flex-end;
  }
}
</style>
