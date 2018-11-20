<template>
  <div id="modal-edit-team">
    <div id="edit-team-modal-container">
      <div id="title">
        Edit Team
      </div>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          :model="teamEditForm"
          :rules="teamEditFormRules"
          label-width="120px"
          ref="team-edit-form">
          <el-form-item
            label="Team Name"
            id="team-name-label"
            prop="teamName">
            <el-input
              id="team-name-input"
              type="teamName"
              placeholder="Team Name"
              v-model="teamEditForm.teamName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Team Colour"
            id="team-colour-label"
            prop="colour">
            <el-color-picker v-model="teamEditForm.colour"></el-color-picker>
          </el-form-item>
          <el-form-item
            label="Manager"
            id="team-manager-label"
            prop="managerID">
            <el-select
              v-model="teamEditForm.managerID"
              id="user-type-input"
              :style="{'float': 'left'}"
              placeholder="Manager">
              <el-option label="None" :value="null"></el-option>
              <el-option
                v-for="manager in managerUsers"
                :key="manager.userID"
                :value="manager.userID"
                :label="`${manager.firstName} ${manager.lastName}`"
                :disabled="managerAlreadyManages(manager.userID)">
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
          @click="teamEditButtonClicked">
          {{ teamEditButtonText }}
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default{
  name: 'ModalEditTeam',
  data() {
    return {
      labelPosition: 'left',
      teamEditForm: {
        teamName: '',
        colour: null,
        managerID: null,
      },
      teamEditFormRules: {
        teamName: [
          {
            required: true,
            message: 'Please input team name',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        colour: [
          {
            required: true,
            message: 'Please input team colour',
            trigger: 'blur',
          },
        ],
        managerID: [
          {
            required: true,
            message: 'Please input team manager',
            trigger: 'blur',
          },
        ],
      },
      loading: false,
      errMsg: null,
    };
  },
  computed: {
    ...mapGetters([
      'editTeamModalVisible',
      'editedTeam',
      'editedTeamId',
      'managerUsers',
      'teams',
    ]),
    teamEditButtonText() {
      return this.loading ? 'Loading' : 'Edit Team';
    },
  },
  methods: {
    ...mapActions([
      'closeModal',
      'editTeam',
    ]),
    managerAlreadyManages(userID) {
      return this.teams.filter(team => team.managerID === userID).length > 0;
    },
    handleKeyUp(e) {
      // Escape ley
      if (e.keyCode === 27) {
        this.closeModal();
      }
      // Enter key
      if (e.keyCode === 13) {
        this.teamEditButtonClicked();
      }
    },
    teamEditButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['team-edit-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.editTeam(this.teamEditForm).then((response) => {
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
    this.teamEditForm = { ...this.editedTeam };
    window.addEventListener('keyup', this.handleKeyUp);
    console.log('teamEditForm: ', this.teamEditForm);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';
#modal-edit-team{
  #edit-team-modal-container{
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

    #team-name-input{
      margin: 8px 0px;
    }

    #errMsg{
      color: red;
    }

    #team-edit-button-container{
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
