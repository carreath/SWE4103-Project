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
      <el-form
        :model="createAccountForm"
        :rules="createAccountFormRules"
        ref="create-account-form">
        <el-form-item prop="firstName">
          <el-input
            id="firstname-input"
            type="text"
            placeholder="First Name"
            prefix-icon="el-icon-view"
            v-model="createAccountForm.firstName">
          </el-input>
        </el-form-item>
        <el-form-item prop="lastName">
          <el-input
            id="lastname-input"
            type="text"
            placeholder="Last Name"
            prefix-icon="el-icon-view"
            v-model="createAccountForm.lastName">
          </el-input>
        </el-form-item>
        <el-form-item prop="email">
          <el-input
            id="email-address-input"
            type="email"
            placeholder="Email Address"
            prefix-icon="el-icon-message"
            v-model="createAccountForm.email">
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            id="password-input"
            type="password"
            placeholder="Password"
            prefix-icon="el-icon-tickets"
            v-model="createAccountForm.password">
          </el-input>
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input
            id="confirm-password-input"
            type="password"
            placeholder="Confirm Password"
            prefix-icon="el-icon-tickets"
            v-model="createAccountForm.confirmPassword">
          </el-input>
        </el-form-item>
        <el-form-item id="create-account-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="createAccountButtonClicked">
            {{ createAccountButtonText }}
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'ModalCreateAccount',
  data() {
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please input a password'));
      } else {
        if (this.createAccountForm.confirmPassword !== '') {
          this.$refs['create-account-form'].validateField('confirmPassword');
        }
        callback();
      }
    };
    const validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please input a password again'));
      } else if (value !== this.createAccountForm.password) {
        callback(new Error('Passwords don\'t match!'));
      } else {
        callback();
      }
    };
    return {
      createAccountForm: {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: '',
      },
      createAccountFormRules: {
        firstName: [
          {
            required: true,
            message: 'Please input first name',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 32,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        lastName: [
          {
            required: true,
            message: 'Please input last name',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 32,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
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
          {
            validator: validatePass,
            trigger: 'blur',
          },
        ],
        confirmPassword: [
          {
            required: true,
            message: 'Please confirm password',
            trigger: 'blur',
          },
          {
            validator: validatePass2,
            trigger: 'blur',
          },
        ],
      },
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
      this.$refs['create-account-form'].validate((valid) => {
        if (valid) {
          // TODO finish this
          this.loading = true;
        }
      });
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

    .el-form-item.is-success /deep/ .el-input__inner,
    .el-form-item.is-success /deep/ .el-input__inner:focus,
    .el-form-item.is-success /deep/ .el-textarea__inner,
    .el-form-item.is-success /deep/ .el-textarea__inner:focus {
      border-color: $ELEMENT_UI_DEFAULT_BORDER;
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