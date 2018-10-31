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

        <li
          v-if="loggedIn"
          :class="{'is-active': curRoute.includes('admin')}"
          @click="handleNavMenuSelect('admin')">
          <span>
            Admin
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
    userDropdownVisible() {
      return this.userDropdownButtonHover || this.userDropdownContentHover;
    },
    adminDropdownVisible() {
      return this.adminDropdownButtonHover || this.adminDropdownContentHover;
    },
  },
  methods: {
    ...mapActions([
      'setLoginModalVisible',
      'setCreateAccountModalVisible',
      'userLogOut',
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
        case ('admin'): {
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

  #user-dropdown-container{
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-weight: bold;
    color: $PRIMARY_TO_FADE;
    transition: 0.3s;
    user-select: none;


    .user-dropdown{
      width: 160px;

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
