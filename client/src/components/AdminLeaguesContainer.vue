<template>
  <div id="admin-leagues-container">
    <div id="title-container">
      <div id="title">
        Leagues
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
  },
  methods: {
    ...mapActions([

    ]),
  },
};

</script>

<style lang="scss" scoped>
#admin-leagues-container{

}
</style>
