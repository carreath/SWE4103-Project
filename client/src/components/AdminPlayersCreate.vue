<template>
  <div id="admin-players-create">
    <div id="admin-players-create-container-main">
      <div id="title">
        Create A New Player
      </div>
      <div id="form-container">
        <el-form
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
            prop="team">
            <el-select v-model="adminPlayersCreate.team" placeholder="Select Team">
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
        team: [
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
