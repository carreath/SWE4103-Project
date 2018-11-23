<template>
  <div id="create-schedule-form">
    <div id="create-schedule-form-container-main">
      <div id="title">
        Create Schedule
      </div>
      <div id="info">
        Please input the field availability for the first week of the schedule.
      </div>
      <el-form
        :model="createScheduleForm"
        ref="schedule-form">
        <div id="line-of-input"
          v-for="(line, index) in createScheduleForm.lines"
          :key="line.key">
          <el-form-item
            label="Field"
            id="field-name-label"
            :prop="'lines.' + index + '.fieldName'"
            :rules="[
              { required: true, message: 'Please input Field Name', trigger: 'blur', },
              { min: 1, max: 64, message: 'Input too long', trigger: 'blur', },
            ]">
            <el-input
              id="field-name-input"
              type="fieldName"
              placeholder="Field Name"
              v-model="line.fieldName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
              label="Game Time"
              id="game-time-label"
              :prop="'lines.' + index + '.gameTime'"
              :rules="[
                { required: true, message: 'Please input date and time', trigger: 'blur', },
              ]">
              <el-date-picker
                v-model="line.gameTime"
                type="datetime"
                placeholder="Select date and time"
                id="game-time-input"
                value-format="yyyy-MM-dd HH:mm:ss"
                :disabled="loading">
              </el-date-picker>
          </el-form-item>
          <el-button
            v-if="index !== 0"
            @click="removeLine(line.key)"
            icon="el-icon-remove">
          </el-button>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
        </div>
      </el-form>
      <div id="bottom-button-container">
        <el-button
          icon="el-icon-arrow-left"
          @click="$router.push('/schedule')">
          Cancel
        </el-button>
        <div></div>
        <div>
          <el-button
            @click="addLine">
            New Entry
          </el-button>
          <el-button
          type="primary"
          :loading="loading"
          @click="submitButtonClicked()">
          Create Schedule
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'CreateScheduleForm',
  data() {
    return {
      createScheduleForm: {
        lines: [
          {
            key: 0,
            fieldName: '',
            gameTime: '',
          },
        ],
      },
      loading: false,
      errMsg: null,
    };
  },
  methods: {
    ...mapActions([
      'createSchedule',
    ]),
    submitButtonText() {
      return this.loading ? 'Loading' : 'Create Schedule';
    },
    submitButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['schedule-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.createSchedule(this.createScheduleForm).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
              this.$router.push('/schedule');
            } else {
              this.errMsg = response.retMsg;
            }
          });
        }
      });
    },
    addLine() {
      const newKey =
      this.createScheduleForm.lines[this.createScheduleForm.lines.length - 1].key + 1;
      this.createScheduleForm.lines.push({
        key: newKey,
        field: '',
        day: '',
        time: '',
      });
    },
    removeLine(lineKey) {
      if (this.createScheduleForm.lines.length > 1) {
        this.createScheduleForm.lines =
        this.createScheduleForm.lines.filter(line => line.key !== lineKey);
      }
    },
  },
};
</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#create-schedule-form{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding-top: 16px;
  margin-left: 24px;

  #title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 16px;
    margin-left: 16px;
  }

  #info {
    display: flex;
    font-size: 1.2rem;
    margin-bottom: 16px;
    margin-left: 16px;
  }

  #line-of-input {
    padding-left: 16px;
    margin-top: 16px;
    display: flex;
    flex-direction: row;
    #game-time-label {
      display: flex;
      margin-right: 25px;
    }
    #field-name-label {
      display: flex;
      margin-right: 16px;
    }
    .el-button {
      height: 100%;
    }
  }

  .el-form-item.is-success /deep/ .el-input__inner,
  .el-form-item.is-success /deep/ .el-input__inner:focus,
  .el-form-item.is-success /deep/ .el-textarea__inner,
  .el-form-item.is-success /deep/ .el-textarea__inner:focus {
    border-color: $ELEMENT_UI_DEFAULT_BORDER;
  }
}
#bottom-button-container {
  margin-top: 16px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}
</style>
