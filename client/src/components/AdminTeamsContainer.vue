<template>
  <div id="admin-teams-container">
    <div id="title-container">
      <div id="title">
        Teams
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
  },
};

</script>

<style lang="scss" scoped>
#admin-teams-container{

}
</style>
