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
      id="reset-password-form"
      :model="resetPasswordForm"
      :rules="resetPasswordFormRules"
      ref="reset-password-form"
      @submit.native.prevent>
      <el-form-item
        prop="email"
        :style="{'is-success': false}">
        <el-input
          id="reset-password-email-input"
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
import { mapGetters } from 'vuex';

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
    ...mapGetters([
      'loggedIn',
    ]),
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
  watch: {
    loggedIn(val) {
      if (val) {
        this.$router.push('/');
      }
    },
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push('/');
    }
  },
};
</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#password-reset{
  display: flex;
  flex-direction: column;
  width: 500px;
  max-width: calc(100% - 80px);
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

  .el-form-item.is-success /deep/ .el-input__inner,
  .el-form-item.is-success /deep/ .el-input__inner:focus,
  .el-form-item.is-success /deep/ .el-textarea__inner,
  .el-form-item.is-success /deep/ .el-textarea__inner:focus {
    border-color: $ELEMENT_UI_DEFAULT_BORDER;
  }

  #reset-password-button-container{
    display: flex;
  }
}
</style>
