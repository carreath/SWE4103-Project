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
          width="70px"
          prop="userID"
          label="ID"
          sortable>
        </el-table-column>
        <el-table-column
          prop="fullName"
          label="Name"
          :show-overflow-tooltip="true"
          sortable>
        </el-table-column>
        <el-table-column
          prop="email"
          label="Email"
          :show-overflow-tooltip="true"
          sortable>
        </el-table-column>
        <el-table-column
          prop="userTypeWithName"
          label="User Type"
          :show-overflow-tooltip="true"
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
            :disabled="scope.row.userID === (user || {}).userID"
            @click="userDeleteClicked(scope.row)">
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
      'user',
      'leagues',
      'teams',
    ]),
    formatUsers() {
      return (this.users || []).filter(userObj => {
        if (!this.searchName) {
          return true;
        }
        const fullName = `${userObj.firstName.toLowerCase()} ${userObj.lastName.toLowerCase()}`;
        return fullName.includes(this.searchName.toLowerCase());
      }).map((userObj) => {
        const newObj = { ...userObj };
        newObj.fullName = `${userObj.firstName} ${userObj.lastName}`;
        switch (newObj.userType) {
          case 'Coordinator': {
            const league = this.leagues.find(league => league.managerID === newObj.userID);
            newObj.userTypeWithName = league ?
              `${newObj.userType} - ${league.leagueName}` :
              `${newObj.userType} - None`;
            break;
          }
          case 'Manager': {
            const team = this.teams.find(team => team.managerID === newObj.userID);
            newObj.userTypeWithName = team ?
              `${newObj.userType} - ${team.teamName}` :
              `${newObj.userType} - None`;
            break;
          }
          default:
            newObj.userTypeWithName = newObj.userType;
        }
        return newObj;
      });
    },
  },
  methods: {
    ...mapActions([
      'setEditedUser',
      'setEditUserModalVisible',
      'deleteUser',
    ]),
    userEditClicked(userObj) {
      this.setEditedUser(userObj.userID);
      this.setEditUserModalVisible(true);
    },
    userDeleteClicked(userObj) {
      const name = `${userObj.firstName} ${userObj.lastName}`;
      this.$confirm(`Are you sure you want to delete ${name}?`, 'Confirm User Deletion', {
        confirmButtonText: 'Delete User',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.deleteUser(userObj).then(() => {
          this.$message({
            message: `Deleted ${name}`,
            center: true,
          });
          this.$router.push('/admin/users');
        });
      }).catch(() => {
      });
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
