<template>
  <div id="modal-wrapper">
    <div id="modal-container">
      <i
        id="close-button"
        class="el-icon-circle-close"
        @click="closeModal">
      </i>
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
            <el-select v-model="leagueEditForm.pointScheme" placeholder="Point Scheme">
              <el-option label="Standard" value="standard"></el-option>
              <el-option label="Capital Scoring" value="capitalScoring"></el-option>
            </el-select>
          </el-form-item>
          <div id="errMsg" v-if="errMsg">
            Error: {{ errMsg }}
          </div>
          <el-form-item id="league-edit-button-container">
            <el-button
              type="primary"
              :loading="loading"
              @click="leagueEditButtonClicked">
              {{ leagueEditButtonText }}
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
  name: 'ModalEditLeague',
  data() {
    return {
      labelPosition: 'left',
      leagueEditForm: {
        leagueName: 'bleh',
        season: 'hi',
        pointScheme: 'Standard',
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
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
};

</script>

<style lang='scss' scoped>
@import '@/style/global.scss';

#modal-wrapper{
  position: fixed;
  z-index: 99;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
  display: flex;
  justify-content: center;
  align-items: center;

  #modal-container{
    width: 350px;
    display: flex;
    flex-direction: column;
    background-color: $SECONDARY_COLOR;
    border-radius: 4px;
    animation: createBox .25s;
    max-height: 100%;
    overflow-y: auto;

    #close-button{
      align-self: flex-end;
      margin-right: 4px;
      margin-top: 4px;
      font-size: 1.2rem;

      &:hover{
        cursor: pointer;
        color: #636363;
      }
    }
  }

  @keyframes createBox {
    from {
      transform: scale(0);
    }
    to {
      transform: scale(1);
    }
  }
}
</style>
