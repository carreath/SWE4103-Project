<template>
  <div id="nav-menu">
    <el-menu
      id="menu"
      class="el-menu-demo"
      mode="horizontal"
      menu-trigger="click"
      @select="handleNavMenuSelect"
      background-color="#fcfcfc"
      text-color="#2577db"
      active-text-color="#4b9dfc">
      <el-menu-item index="1">
        News
      </el-menu-item>
      <el-submenu index="2">
        <template slot="title">
          Teams
        </template>
        <el-menu-item index="2-1">
          item one
        </el-menu-item>
        <el-menu-item index="2-2">
          item two
        </el-menu-item>
        <el-menu-item index="2-3">
          item three
        </el-menu-item>
        <el-submenu index="2-4">
          <template slot="title">
            item four
          </template>
          <el-menu-item index="2-4-1">
            item one
          </el-menu-item>
          <el-menu-item index="2-4-2">
            item two
          </el-menu-item>
          <el-menu-item index="2-4-3">
            item three
          </el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="3">
        Schedule
      </el-menu-item>
      <el-menu-item
        index="4"
        :class="{'is-active': curRoute}">
        Standings
      </el-menu-item>
    </el-menu>

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
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
      'setCreateAccountModalVisible',
      'userLogOut',
      'setActiveNavIndex',
    ]),
    handleNavMenuSelect(key, keyPath) {
      this.setActiveNavIndex(key);
      switch (keyPath[0]) {
        case ('1'): {
          this.$router.push('/');
          break;
        }
        case ('2'): {
          this.$router.push('/teams');
          break;
        }
        case ('3'): {
          this.$router.push('/schedule');
          break;
        }
        case ('4'): {
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

<style lang="scss">
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
