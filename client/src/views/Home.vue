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
    width: calc(75% - 16px);

  }

  #home-right{
    width: 25%;
    margin: 0px 8px;
    display: flex;
    justify-content: flex-start;
  }
}
</style>
