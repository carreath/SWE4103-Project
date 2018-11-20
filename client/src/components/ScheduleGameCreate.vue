<template>
  <div id="schedule-game-create">
    <div id="schedule-game-create-container-main">
      <div id="title">
        Create A New Game
      </div>
      <div id="form-container">
        <el-form
          :model="scheduleGameCreate"
          :rules="scheduleGameCreateRules"
          label-width="120px"
          ref="game-form">
          <el-form-item
            label="Field"
            id="field-name-label"
            prop="fieldName">
            <el-input
              id="field-name-input"
              type="fieldName"
              placeholder="Field Name"
              v-model="scheduleGameCreate.fieldName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Day"
            id="day-label"
            prop="day">
            <el-select v-model="scheduleGameCreate.day" placeholder="Select Day">
              <el-option
                v-for="item in options"
                :key="item.value.key"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item
              label="Time"
              id="time-label"
              prop="time">
              <el-input v-model="scheduleGameCreate.time" type="time" id="time-input"></el-input>
          </el-form-item>
          <div id="teams-container">
            <el-form-item
              label="Home Team Name"
              id="home-team-name-label"
              prop="homeTeamID">
              <el-select v-model="scheduleGameCreate.homeTeamID" placeholder="Home Team">
                <el-option
                  v-for="item in formatTeams"
                  :key="item.teamID"
                  :label="item.teamName"
                  :value="item.teamID">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item
              label="Away Team Name"
              id="away-team-name-label"
              prop="awayTeamID">
              <el-select v-model="scheduleGameCreate.awayTeamID" placeholder="Away Team">
                <el-option
                  v-for="item in formatTeams"
                  :key="item.teamID"
                  :label="item.teamName"
                  :value="item.teamID">
                </el-option>
              </el-select>
            </el-form-item>
          </div>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
          <el-form-item id="submit-button-container">
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
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default{
  name: 'ScheduleGameCreate',
  data() {
    return {
      scheduleGameCreate: {
        fieldName: '',
        day: '',
        time: '',
        homeTeamID: '',
        awayTeamID: '',
      },
      scheduleGameCreateRules: {
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
        day: [
          {
            required: true,
            message: 'Please input day',
            trigger: 'blur',
          },
        ],
        time: [
          {
            required: true,
            message: 'Please input time',
            trigger: 'blur',
          },
        ],
        homeTeamID: [
          {
            required: true,
            message: 'Please select Team',
            trigger: 'blur',
          },
        ],
        awayTeamID: [
          {
            required: true,
            message: 'Please select Team',
            trigger: 'blur',
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
      return this.loading ? 'Loading' : 'Create Game';
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
      this.$refs['game-form'].validate((valid) => {
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
#schedule-game-create{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 16px;

  #field-name-label{
    margin-top: 16px;
  }

  #teams-container {
    display: flex;
    flex-direction: row;
    white-space: nowrap;
    justify-content: space-between;
  }

  #submit-button-container{
    margin-top: 16px;
    width: 110%;
    justify-content: center;
    align-items: center;
    /deep/ .el-form-item__content{
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
  }

  .el-input {
   width: 120%;
  }

  .el-option {
    float: left;
  }

  .el-form-item.is-success /deep/ .el-input__inner,
  .el-form-item.is-success /deep/ .el-input__inner:focus,
  .el-form-item.is-success /deep/ .el-textarea__inner,
  .el-form-item.is-success /deep/ .el-textarea__inner:focus {
    border-color: $ELEMENT_UI_DEFAULT_BORDER;
  }
}
</style>
