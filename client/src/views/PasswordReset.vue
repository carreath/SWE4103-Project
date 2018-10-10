<template>
  <div id="password-reset">
    <div id="title">
      Reset Password
    </div>
    <div id="explanation">
      Lost your password? Please enter the email address you used to sign up and
      click the button below. You will recieve a message containing your
      temporary password.
    </div>
    <el-form
      :model="resetPasswordForm"
      :rules="resetPasswordFormRules"
      ref="reset-password-form">
      <el-form-item prop="email">
        <el-input
          id="email-input"
          type="email"
          placeholder="Email Address"
          prefix-icon="el-icon-message"
          v-model="resetPasswordForm.email">
        </el-input>
      </el-form-item>
      <el-form-item id="reset-password-button-container">
        <el-button
          type="primary"
          :loading="loading"
          @click="resetPasswordButtonClicked">
          {{ resetPasswordButtonText }}
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default{
  name: 'passwordreset',
  data() {
    return {
      resetPasswordForm: {
        email: '',
      },
      resetPasswordFormRules: {
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
      },
      loading: false,
    };
  },
  computed: {
    resetPasswordButtonText() {
      return this.loading ? 'Loading' : 'Reset Password';
    },
  },
  methods: {
    resetPasswordButtonClicked() {
      this.$refs['reset-password-form'].validate((valid) => {
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
#password-reset{
  display: flex;
  flex-direction: column;
  width: 500px;
  padding: 16px 40px;

  #title{
    font-weight: bold;
    font-size: 2rem;
    margin-bottom: 16px;
  }

  #explanation{
    text-align: left;
    margin-bottom: 8px;
  }

  #reset-password-button-container{
    display: flex;
  }
}
</style>
