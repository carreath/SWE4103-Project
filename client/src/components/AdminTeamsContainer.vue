<template>
  <div id="admin-teams-container">
    <div id="title-container">
      <div id="title">
        Teams
      </div>
    </div>
    <div
      id="create-team-button-container"
      @click="teamCreateClicked">
      <div id="create-team-button-text">
        Create New Team
      </div>
    </div>
    <div id="teams-table-container">
      <el-table
        :data="teams"
        stripe
        style="width: 100%">
        <el-table-column
          prop="teamID"
          label="Team ID">
        </el-table-column>
        <el-table-column
          prop="teamName"
          label="Team Name">
        </el-table-column>
        <el-table-column
          prop="leagueID"
          label="League ID">
        </el-table-column>
        <el-table-column
          prop="managerID"
          label="Manager ID">
        </el-table-column>
        <el-table-column
          label="Action">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminTeamsContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'teams',
    ]),
  },
  methods: {
    ...mapActions([

    ]),
    teamCreateClicked() {
      this.$router.push('/admin/teams/create');
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-teams-container{
  #create-team-button-container{
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    height: 61px;
    transition: 0.3s;
    user-select: none;
    width: 10vw;
    background-color: $VERY_LIGHT_GREY;

    &:hover{
      background-color: $HOVER_GREY;
      cursor: pointer;
    }

    #create-team-button-text{
      padding: 0px 20px;
    }
  }
}
</style>
