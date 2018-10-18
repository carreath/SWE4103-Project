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
      <el-form
        :model="loginForm"
        :rules="loginFormRules"
        ref="login-form">
        <el-form-item prop="email">
          <el-input
            id="email-input"
            type="email"
            placeholder="Email Address"
            prefix-icon="el-icon-message"
            v-model="loginForm.email"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            id="password-input"
            type="password"
            placeholder="Password"
            prefix-icon="el-icon-tickets"
            v-model="loginForm.password"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <div id="errMsg" v-if="errMsg">
          Error: {{ errMsg }}
        </div>
        <el-form-item id="login-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="loginButtonClicked">
            {{ loginButtonText }}
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'ModalLogin',
  data() {
    return {
      loginForm: {
        email: '',
        password: '',
      },
      loginFormRules: {
        email: [
          {
            required: true,
            message: 'Please input email',
            trigger: 'blur',
          },
          {
            type: 'email',
            message: 'Please input correct email address',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        password: [
          {
            required: true,
            message: 'Please input password',
            trigger: 'blur',
          },
        ],
      },
      loading: false,
      errMsg: null,
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
      'closeModal',
      'userLogIn',
    ]),
    handleKeyUp(e) {
      // Escape ley
      if (e.keyCode === 27) {
        this.closeModal();
      }
      // Enter key
      if (e.keyCode === 13) {
        this.loginButtonClicked();
      }
    },
    loginButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['login-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.userLogIn(this.loginForm).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
              this.closeModal();
            } else {
              this.errMsg = response.retMsg;
            }
          });
        }
      });
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

    .el-form-item.is-success /deep/ .el-input__inner,
    .el-form-item.is-success /deep/ .el-input__inner:focus,
    .el-form-item.is-success /deep/ .el-textarea__inner,
    .el-form-item.is-success /deep/ .el-textarea__inner:focus {
      border-color: $ELEMENT_UI_DEFAULT_BORDER;
    }

    #email-address-container{
      margin: 8px 0px;
    }

    #password-container{
      margin: 8px 0px;
    }

    #errMsg{
      color: red;
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
