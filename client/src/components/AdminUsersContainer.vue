<template>
  <div id="admin-users-container">
    <div id="title-container">
    </div>
    <div id="users-table-container">
      <el-table
        :data="formatUsers"
        stripe
        style="">
        <el-table-column
          width="100px"
          prop="userID"
          label="User ID">
        </el-table-column>
        <el-table-column
          prop="firstName"
          label="First Name">
        </el-table-column>
        <el-table-column
          prop="lastName"
          label="Last Name">
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
  name: 'AdminUsersContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
    ]),
    formatUsers() {
      const formatedUsers = [].map(() => {
        return {
        };
      });
      return formatedUsers;
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
#admin-users-container{
  #create-users-button-container{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    height: 61px;
    transition: 0.3s;
  }
}
</style>
