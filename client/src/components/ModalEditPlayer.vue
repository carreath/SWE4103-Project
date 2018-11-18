<template>
  <div id="modal-edit-player">
    <div id="edit-player-modal-container">
      <div id="title">
        Edit Players
      </div>
      <div id="form-container">
        <el-form
          :label-position="labelPosition"
          :model="playerEditForm"
          :rules="playerEditFormRules"
          label-width="120px"
          ref="player-edit-form">
          <el-form-item
            label="First Name"
            id="first-name-label"
            prop="firstName">
            <el-input
              id="first-name-input"
              type="firstName"
              placeholder="First Name"
              v-model="playerEditForm.firstName"
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
              v-model="playerEditForm.lastName"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <el-form-item
            label="Jersey Number"
            id="number-label"
            prop="number">
            <el-input
              id="number-input"
              type="number"
              placeholder="Jersey Number"
              v-model="playerEditForm.number"
              :disabled="loading">
            </el-input>
          </el-form-item>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
          <el-form-item id="player-edit-button-container">
            <el-button
              type="primary"
              :loading="loading"
              @click="playerEditButtonClicked">
              {{ playerEditButtonText }}
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
  name: 'ModalEditPlayer',
  data() {
    return {
      labelPosition: 'left',
      playerEditForm: {
        firstName: '',
        lastName: '',
        number: '',
      },
      playerEditFormRules: {
        firstName: [
          {
            required: true,
            message: 'Please input first name',
            trigger: 'blur',
          },
        ],
        lastName: [
          {
            required: true,
            message: 'Please input last name',
            trigger: 'blur',
          },
        ],
        number: [
          {
            required: true,
            message: 'Please input jersey number',
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
      'editPlayerModalVisible',
      'editedPlayer',
      'editedPlayerId',
    ]),
    playerEditButtonText() {
      return this.loading ? 'Loading' : 'Edit Team';
    },
  },
  methods: {
    ...mapActions([
      'closeModal',
      'editPlayer',
    ]),
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
    playerEditButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['player-edit-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.editPlayer(this.playerEditForm).then((response) => {
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
    this.playerEditForm = this.editedPlayer;
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';
#modal-edit-player{
  #edit-player-modal-container{
    padding: 0px 40px;
    display: flex;
    flex-direction: column;

    #title{
      font-size: 2rem;
      font-weight: bold;
    }

    .el-form-item.is-success /deep/ .el-input__inner,
    .el-form-item.is-success /deep/ .el-input__inner:focus,
    .el-form-item.is-success /deep/ .el-textarea__inner,
    .el-form-item.is-success /deep/ .el-textarea__inner:focus {
      border-color: $ELEMENT_UI_DEFAULT_BORDER;
    }

    #player-name-input{
      margin: 8px 0px;
    }

    #errMsg{
      color: red;
    }

    #player-edit-button-container{
      width: 100%;
      margin: 8px 0px;

      button{
        width: 50%;
      }
    }
  }
}
</style>
