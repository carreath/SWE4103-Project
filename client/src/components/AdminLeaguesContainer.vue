<template>
  <div id="admin-leagues-container">
    <div id="title-container">
      <div id="title">
        Leagues
      </div>
    </div>
    <div
      id="create-league-button-container"
      @click="leagueCreateClicked">
      <div id="create-league-button-text">
        Create New League
      </div>
    </div>
    <div id="leagues-table-container">
      <el-table
        :data="leagues"
        stripe
        style="width: 100%">
        <el-table-column
          prop="id"
          label="League Id">
        </el-table-column>
        <el-table-column
          prop="name"
          label="League Name">
        </el-table-column>
        <el-table-column
          prop="season"
          label="League Season">
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
  name: 'AdminLeaguesContainer',
  data() {
    return {

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
    leagueCreateClicked() {
      this.$router.push('/admin/leagues/create');
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-leagues-container{

  #create-league-button-container{
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

    #create-league-button-text{
      padding: 0px 20px;
    }
  }
}
</style>
