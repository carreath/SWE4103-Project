<template>
  <div id="nav-menu">
    <div id="menu-container">
      <ul id="menu">
        <li
          :class="{'is-active': curRoute === 'home'}"
          @click="handleNavMenuSelect('news')">
          <span>
            News
          </span>
        </li>
        <li
          :class="{'is-active': curRoute === 'teams'}"
          @click="handleNavMenuSelect('teams')">
          <span>
            Teams
          </span>
        </li>
        <li
          :class="{'is-active': curRoute === 'schedule'}"
          @click="handleNavMenuSelect('schedule')">
          <span>
            Schedule
          </span>
        </li>
        <li
          :class="{'is-active': curRoute === 'standings'}"
          @click="handleNavMenuSelect('standings')">
          <span>
            Standings
          </span>
        </li>
      </ul>
    </div>

    <div
      id="user-dropdown-container"
      v-if="loggedIn">
      <el-dropdown
        trigger="click"
        @command="handleUserDropdownClick"
        placement="bottom-end">
        <span
          id="user-dropdown-user-text"
          class="el-dropdown-link">
          {{ user.first_name }} {{ user.last_name }}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>
            Change Password
          </el-dropdown-item>
          <el-dropdown-item>
            Add Game Scores
          </el-dropdown-item>
          <el-dropdown-item>
            Admin
          </el-dropdown-item>
          <el-dropdown-item
            id="user-dropdown-option-logout"
            divided
            command="logout">
            Log Out
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>

    <div
      id="login-button-container"
      @click='setLoginModalVisible(true)'
      v-else>
      <div id="login-button-text">
        Log In
      </div>
    </div>

    <el-dialog
      title="Confirm Logout"
      :visible.sync="logoutDialogVisible"
      width="30%">
      <span>Are you sure you want to log out?</span>
      <span
        slot="footer"
        class="dialog-footer">
        <el-button @click="logoutDialogVisible=false">
          Cancel
        </el-button>
        <el-button
          type="primary"
          @click="logoutClicked">
          Confirm
        </el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'NavMenu',
  data() {
    return {
      logoutDialogVisible: false,
    };
  },
  computed: {
    ...mapGetters([
      'user',
      'loggedIn',
      'activeNavIndex',
    ]),
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
      'setCreateAccountModalVisible',
      'userLogOut',
      'setActiveNavIndex',
    ]),
    handleNavMenuSelect(key) {
      switch (key) {
        case ('news'): {
          this.$router.push('/');
          break;
        }
        case ('teams'): {
          this.$router.push('/teams');
          break;
        }
        case ('schedule'): {
          this.$router.push('/schedule');
          break;
        }
        case ('standings'): {
          this.$router.push('/standings');
          break;
        }
        default: {
          break;
        }
      }
    },
    handleUserDropdownClick(command) {
      // TODO remember to set the active nav index to null for the appropriate
      // commands here
      switch (command) {
        case ('logout'): {
          this.logoutDialogVisible = true;
          break;
        }
        default: {
          break;
        }
      }
    },
    logoutClicked() {
      this.logoutDialogVisible = false;
      this.userLogOut().then(() => {
        this.$message({
          message: 'Logged Out',
          center: true,
        });
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#nav-menu{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  border-bottom: 1px solid $HOVER_GREY;

  #menu{
    padding: 0px 20px;
    font-weight: bold;
    display: flex;
    list-style-type: none;
    margin: 0;
    height: 100%;

    li{
      display: flex;
      align-items: center;
      font-weight: bold;
      color: $PRIMARY_TO_FADE;
      transition: 0.3s;

      &:hover{
        background-color: $HOVER_GREY;
        cursor: pointer;
      }

      span{
        padding: 0px 20px;
      }
    }

    .is-active{
      transition: 0.3s;
      border-bottom: 2px solid $PRIMARY_TO_FADE;

      span{
        margin-bottom: -2px;
        transition: 0.3s;
      }
    }
  }

  #user-dropdown-container{
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    height: 61px;
    transition: 0.3s;

    &:hover{
      background-color: $HOVER_GREY;
      cursor: pointer;
    }

    #user-dropdown-user-text{
      color: $PRIMARY_TO_FADE;
      padding: 20px 20px;
    }
  }

  #login-button-container{
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    height: 61px;
    transition: 0.3s;

    &:hover{
      background-color: $HOVER_GREY;
      cursor: pointer;
    }

    #login-button-text{
      padding: 0px 20px;
    }
  }
}
</style>
