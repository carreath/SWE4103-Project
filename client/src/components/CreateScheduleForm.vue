<template>
  <div id="create-schedule-form">
    <div id="create-schedule-form-container-main">
      <div id="title">
        Create Schedule
      </div>
      <el-form
        :model="createScheduleForm"
        :rules="createScheduleFormRules"
        ref="schedule-form">
        <el-form-item prop="field">
          <el-input
            id="field-input"
            type="field"
            placeholder="Field Name"
            prefix-icon="el-icon-message"
            v-model="createScheduleForm.field"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item prop="day">
          <el-input
            id="day-input"
            type="day"
            placeholder="Day Available"
            prefix-icon="el-icon-message"
            v-model="createScheduleForm.day"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item prop="time">
          <el-input
            id="time-input"
            type="time"
            placeholder="Time Available"
            prefix-icon="el-icon-message"
            v-model="createScheduleForm.time"
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
  name: 'CreateScheduleForm',
  data() {
    return {
      createScheduleForm: {
        field: '',
        day: '',
        time: '',
      },
      createScheduleFormRules: {
        field: [
          {
            required: true,
            message: 'Please input field',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        day: [
          {
            required: true,
            message: 'Please input day available',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        time: [
          {
            required: true,
            message: 'Please input time available',
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
      'closeModal',
      'submitScheduleForm',
    ]),
    handleKeyUp(e) {
      // Escape ley
      if (e.keyCode === 27) {
        this.closeModal();
      }
      // Enter key
      if (e.keyCode === 13) {
        this.submitButtonClicked();
      }
    },
    submitButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['schedule-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.submitScheduleForm(this.createScheduleForm).then((response) => {
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

#create-schedule-from{
  #create-schedule-form-container-main{
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

    #field-container{
      margin: 8px 0px;
    }

    #day-container{
      margin: 8px 0px;
    }

    #time-container{
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
