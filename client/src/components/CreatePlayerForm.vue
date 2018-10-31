<template>
  <div id="create-player-form">
    <div id="create-player-form-container-main">
      <div id="title">
        Create Player
      </div>
      <el-form
        :model="createPlayerForm"
        :rules="createPlayerFormRules"
        ref="player-form">
        <el-form-item prop="firstName">
          <el-input
            id="firstName-input"
            type="firstName"
            placeholder="First Name"
            prefix-icon="el-icon-message"
            v-model="createPlayerForm.firstName"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item prop="lastName">
          <el-input
            id="lastName-input"
            type="lastName"
            placeholder="Last Name"
            prefix-icon="el-icon-message"
            v-model="createPlayerForm.lastName"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <div id="errMsg" v-if="errMsg">
          Error: {{ errMsg }}
        </div>
        <el-form-item id="submit-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="submitButtonClicked">
            {{ submitButtonText }}
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default{
  name: 'CreatePlayerForm',
  data() {
    return {
      createPlayerForm: {
        firstName: '',
        lastName: '',
      },
      createPlayerFormRules: {
        firstName: [
          {
            required: true,
            message: 'Please input First Name',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        lastName: [
          {
            required: true,
            message: 'Please input Last Name',
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
      errMsg: null,
    };
  },
  computed: {
    submitButtonText() {
      return this.loading ? 'Loading' : 'Submit';
    },
  },
  methods: {
    ...mapActions([
      'submitPlayerForm',
    ]),
    handleKeyUp(e) {
      // Enter key
      if (e.keyCode === 13) {
        this.submitButtonClicked();
      }
    },
    submitButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['player-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.submitPlayerForm(this.createPlayerForm).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
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

#create-player-from{
  #create-player-form-container-main{
    padding: 0px 40px;
    display: flex;
    flex-direction: column;

    #title{
      font-size: 2rem;
      font-weight: bold;
    }

    #sub-message-container{
      margin-bottom: 16px;
    }

    .el-form-item.is-success /deep/ .el-input__inner,
    .el-form-item.is-success /deep/ .el-input__inner:focus,
    .el-form-item.is-success /deep/ .el-textarea__inner,
    .el-form-item.is-success /deep/ .el-textarea__inner:focus {
      border-color: $ELEMENT_UI_DEFAULT_BORDER;
    }

    #firstName-container{
      margin: 8px 0px;
    }

    #lastName-container{
      margin: 8px 0px;
    }

    #errMsg{
      color: red;
    }

    #submit-button-container{
      width: 100%;
      margin: 8px 0px;

      button{
        width: 100%;
      }
    }
  }
}
</style>
