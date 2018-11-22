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
        :rules="createScheduleRules"
        ref="schedule-form">
        <div id="line-of-input"
          v-for="(line) in createScheduleForm.lines"
          :key="line.key">
          <el-form-item
            label="Field"
            id="field-name-label"
            prop="fieldName">
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
              prop="gameTime">
              <el-date-picker
                v-model="line.gameTime"
                type="datetime"
                placeholder="Select date and time"
                id="game-time-input"
                value-format="yyyy-MM-dd HH:mm:ss"
                :disabled="loading">
              </el-date-picker>
          </el-form-item>
          <el-button @click="removeLine(line.key)">Delete Entry</el-button>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
        </div>
        <el-form-item id="bottom-button-container">
          <el-button @click="addLine">New Entry</el-button>
          <el-button
          type="primary"
          :loading="loading"
          @click="submitButtonClicked()"> Create Schedule
          </el-button>
        </el-form-item>
      </el-form>
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
      createScheduleRules: {
        fieldName: [
          {
            required: true,
            message: 'Please input Field Name',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        gameTime: [
          {
            required: true,
            message: 'Please input date and time',
            trigger: 'blur',
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
  justify-content: space-between;
  padding-top: 16px;
  width: 150%;

  #title {
    font-size: 25px;
    margin-bottom: 16px;
  }

  #info {
    margin-bottom: 16px;
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
}
#bottom-button-container {
  margin-top: 16px;
}
</style>
