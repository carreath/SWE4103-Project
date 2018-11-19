<template>
  <div id="admin-users-container">
    <div id="title-container">
      <span id="usersNameSearch">
        <el-input
          v-model="searchName"
          size="small"
          placeholder="Filter Name"/>
      </span>
    </div>
    <div id="users-table-container">
      <el-table
        :data="formatUsers"
        stripe
        style="">
        <el-table-column
          width="100px"
          prop="userID"
          label="User ID"
          sortable>
        </el-table-column>
        <el-table-column
          prop="firstName"
          label="First Name"
          sortable>
        </el-table-column>
        <el-table-column
          prop="lastName"
          label="Last Name"
          sortable>
        </el-table-column>
        <el-table-column
          prop="email"
          label="Email"
          sortable>
        </el-table-column>
        <el-table-column
          prop="userType"
          label="User Type"
          sortable>
        </el-table-column>
        <el-table-column
          label="Action">
          <template slot-scope="scope">
            <el-button
            icon="el-icon-edit"
            size="mini"
            @click='userEditClicked(scope.row)'>
            </el-button>
            <el-button
            icon="el-icon-delete"
            size="mini"
            @click="userDeleteClicked(scope.row.id, scope.row.name)">
            </el-button>
          </template>
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
      searchName: '',
    };
  },
  computed: {
    ...mapGetters([
      'users',
    ]),
    formatUsers() {
      return (this.users || []).filter(userObj => {
        if (!this.searchName) {
          return true;
        }
        const fullName = `${userObj.firstName.toLowerCase()} ${userObj.lastName.toLowerCase()}`;
        return fullName.includes(this.searchName.toLowerCase());
      });
    },
  },
  methods: {
    ...mapActions([
      'setEditedUser',
      'setEditUserModalVisible',
    ]),
    userEditClicked(userObj) {
      this.setEditedUser(userObj.userID);
      this.setEditUserModalVisible(true);
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-users-container{

  #title-container{
    margin-top: 8px;
    width: 100%;
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;

    #usersNameSearch{
      width: 25%;
      min-width: 150px;
    }
  }

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
