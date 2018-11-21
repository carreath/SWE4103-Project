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
          v-for="(line) in createScheduleForm.lines"
          :key="line.key">
          <el-form-item
            label="Field"
            id="field-name-label"
            :prop="line.field"
            :rules="{
              required: true, message: 'Please input field name', trigger: 'blur'
            }">
            <el-input v-model="line.field"></el-input>
          </el-form-item>
          <el-form-item
              label="Game Time"
              id="game-time-label"
              prop="gameTime">
              <el-date-picker
                v-model="createScheduleForm.gameTime"
                type="datetime"
                placeholder="Select date and time"
                id="game-time-input"
                value-format="yyyy-MM-dd HH:mm:ss">
              </el-date-picker>
          </el-form-item>
          <el-button @click="removeLine(line.key)">Delete Entry</el-button>
        </div>
        <el-form-item>
          <el-button @click="addLine">New Entry</el-button>
          <el-button
          type="primary"
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
            field: '',
            day: '',
            time: '',
          },
        ],
      },
      options: [
        {
          value: 'Sunday',
          label: 'Sunday',
        },
        {
          value: 'Monday',
          label: 'Monday',
        },
        {
          value: 'Tuesdau',
          label: 'Tuesday',
        },
        {
          value: 'Wednesday',
          label: 'Wednesday',
        },
        {
          value: 'Thursday',
          label: 'Thursday',
        },
        {
          value: 'Friday',
          label: 'Friday',
        },
        {
          value: 'Saturday',
          label: 'Saturday',
        },
      ],
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

  #title {
    font-size: 25px;
    margin-bottom: 16px;
  }

  #info {
    margin-bottom: 16px;
  }

  #line-of-input {
    padding-left: 16px;
    display: flex;
    flex-direction: row;
    .el-input {
      width: 60%;
    }
    .el-select {
      width: 60%;
    }
    .el-button {
      height: 100%;
    }
  }
}
.el-form-item__content {
  display: inline-block;
}
</style>
