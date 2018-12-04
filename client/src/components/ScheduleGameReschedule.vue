<template>
  <div id="schedule-game-reschedule">
    <div id="schedule-game-reschedule-container-main">
      <div id="title">
        Reschedule Game
      </div>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          label-width="140px"
          :model="scheduleGameReschedule"
          :rules="scheduleGameRescheduleRules"
          ref="reschedule-game-form">
          <el-form-item
            label="Field"
            id="field-name-label"
            prop="fieldName">
            <el-input
              id="field-name-input"
              type="fieldName"
              placeholder="Field Name"
              v-model="scheduleGameReschedule.fieldName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
              label="Game Time"
              id="game-time-label"
              prop="gameTime">
              <el-date-picker
                v-model="scheduleGameReschedule.gameTime"
                type="datetime"
                placeholder="Select date and time"
                id="game-time-input"
                value-format="yyyy-MM-dd HH:mm:ss">
              </el-date-picker>
          </el-form-item>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
        </el-form>
        <div id="submit-button-container">
          <el-button
            icon="el-icon-arrow-left"
            @click="$router.push('/schedule')">
            Cancel
          </el-button>
          <div></div>
          <el-button
            type="primary"
            :loading="loading"
            @click="submitButtonClicked">
            {{ submitButtonText }}
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default{
  name: 'ScheduleGameReschedule',
  data() {
    return {
      labelPosition: 'left',
      scheduleGameReschedule: {
        fieldName: '',
        gameTime: '',
        homeTeamID: '',
        awayTeamID: '',
      },
      scheduleGameRescheduleRules: {
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
      value: '',
      loading: false,
      errMsg: null,
    };
  },
  computed: {
    ...mapGetters([
      'teams',
      'leagueById',
    ]),
    formatTeams() {
      const formatedTeams = this.teams.map((team) => {
        return {
          teamID: team.teamID,
          teamName: team.teamName,
          managerID: team.managerID,
        };
      });
      return formatedTeams;
    },
    submitButtonText() {
      return this.loading ? 'Loading' : 'Reschedule Game';
    },
  },
  methods: {
    ...mapActions([
      'createGame',
    ]),
    handleKeyUp(e) {
      // Enter key
      if (e.keyCode === 13) {
        this.submitButtonClicked();
      }
    },
    submitButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['reschedule-game-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.createGame(this.scheduleGameCreate).then((response) => {
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

<style lang="scss" scoped>
@import '@/style/global.scss';

</style>
