<template>
  <div id="admin-teams-create">
    <div id="title-container">
      <div id="title">
        Create Team
      </div>
    </div>
    <el-form
        :model="teamCreateForm"
        :rules="teamCreateFormRules"
        ref="team-create-form">
        <div>
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
        </div>
        <el-form-item
          label="Team Colour"
          id="team-colour-label"
          prop="teamColour">
          <el-color-picker v-model="teamCreateForm.teamColour"></el-color-picker>
        </el-form-item>
        <div id="errMsg" v-if="errMsg">
          Error: {{ errMsg }}
        </div>
        <el-form-item id="team-create-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="teamCreateButtonClicked">
            {{ teamCreateButtonText }}
          </el-button>
        </el-form-item>
      </el-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'AdminTeamsCreate',
  data() {
    return {
      teamCreateForm: {
        teamName: '',
        teamColour: null,
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
        teamColour: [
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
  #team-name-label{
    padding: 10px;
    margin: 0px;
  }
  #team-colour-label{
    padding: 10px;
    margin: 0px;
  }
  .el-input {
    width: 300px;
    float:left;
  }
  .el-color-picker{
    float:left;
  }
}
</style>
