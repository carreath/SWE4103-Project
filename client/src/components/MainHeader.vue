<template>
  <div id="main-header">
    <div id="main-header-minor">
      <div
        id="login"
        @click='loginButtonClicked'>
        Login
      </div>
      <div id="create-account">
        Create Account
      </div>
    </div>
    <div id="main-header-major">
      <div id="main-header-major-left">
        <img id="soccer-ball-img" src="@/assets/Soccerball.svg" alt="SoccerBall">
        <!-- TODO clicking this should take user to home page -->
        <div id="main-header-title">
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
  data() {
    return {

    };
  },
  components: {
    WeatherWidget,
  },
  computed: {
    ...mapGetters([
      'loginModalVisible',
    ]),
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
    ]),
    loginButtonClicked() {
      this.setLoginModalVisible(!this.loginModalVisible);
    },
  },
};
</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#main-header{
  height: 212px;
  width: 100%;
  display: flex;
  flex-direction: column;

  #main-header-minor{
    height: 32px;
    background-color: $SECONDARY_COLOR;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-right: 8px;

    #login{
      margin: 0px 4px;
      font-weight: bold;

      &:hover{
        cursor: pointer;
        text-decoration: underline;
      }
    }

    #create-account{
      margin: 0px 4px;

      &:hover{
        cursor: pointer;
        text-decoration: underline;
      }
    }
  }

  #main-header-major{
    height: 180px;
    background: linear-gradient($PRIMARY_COLOR, $PRIMARY_TO_FADE);
    padding: 8px 8px;
    width: calc(100% - 16px);
    display: flex;
    justify-content: space-between;

    #main-header-major-left{
      display: flex;
      flex-direction: row;

      #soccer-ball-img{
        height: 132px;
        align-self: flex-end;

        @include smallScreenSize{
          display: none;
        }
      }

      #main-header-title{
        color: $SECONDARY_COLOR;
        text-align: start;
        align-self: flex-end;
        font-weight: bold;
        font-size: 48px;
        margin: 0px 4px;
        text-shadow:
          -1px -1px 0 #000,
          1px -1px 0 #000,
          -1px 1px 0 #000,
          1px 1px 0 #000;

        @include checkMaxScreenSize(500px){
          font-size: 36px;
        }

        #soccer-ball-img{
          height: 32px;
          width: 32px;
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
