<template>
  <div id="admin-teams-create">
    <div id="title-container">
      <h1 id="title">
        Create A New Team
      </h1>
    </div>
    <div id="form-container">
      <el-form
        :label-position="labelPosition"
        :model="teamCreateForm"
        :rules="teamCreateFormRules"
        label-width="120px"
        ref="team-create-form">
        <el-form-item
          label="Team Name"
          id="team-name-label"
          prop="teamName">
          <el-input
            id="team-name-input"
            type="teamName"
            placeholder="Team Name"
            v-model="teamCreateForm.teamName"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item
          label="Team Colour"
          id="team-colour-label"
          prop="colour">
          <el-color-picker v-model="teamCreateForm.colour"></el-color-picker>
        </el-form-item>
        <div id="errMsg" v-if="errMsg">
          Error: {{ errMsg }}
        </div>
        <el-form-item id="team-create-button-container">
          <el-button
            icon="el-icon-arrow-left"
            @click="$router.push('/admin/leagues')">
            Cancel
          </el-button>
          <div></div>
          <el-button
            type="primary"
            :loading="loading"
            @click="teamCreateButtonClicked">
            {{ teamCreateButtonText }}
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'AdminTeamsCreate',
  data() {
    return {
      labelPosition: 'left',
      teamCreateForm: {
        teamName: '',
        colour: null,
      },
      teamCreateFormRules: {
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
      },
      loading: false,
      errMsg: null,
    };
  },
  computed: {
    teamCreateButtonText() {
      return this.loading ? 'Loading' : 'Create Team';
    },
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([
      'createTeam',
    ]),
    teamCreateButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['team-create-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.createTeam(this.teamCreateForm).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
              this.$router.push('/admin/teams');
            } else {
              this.errMsg = response.retMsg;
            }
          });
        }
      });
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-create{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 16px;

  #form-container{
    max-width: 80%;
    display: flex;
    justify-content: center;
    align-items: center;

    #team-create-button-container{
      margin-top: 16px;
      /deep/ .el-form-item__content{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
      }
    }
  }

  #team-name-label{
    padding: 10px;
    margin: 0px;
  }
  #team-colour-label{
    padding: 10px;
    margin: 0px;
  }
  .el-input {
    width: 350px;
    float:left;
  }
  .el-select{
    float:left;
  }
  .label{
    padding: 10px;
    margin: 0px;
  }

  .el-form-item.is-success /deep/ .el-input__inner,
  .el-form-item.is-success /deep/ .el-input__inner:focus,
  .el-form-item.is-success /deep/ .el-textarea__inner,
  .el-form-item.is-success /deep/ .el-textarea__inner:focus {
    border-color: $ELEMENT_UI_DEFAULT_BORDER;
  }
}
</style>
