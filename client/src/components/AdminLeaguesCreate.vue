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
        ref="league-create-form">
        <el-form-item prop="leagueName">
          <el-input
            id="league-name-input"
            type="leagueName"
            placeholder="League Name"
            v-model="leagueCreateForm.leagueName"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <el-form-item prop="season">
          <el-input
            id="season-input"
            type="season"
            placeholder="Season"
            v-model="leagueCreateForm.season"
            :disabled="loading">
          </el-input>
        </el-form-item>
        <div id="errMsg" v-if="errMsg">
          Error: {{ errMsg }}
        </div>
        <el-form-item id="league-create-button-container">
          <el-button
            type="primary"
            :loading="loading"
            @click="leagueCreateButtonClicked">
            {{ leagueCreateButtonText }}
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
      },
      loading: false,
      errMsg: null,
    };
  },
  computed: {
    leagueCreateButtonText() {
      return this.loading ? 'Loading' : 'Create League';
    },
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([
        'createLeague',
    ]),
    leagueCreateButtonClicked() {
      this.displayErrMsg = false;
      this.$refs['league-create-form'].validate((valid) => {
        if (valid) {
          this.loading = true;
          this.createLeague(this.leagueCreateForm).then((response) => {
            this.loading = false;
            if (response.retVal) {
              this.errMsg = null;
              this.$router.push('/admin/leagues');
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
#admin-leagues-create{

}
</style>
