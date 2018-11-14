<template>
  <div id="nav-menu">
    <div id="menu-container">
      <ul
        id="menu"
        v-if="showTabMenu"
        ref="tab-menu">
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

        <li
          v-if="loggedIn"
          :class="{'is-active': curRoute.includes('admin')}"
          @click="handleNavMenuSelect('admin')">
          <span>
            Admin
          </span>
        </li>
      </ul>

      <div
        v-else
        id="nav-menu-dropdown-container">
        <div class="nav-menu-dropdown">
          <div
            class="nav-menu-dropdown-button"
            @mouseover="navMenuDropdownButtonHover=true"
            @mouseleave="navMenuDropdownButtonHover=false"
            :class="{'lightGreyBackground': navMenuDropdownContentHover}">
            <span>{{ navMenuDropDownSelect }}</span>
            <font-awesome-icon class="caret-down" icon="caret-down" />
          </div>
          <div
            class="nav-menu-dropdown-content"
            :class="{'nav-menu-view-dropdown-content': navMenuDropdownVisible}"
            @mouseover="navMenuDropdownContentHover=true"
            @mouseleave="navMenuDropdownContentHover=false">
            <div
              @click="handleNavMenuSelect('news')"
              :class="{'boldText': curRoute === 'home'}">
              News
            </div>
            <div
              @click="handleNavMenuSelect('teams')"
              :class="{'boldText': curRoute === 'teams'}">
              Teams
            </div>
            <div
              @click="handleNavMenuSelect('standings')"
              :class="{'boldText': curRoute === 'standings'}">
              Standings
            </div>
            <div
              @click="handleNavMenuSelect('schedule')"
              :class="{'boldText': curRoute === 'schedule'}">
              Schedule
            </div>
            <div
              @click="handleNavMenuSelect('admin')"
              :class="{'boldText': curRoute.includes('admin')}">
              Admin
            </div>
          </div>
        </div>
      </div>

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
          <font-awesome-icon
            id="caret-down"
            icon="caret-down"/>
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
            Log Out <font-awesome-icon icon="sign-out-alt" />
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
      adminDropdownButtonHover: false,
      adminDropdownContentHover: false,
      navMenuDropdownButtonHover: false,
      navMenuDropdownContentHover: false,
      navMenuDropDownSelect: 'News',
      showTabMenu: window.innerWidth > 650,
    };
  },
  computed: {
    ...mapGetters([
      'user',
      'loggedIn',
    ]),
    curRoute() {
      return this.$route.name;
    },
    curRouteNameCap() {
      const name = this.curRoute;
      if (name === 'home') return 'News';
      return name.charAt(0).toUpperCase() + name.slice(1);
    },
    userDropdownVisible() {
      return this.userDropdownButtonHover || this.userDropdownContentHover;
    },
    adminDropdownVisible() {
      return this.adminDropdownButtonHover || this.adminDropdownContentHover;
    },
    navMenuDropdownVisible() {
      return this.navMenuDropdownButtonHover || this.navMenuDropdownContentHover;
    },
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
      'setCreateAccountModalVisible',
      'userLogOut',
    ]),
    handleResize() {
      this.showTabMenu = window.innerWidth > 650;
    },
    handleNavMenuSelect(key) {
      this.navMenuDropdownContentHover = false;
      switch (key) {
        case ('news'): {
          this.navMenuDropDownSelect = 'News';
          this.$router.push('/');
          break;
        }
        case ('teams'): {
          this.navMenuDropDownSelect = 'Teams';
          this.$router.push('/teams');
          break;
        }
        case ('schedule'): {
          this.navMenuDropDownSelect = 'Schedule';
          this.$router.push('/schedule');
          break;
        }
        case ('standings'): {
          this.navMenuDropDownSelect = 'Standings';
          this.$router.push('/standings');
          break;
        }
        case ('admin'): {
          this.navMenuDropDownSelect = 'Admin';
          this.$router.push('/admin/leagues');
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
          if (this.$route.name.includes('admin')) {
            this.$router.push('/');
          }
        });
      }).catch(() => {
      });
    },
  },
  mounted() {
    window.addEventListener('resize', this.handleResize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize);
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
  height: 44px;

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

      .admin-dropdown{
        .admin-dropdown-button{
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

        .admin-dropdown-content{
          /*display: none;*/
          opacity: 0;
          visibility: hidden;
          position: absolute;
          background-color: #f9f9f9;
          box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
          z-index: 10;
          border-radius: 0px 0px 6px 6px;
          transition: visibility 0s, opacity 0.2s linear;

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
        }

        .show-admin-dropdown-content{
          display: block;
        }
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

  #nav-menu-dropdown-container{
    display: flex;
    align-items: center;
    margin-left: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    transition: 0.3s;
    user-select: none;
    height: 100%;


    .nav-menu-dropdown{
      min-width: 128px;
      height: 100%;

      .nav-menu-dropdown-button{
        border: none;
        outline: none;
        color: $PRIMARY_TO_FADE;
        padding: 0px 20px;
        margin: 0;
        transition: 0.3s;
        height: 100%;
        display: flex;
        align-items: center;
        white-space: nowrap;

        .caret-down{
          margin-left: 4px;
        }

        &:hover{
          background-color: $HOVER_GREY;
          cursor: pointer;
        }
      }

      .nav-menu-dropdown-content{
        /*display: none;*/
        position: absolute;
        background-color: #f9f9f9;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 10;
        border-radius: 0px 0px 6px 6px;
        width: 128px;
        opacity: 0;
        visibility: hidden;
        transition: visibility 0s, opacity 0.2s linear;

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

        .boldText{
          font-weight: bold;
        }
      }

      .nav-menu-view-dropdown-content{
        /*display: block;*/
        opacity: 1;
        visibility: visible;
      }
    }
  }


  #user-dropdown-container{
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    transition: 0.3s;
    user-select: none;
    height: 100%;


    .user-dropdown{
      min-width: 160px;
      height: 100%;

      .user-dropdown-button{
        border: none;
        outline: none;
        color: $PRIMARY_TO_FADE;
        padding: 0px 20px;
        margin: 0;
        transition: 0.3s;
        height: 100%;
        display: flex;
        align-items: center;
        white-space: nowrap;

        #caret-down{
          margin-left: 4px;
        }

        &:hover{
          background-color: $HOVER_GREY;
          cursor: pointer;
        }
      }

      .user-dropdown-content{
        /*display: none;*/
        position: absolute;
        background-color: #f9f9f9;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 10;
        right: 20px;
        border-radius: 0px 0px 6px 6px;
        width: 160px;
        opacity: 0;
        visibility: hidden;
        transition: visibility 0s, opacity 0.2s linear;

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
        /*display: block;*/
        opacity: 1;
        visibility: visible;
      }
    }
  }

  #login-button-container{
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    transition: 0.3s;
    user-select: none;
    white-space: nowrap;

    &:hover{
      background-color: $HOVER_GREY;
      cursor: pointer;
    }

    #login-button-text{
      padding: 0px 20px;
      white-space: nowrap;
    }
  }
}
</style>
