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
      <div class="user-dropdown">
        <div
          class="user-dropdown-button"
          @mouseover="userDropdownButtonHover=true"
          @mouseleave="userDropdownButtonHover=false"
          :class="{'lightGreyBackground': userDropdownContentHover}">
          {{ user.first_name }} {{ user.last_name }}
          <font-awesome-icon icon="caret-down" />
        </div>
        <div
          class="user-dropdown-content"
          :class="{'show-user-dropdown-content': userDropdownVisible}"
          @mouseover="userDropdownContentHover=true"
          @mouseleave="userDropdownContentHover=false">
          <div>
            Change Password
          </div>
          <div @click="logoutClicked">
            Log Out
          </div>
        </div>
      </div>
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
  data() {
    return {
      userDropdownButtonHover: false,
      userDropdownContentHover: false,
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
    userDropdownVisible() {
      return this.userDropdownButtonHover || this.userDropdownContentHover;
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
    logoutClicked() {
      this.$confirm('Are you sure you want to log out?', 'Confirm Log Out', {
        confirmButtonText: 'Log Out',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.userLogOut().then(() => {
          this.$message({
            message: 'Logged Out',
            center: true,
          });
        });
      }).catch(() => {
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
  background-color: $SECONDARY_COLOR;

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
        user-select: none;
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
    user-select: none;


    .user-dropdown{

      .user-dropdown-button{
        border: none;
        outline: none;
        color: $PRIMARY_TO_FADE;
        padding: 20px 20px;
        margin: 0;
        transition: 0.3s;

        &:hover{
          background-color: $HOVER_GREY;
          cursor: pointer;
        }
      }

      .user-dropdown-content{
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        width: 156px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 10;
        right: 20px;

        div{
          float: none;
          color: $PRIMARY_TO_FADE;
          padding: 12px 16px;
          text-decoration: none;
          display: block;
          text-align: left;
          white-space:nowrap;
          font-weight: normal;
          transition: 0.3s;

          &:hover{
            background-color: $HOVER_GREY;
            cursor: pointer;
          }
        }

        :last-child{
          border-top: 1px solid $ELEMENT_UI_DEFAULT_BORDER;
          padding-top: 4px;
        }
      }

      .show-user-dropdown-content{
        display: block;
      }
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
    user-select: none;

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
