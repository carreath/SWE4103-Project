<template>
  <div id="modal-login">
    <div id="login-container-main">
      <div id="title">
        Log In
      </div>
      <div id="sub-message-container">
        New User?
        <span id="create-account-link" @click="setCreateAccountModalVisible(true)">
          <u>Create an account</u>
        </span>
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
            :loading="loading"
            @click="loginButtonClicked">
            {{ loginButtonText }}
          </el-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'ModalLogin',
  data() {
    return {
      email: '',
      password: '',
      loading: false,
    };
  },
  computed: {
    loginButtonText() {
      return this.loading ? 'Loading' : 'Log In';
    },
  },
  methods: {
    ...mapActions([
      'setCreateAccountModalVisible',
    ]),
    loginButtonClicked() {
      // TODO finish this
      this.loading = true;
    },
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#modal-login{
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
}
</style>
