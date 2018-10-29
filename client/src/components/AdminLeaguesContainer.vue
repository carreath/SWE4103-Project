<template>
  <div id="admin-leagues-container">
    <div id="title-container">
    </div>
    <div
      id="create-league-button-container"
      @click="leagueCreateClicked">
      <el-button type="success">Create New League</el-button>
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
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    height: 61px;
    transition: 0.3s;
  }
}
</style>
