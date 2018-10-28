<template>
  <div id="admin-leagues-create">
    <div id="title-container">
      <div id="title">
        Create League
      </div>
    </div>
    <el-form
        :model="leagueCreateForm"
        :rules="leagueCreateFormRules"
        ref="login-form">
        <el-form-item prop="leagueName">
          <el-input
            id="league-name-input"
            type="leagueName"
            placeholder="League Name"
            v-model="leagueCreateForm.leagueName"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            id="password-input"
            type="password"
            placeholder="Password"
            prefix-icon="el-icon-tickets"
            v-model="leagueCreateForm.password"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <div id="errMsg" v-if="errMsg">
          Error: {{ errMsg }}
        </div>
        <el-form-item id="login-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="loginButtonClicked">
            {{ loginButtonText }}
          </el-button>
        </el-form-item>
      </el-form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminLeaguesCreate',
  data() {
    return {
      leagueCreateForm: {
        leagueName: '',
        leagueSeason: '',
      },
      leagueCreateFormRules: {
        email: [
          {
            required: true,
            message: 'Please input email',
            trigger: 'blur',
          },
          {
            min: 1,
            max: 64,
            message: 'Input too long',
            trigger: 'blur',
          },
        ],
        password: [
          {
            required: true,
            message: 'Please input password',
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
      'leagues',
    ]),
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
#admin-leagues-create{

}
</style>
