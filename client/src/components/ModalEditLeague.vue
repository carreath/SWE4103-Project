<template>
  <div id="modal-edit-league">
    <div id="edit-league-modal-container">
      <div id="title">
        Edit League
      </div>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          :model="leagueEditForm"
          :rules="leagueEditFormRules"
          label-width="120px"
          ref="league-edit-form">
          <el-form-item
            label="League Name"
            class = "label"
            prop="leagueName">
            <el-input
              id="league-name-input"
              type="leagueName"
              placeholder="League Name"
              v-model="leagueEditForm.leagueName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Season"
            class = "label"
            prop="season">
            <el-input
              id="season-input"
              type="season"
              placeholder="Season"
              v-model="leagueEditForm.season"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Point Scheme"
            class = "label"
            prop="pointScheme">
            <el-select
              v-model="leagueEditForm.pointScheme"
              id="point-scheme-input"
              :style="{'float': 'left'}"
              placeholder="Point Scheme">
              <el-option label="Standard" value="standard"></el-option>
              <el-option label="Capital Scoring" value="capitalScoring"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item
            label="Coordinator"
            id="league-coordinator-label"
            prop="managerID">
            <el-select
              v-model="leagueEditForm.managerID"
              id="league-coordinator-input"
              :style="{'float': 'left'}"
              placeholder="Coordinator">
              <el-option label="None" :value="null"></el-option>
              <el-option
                v-for="coordinator in coordinatorUsers"
                :key="coordinator.userID"
                :value="coordinator.userID"
                :label="`${coordinator.firstName} ${coordinator.lastName}`"
                :disabled="coordinatorAlreadyCoordinates(coordinator.userID)">
              </el-option>
            </el-select>
          </el-form-item>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
        </el-form>
      </div>
      <div class="footer">
        <el-button
          :loading="loading"
          @click="closeModal">
          Cancel
        </el-button>
        <div></div>
        <el-button
          type="primary"
          :loading="loading"
          @click="leagueEditButtonClicked">
          {{ leagueEditButtonText }}
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default{
  name: 'ModalEditLeague',
  data() {
    return {
      labelPosition: 'left',
      leagueEditForm: {
        leagueName: '',
        season: '',
        pointScheme: '',
        managerID: null,
      },
      leagueEditFormRules: {
        leagueName: [
          {
            required: true,
            message: 'Please input league name',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        season: [
          {
            required: true,
            message: 'Please input season',
            trigger: 'blur',
          },
        ],
        pointScheme: [
          {
            required: true,
            message: 'Please select Point Scheme',
            trigger: 'change',
          },
        ],
      },
      loading: false,
      errMsg: null,
    };
  },
  computed: {
    ...mapGetters([
      'editLeagueModalVisible',
      'editedLeague',
      'editedLeagueId',
      'leagues',
      'coordinatorUsers',
    ]),
    leagueEditButtonText() {
      return this.loading ? 'Loading' : 'Edit League';
    },
  },
  methods: {
    ...mapActions([
      'closeModal',
      'editLeague',
    ]),
    coordinatorAlreadyCoordinates(userID) {
      return this.leagues.filter(league => league.managerID === userID).length > 0;
    },
    handleKeyUp(e) {
      // Escape ley
      if (e.keyCode === 27) {
        this.closeModal();
      }
      // Enter key
      if (e.keyCode === 13) {
        this.leagueEditButtonClicked();
      }
    },
    leagueEditButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['league-edit-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.editLeague(this.leagueEditForm).then((response) => {
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
    console.log('editedLeague: ', this.editedLeague);
    this.leagueEditForm = { ...this.editedLeague };
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#modal-edit-league{
  #edit-league-modal-container{
    padding: 0px 40px;
    display: flex;
    flex-direction: column;

    #title{
      font-size: 2rem;
      font-weight: bold;
      margin-bottom: 8px;
    }

    .el-form-item.is-success /deep/ .el-input__inner,
    .el-form-item.is-success /deep/ .el-input__inner:focus,
    .el-form-item.is-success /deep/ .el-textarea__inner,
    .el-form-item.is-success /deep/ .el-textarea__inner:focus {
      border-color: $ELEMENT_UI_DEFAULT_BORDER;
    }

    #league-name-input{
      margin: 8px 0px;
    }

    #season-input{
      margin: 8px 0px;
    }

    #point-scheme-input{
      margin: 8px 0px;
    }

    #errMsg{
      color: red;
    }

    #league-edit-button-container{
      width: 100%;
      margin: 8px 0px;

      button{
        width: 50%;
      }
    }

    .footer{
      display: flex;
      justify-content: space-between;
      margin-bottom: 12px;
    }
  }
}
</style>
