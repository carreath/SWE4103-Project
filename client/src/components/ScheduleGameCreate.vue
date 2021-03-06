<template>
  <div id="schedule-game-create">
    <div id="schedule-game-create-container-main">
      <div id="title">
        Create A New Game
      </div>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          label-width="140px"
          :model="scheduleGameCreate"
          :rules="scheduleGameCreateRules"
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
              label="Game Time"
              id="game-time-label"
              prop="gameTime">
              <el-date-picker
                v-model="scheduleGameCreate.gameTime"
                type="datetime"
                placeholder="Select date and time"
                id="game-time-input"
                value-format="yyyy-MM-dd HH:mm:ss">
              </el-date-picker>
          </el-form-item>
          <el-form-item
            label="Home Team Name"
            id="home-team-name-label"
            prop="homeTeamID">
            <el-select
              v-model="scheduleGameCreate.homeTeamID"
              placeholder="Home Team"
              :style="{'float': 'left'}">
              <el-option
                v-for="item in formatHomeTeams"
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
            <el-select
              v-model="scheduleGameCreate.awayTeamID"
              placeholder="Away Team"
              :style="{'float': 'left'}">
              <el-option
                v-for="item in formatAwayTeams"
                :key="item.teamID"
                :label="item.teamName"
                :value="item.teamID">
              </el-option>
            </el-select>
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
  name: 'ScheduleGameCreate',
  data() {
    return {
      labelPosition: 'left',
      scheduleGameCreate: {
        fieldName: '',
        gameTime: '',
        homeTeamID: null,
        awayTeamID: null,
        status: 'Scheduled',
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
        gameTime: [
          {
            required: true,
            message: 'Please input date and time',
            trigger: 'blur',
          },
        ],
        homeTeamID: [
          {
            required: true,
            message: 'Please select Home Team',
            trigger: 'blur',
          },
        ],
        awayTeamID: [
          {
            required: true,
            message: 'Please select Away Team',
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
    formatHomeTeams() {
      const formatedTeams = this.teams.filter(team => {
        return team.teamID !== this.scheduleGameCreate.awayTeamID;
      }).map((team) => {
        return {
          teamID: team.teamID,
          teamName: team.teamName,
          managerID: team.managerID,
        };
      });
      return formatedTeams;
    },
    formatAwayTeams() {
      const formatedTeams = this.teams.filter(team => {
        return team.teamID !== this.scheduleGameCreate.homeTeamID;
      }).map((team) => {
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
              this.$message({
                message: 'Game Created',
                type: 'success',
              });
              this.$router.push('/schedule');
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
  align-items: center;
  margin-top: 16px;
  margin-left: 24px;

  #title{
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 20px;
  }

  #field-name-label{
    margin-top: 16px;
  }

  #teams-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    white-space: nowrap;
    justify-content: space-between;
    margin-left: 16px;
    #home-team-name-label {
      margin-right: 20px;
    }
    .el-select {
      margin-left: 15px;
    }
  }

  #submit-button-container{
    margin-top: 16px;
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  .el-input {
    float: left;
    width: 100%;
  }

  .el-form-item.is-success /deep/ .el-input__inner,
  .el-form-item.is-success /deep/ .el-input__inner:focus,
  .el-form-item.is-success /deep/ .el-textarea__inner,
  .el-form-item.is-success /deep/ .el-textarea__inner:focus {
    border-color: $ELEMENT_UI_DEFAULT_BORDER;
  }
}
</style>
