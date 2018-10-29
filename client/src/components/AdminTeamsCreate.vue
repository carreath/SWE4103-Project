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
        ref="team-form">
        <el-form-item
          label="Team Name"
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
        leagueSeason: '',
        teamColour: '#409EFF',
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

    ]),
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-create{

}
</style>
