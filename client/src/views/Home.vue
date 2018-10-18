<template>
  <div id="home">
    <div id="home-left">
      <TwitterFeed/>
    </div>
    <div id="home-right">
      HOME
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
    width: 25%;
    display: flex;
    justify-content: flex-start;
  }

  #home-right{
    width: calc(75% - 16px);
    margin: 0px 8px;
  }
}
</style>
