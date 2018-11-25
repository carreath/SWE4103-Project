<template>
  <div id="admin-players-create">
    <div id="admin-players-create-container-main">
      <h1 id="title">
        Create A New Player
      </h1>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          :model="adminPlayersCreate"
          :rules="adminPlayersCreateRules"
          label-width="120px"
          ref="player-form">
          <el-form-item
            label="First Name"
            id="first-name-label"
            prop="firstName">
            <el-input
              id="first-name-input"
              type="firstName"
              placeholder="First Name"
              v-model="adminPlayersCreate.firstName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Last Name"
            id="last-name-label"
            prop="lastName">
            <el-input
              id="last-name-input"
              type="lastName"
              placeholder="Last Name"
              v-model="adminPlayersCreate.lastName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Team Name"
            id="team-name-label"
            prop="teamID">
            <el-select
              v-model="adminPlayersCreate.teamID"
              :style="{'float': 'left'}"
              placeholder="Select Team">
              <el-option
                v-for="item in formatTeams"
                :key="item.teamID"
                :label="item.teamName"
                :value="item.teamID">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item
            label="Player Number"
            id="player-number-label"
            prop="number">
            <el-input
              id="player-number-input"
              type="number"
              placeholder="Player Number"
              v-model="adminPlayersCreate.number"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
          <el-form-item id="submit-button-container">
            <el-button
              icon="el-icon-arrow-left"
              @click="$router.push('/admin/players')">
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
  name: 'AdminPlayersCreate',
  data() {
    return {
      labelPosition: 'left',
      adminPlayersCreate: {
        firstName: '',
        lastName: '',
        teamID: '',
        number: '',
      },
      adminPlayersCreateRules: {
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
        teamID: [
          {
            required: true,
            message: 'Please select Team',
            trigger: 'blur',
          },
        ],
        number: [
          {
            required: true,
            message: 'Please input Player Number',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 4,
            message: 'Input too long',
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
      'user',
      'selectedLeagueId',
      'leagues',
    ]),
    formatTeams() {
      const formatedTeams = this.teams.filter(team => {
        if (!this.user) {
          return false;
        }
        if (this.user.userType === 'Admin') {
          return team.leagueID === this.selectedLeagueId;
        }
        if (this.user.userType === 'Coordinator') {
          return team.leagueID === (this.leagues.find(league => {
            return league.managerID === this.user.userID;
          }) || {}).leagueID;
        }
        if (this.user.userType === 'Manager') {
          return team.teamID === (this.teams.find(team => {
            return team.managerID === this.user.userID;
          }) || {}).teamID;
        }
        return false;
      });
      return formatedTeams;
    },
    submitButtonText() {
      return this.loading ? 'Loading' : 'Create Player';
    },
  },
  methods: {
    ...mapActions([
      'createPlayer',
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
          this.createPlayer(this.adminPlayersCreate).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
              this.$router.push('/admin/players');
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
#admin-players-create{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 16px;

  #title{
    display: flex;
  }

  #first-name-label{
    margin-top: 16px;
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
