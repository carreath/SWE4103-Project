<template>
  <div id="login-modal">
    <div id="login-container">
      <i
        id="close-button"
        class="el-icon-circle-close"
        @click="setLoginModalVisible(false)">
      </i>
      <div id="login-container-main">
        <div id="title">
          Log In
        </div>
        <div id="sub-message-container">
          New User? <span><u id="create-account-link">Create an account</u></span>
        </div>
        <form>
          <div id="email-address-container">
            <el-input
              id="email-address-input"
              type="email"
              placeholder="Email Address"
              prefix-icon="el-icon-message"
              v-model="email">
            </el-input>
          </div>
          <div id="password-container">
            <el-input
              id="password-input"
              type="password"
              placeholder="Password"
              prefix-icon="el-icon-tickets"
              v-model="password">
            </el-input>
          </div>
          <div id="login-button-container">
            <el-button
              type="primary"
              :loading="loading">
              Log In
            </el-button>
          </div>
        </form>
      </div>
      <div id="login-container-footer">
        Forgot your password? <span id="reset-password-link"><u>Get it back!</u></span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'LoginModal',
  data() {
    return {
      email: '',
      password: '',
      loading: false,
    };
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
    ]),
    handleKeyUp(e) {
      // Escape ley
      if (e.keyCode === 27) {
        this.setLoginModalVisible(false);
      }
    },
  },
  mounted() {
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#login-modal{
  position: fixed;
  z-index: 99;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
  display: flex;
  justify-content: center;
  align-items: center;

  #login-container{
    width: 350px;
    display: flex;
    flex-direction: column;
    background-color: $SECONDARY_COLOR;
    border-radius: 4px;
    animation: createBox .25s;

    #close-button{
      align-self: flex-end;
      margin-right: 4px;
      margin-top: 4px;
      font-size: 1.2rem;

      &:hover{
        cursor: pointer;
        color: #636363;
      }
    }

    #login-container-main{
      padding: 0px 40px;
      display: flex;
      flex-direction: column;

      #title{
        font-size: 2rem;
        font-weight: bold;
      }

      #sub-message-container{
        margin-bottom: 16px;

        #create-account-link{
          &:hover{
            cursor: pointer;
          }
        }
      }

      #email-address-container{
        margin: 8px 0px;
      }

      #password-container{
        margin: 8px 0px;
      }

      #login-button-container{
        width: 100%;
        margin: 8px 0px;

        button{
          width: 100%;
        }
      }
    }

    #login-container-footer{
      margin-top: 12px;
      padding-top: 8px;
      padding-bottom: 8px;
      background-color: #e8eaed;
      border-radius: 0px 0px 4px 4px;

      #reset-password-link{
        &:hover{
          cursor: pointer;
        }
      }
    }
  }

  @keyframes createBox {
    from {
      transform: scale(0);
    }
    to {
      transform: scale(1);
    }
  }
}
</style>
