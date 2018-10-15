<template>
  <div id="nav-menu">
    <el-menu
      id="menu"
      class="el-menu-demo"
      mode="horizontal"
      menu-trigger="click"
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
      <el-menu-item index="4">
        Standings
      </el-menu-item>
    </el-menu>

    <div
      id="user-dropdown-container"
      v-if="loggedIn">
      <el-dropdown
        trigger="click"
        @command="handleUserDropdownClick">
        <span
          id="user-dropdown-user-text"
          class="el-dropdown-link">
          {{ user.first_name }} {{ user.last_name }}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>Action 1</el-dropdown-item>
          <el-dropdown-item>Action 2</el-dropdown-item>
          <el-dropdown-item>Action 3</el-dropdown-item>
          <el-dropdown-item divided @command="logoutClicked">Log Out</el-dropdown-item>
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
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'NavMenu',
  computed: {
    ...mapGetters([
      'user',
      'loggedIn',
    ]),
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
      'setCreateAccountModalVisible',
      'userLogOut',
    ]),
    handleUserDropdownClick(e) {
      // TODO Fix this
      console.log(e);
    },
    logoutClicked() {
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

    /* TODO Commented code */
    /*
    li:nth-last-child(-n+1) {
      float: right;
    }
    */
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
