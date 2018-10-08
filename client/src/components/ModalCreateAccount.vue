<template>
  <div id="modal-create-account">
    <div id="create-account-container-main">
      <div id="title">
        Create An Account
      </div>
      <div id="sub-message-container">
        Already have an account?
        <span id="login-link" @click="setLoginModalVisible(true)">
          <u>Log In</u>
        </span>
      </div>
      <form>
        <div id="email-address-container">
          <el-input
            id="firstname-input"
            type="text"
            placeholder="First Name"
            prefix-icon="el-icon-view"
            v-model="firstName">
          </el-input>
        </div>
        <div id="lastname-container">
          <el-input
            id="lastname-input"
            type="text"
            placeholder="Last Name"
            prefix-icon="el-icon-view"
            v-model="lastName">
          </el-input>
        </div>
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
        <div id="confirm-password-container">
          <el-input
            id="confirm-password-input"
            type="password"
            placeholder="Confirm Password"
            prefix-icon="el-icon-tickets"
            v-model="confirmPassword">
          </el-input>
        </div>
        <div id="create-account-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="createAccountButtonClicked">
            {{ createAccountButtonText }}
          </el-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'ModalCreateAccount',
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      confirmPassword: '',
      loading: false,
    };
  },
  computed: {
    createAccountButtonText() {
      return this.loading ? 'Loading' : 'Create Account';
    },
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
    ]),
    createAccountButtonClicked() {
      // TODO finish this
      this.loading = true;
    },
  },
};
</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#modal-create-account{
  #create-account-container-main{
    padding: 0px 40px;
    display: flex;
    flex-direction: column;

    #title{
      font-size: 1.8rem;
      font-weight: bold;
    }

    #sub-message-container{
      margin-bottom: 16px;

      #login-link{
        &:hover{
          cursor: pointer;
        }
      }
    }

    #firstName-container{
      margin: 8px 0px;
    }

    #lastName-container{
      margin: 8px 0px;
    }

    #email-address-container{
      margin: 8px 0px;
    }

    #password-container{
      margin: 8px 0px;
    }

    #create-account-button-container{
      width: 100%;
      margin: 8px 0px;

      button{
        width: 100%;
      }
    }
  }
}
</style>
