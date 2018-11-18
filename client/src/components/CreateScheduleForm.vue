<template>
  <div id="create-schedule-form">
    <div id="create-schedule-form-container-main">
      <div id="title">
        Create Schedule
      </div>
      <el-form
        :model="createScheduleForm"
        :ref="schedule-form"
        :class="demo-dynamic">
        <el-form-item
          v-for="(field, index) in createScheduleForm.fields"
          :label="'Field'"
          :key="field.key"
          :prop="'fields.' + index + '.value'"
          :rules="{
            required: true, message: 'Please input field name', trigger: 'blur'
          }">
          <el-input v-model="field.value"></el-input>
        </el-form-item>
        <el-form-item
          v-for="(day, index) in createScheduleForm.days"
          :label="'Day'"
          :key="day.key"
          :prop="'days.' + index + '.value'"
          :rules="{
            required: true, message: 'Please input day available', trigger: 'blur'
          }">
          <el-select v-model="day.value" placeholder="Select Day">
            <el-option
              v-for="item in options"
              :key="item.value.key"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          v-for="(time, index) in createScheduleForm.times"
          :label="'Time'"
          :key="time.key"
          :prop="'times.' + index + '.value'"
          :rules="{
            required: true, message: 'Please input time available', trigger: 'blur'
          }">
          <el-input v-model="time.value" type="time"></el-input>
          <el-button @click="removeInput(time)">Delete Entry</el-button>
        </el-form-item>
        <el-form-item>
          <el-button
          :type="primary"
          @click="submitScheduleForm('createScheduleForm')">Submit
          </el-button>
          <el-button @click="addField">New Entry</el-button>
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
        fields: [{
          key: 1,
          value: '',
        }],
        days: [{
          key: 1,
          value: '',
        }],
        times: [{
          key: 1,
          value: '',
        }],
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
      'submitScheduleForm',
    ]),
    submitButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['schedule-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.submitScheduleForm(this.createScheduleForm).then((response) => {
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
    addField() {
      this.createScheduleForm.fields.push({
        key: Date.now(),
        value: '',
      });
      this.addDay();
    },
    removeField(index) {
      if (index !== -1) {
        this.createScheduleForm.fields.splice(index, 1);
      }
    },
    addDay() {
      this.createScheduleForm.days.push({
        key: Date.now(),
        value: '',
      });
      this.addTime();
    },
    removeDay(index) {
      this.removeField(index);
      if (index !== -1) {
        this.createScheduleForm.days.splice(index, 1);
      }
    },
    addTime() {
      this.createScheduleForm.times.push({
        key: Date.now(),
        value: '',
      });
    },
    removeTime(index) {
      this.removeDay(index);
      if (index !== -1) {
        this.createScheduleForm.times.splice(index, 1);
      }
    },
    removeInput(index) {
      this.removeTime(index);
    },
  },
};
</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

.el-input {
  width: 40%;
}

</style>
