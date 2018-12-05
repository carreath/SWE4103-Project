<template>
  <div id="home">
    <div id="home-left">
      Gallery
      <div id="carousel-container">
        <el-carousel
          trigger="click"
          type="card"
          interval=3900
          indicator-position="outside">
          <el-carousel-item>
            <img src="@/assets/Team.jpg" alt="TEAM 2 WOO">
          </el-carousel-item>
          <el-carousel-item>
            <img src="@/assets/BenAndToes.jpg" alt="TEAM 2 WOO">
          </el-carousel-item>
          <el-carousel-item>
            <img src="@/assets/Josh.jpg" alt="TEAM 2 WOO">
          </el-carousel-item>
          <el-carousel-item>
            <img src="@/assets/Zach.png" alt="TEAM 2 WOO">
          </el-carousel-item>
          <el-carousel-item>
            <img src="@/assets/Caleb.jpg" alt="TEAM 2 WOO">
          </el-carousel-item>
          <el-carousel-item>
            <img src="@/assets/Cam.jpg" alt="TEAM 2 WOO">
          </el-carousel-item>
        </el-carousel>
      </div>
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
  data() {
    return {

    };
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
    height: 100%;

    #carousel-container{
      img{
        max-height: 100%;
        max-width: 100%;
        border-radius: 8px;
      }

      .el-carousel__item h3 {
        background-color: #99a9bf;
      }
    }

  }

  #home-right{
    width: 25%;
    margin: 0px 8px;
    display: flex;
    justify-content: flex-start;
  }
}
</style>
