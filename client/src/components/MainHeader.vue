<template>
  <div id="main-header">
    <div id="main-header-major">
      <div id="main-header-major-left">
        <img id="soccer-ball-img" src="@/assets/Soccerball.svg" alt="SoccerBall">
        <div
          id="main-header-title"
          @click="mainHeaderClicked">
          Fredericton<br>Football Club
        </div>
      </div>
      <div id="main-header-major-right">
        <WeatherWidget/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import WeatherWidget from '@/components/WeatherWidget.vue';

export default{
  name: 'MainHeader',
  components: {
    WeatherWidget,
  },
  computed: {
    ...mapGetters([
      'user',
      'loggedIn',
    ]),
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
      'setCreateAccountModalVisible',
      'userLogOut',
    ]),
    mainHeaderClicked() {
      this.$router.push('/');
    },
    logoutClicked() {
      this.userLogOut().then(() => {
        this.$message({
          message: 'Logged Out',
          center: true,
        });
      });
    },
  },
};
</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#main-header{
  width: 100%;
  display: flex;
  flex-direction: column;

  #main-header-major{
    background: linear-gradient($PRIMARY_COLOR, $PRIMARY_TO_FADE);
    padding: 0px 8px;
    width: calc(100% - 16px);
    display: flex;
    justify-content: space-between;
    align-items: center;

    #main-header-major-left{
      display: flex;
      flex-direction: row;
      user-select: none;

      &:hover{
        cursor: pointer;
      }

      #soccer-ball-img{
        height: 100px;
        align-self: center;

        @include smallScreenSize{
          display: none;
        }
      }

      #main-header-title{
        color: $SECONDARY_COLOR;
        text-align: start;
        align-self: flex-end;
        font-weight: bold;
        font-size: 2.5rem;
        margin: 0px 4px;
        text-shadow:
          -1px -1px 0 #000,
          1px -1px 0 #000,
          -1px 1px 0 #000,
          1px 1px 0 #000;

        @include checkMaxScreenSize(500px){
          font-size: 36px;
        }
      }
    }

    #main-header-major-right{
      max-height: 100%;
      width: calc(100% - 445px);
      max-width: 316px;

      @include checkMaxScreenSize(780px){
        max-width: 240px;
      }
      @include checkMaxScreenSize(680px){
        max-width: 120px;
      }
      @include checkMaxScreenSize(560px){
        display: none
      }
    }
  }
}
</style>
