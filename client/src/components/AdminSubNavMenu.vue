<template>
  <div id="admin-sub-nav-menu">
    <div id="admin-sub-menu-container">
      <ul id="admin-sub-menu">
        <li
          v-if="showLeaguesTab"
          :class="{'is-active': curRoute.includes('admin-leagues')}"
          @click="handleAdminNavMenuSelect('leagues')">
          <span>
            Leagues
          </span>
        </li>
        <li
          v-if="showTeamsTab"
          :class="{'is-active': curRoute.includes('admin-teams')}"
          @click="handleAdminNavMenuSelect('teams')">
          <span>
            Teams
          </span>
        </li>
        <li
          v-if="showPlayersTab"
          :class="{'is-active': curRoute.includes('admin-players')}"
          @click="handleAdminNavMenuSelect('players')">
          <span>
            Players
          </span>
        </li>
        <li
          v-if="showUsersTab"
          :class="{'is-active': curRoute === 'admin-users'}"
          @click="handleAdminNavMenuSelect('users')">
          <span>
            Users
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminSubNavMenu',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'user',
    ]),
    curRoute() {
      return this.$route.name || '';
    },
    showLeaguesTab() {
      if (!this.user) {
        return false;
      }
      return this.user.userType === 'Admin'
        || this.user.userType === 'Coordinator';
    },
    showTeamsTab() {
      if (!this.user) {
        return false;
      }
      return this.user.userType === 'Admin'
        || this.user.userType === 'Coordinator'
        || this.user.userType === 'Manager';
    },
    showPlayersTab() {
      if (!this.user) {
        return false;
      }
      return this.user.userType === 'Admin'
        || this.user.userType === 'Coordinator'
        || this.user.userType === 'Manager';
    },
    showUsersTab() {
      if (!this.user) {
        return false;
      }
      return this.user.userType === 'Admin';
    },
  },
  methods: {
    ...mapActions([

    ]),
    handleAdminNavMenuSelect(key) {
      switch (key) {
        case ('leagues'): {
          this.$router.push('/admin/leagues');
          break;
        }
        case ('teams'): {
          this.$router.push('/admin/teams');
          break;
        }
        case ('players'): {
          this.$router.push('/admin/players');
          break;
        }
        case ('users'): {
          this.$router.push('/admin/users');
          break;
        }
        default: {
          break;
        }
      }
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#admin-sub-nav-menu{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  border-bottom: 1px solid $HOVER_GREY;
  background-color: $VERY_LIGHT_GREY;
  transition: 0.3s;
  font-size: 0.9rem;
  min-height: 36px;

  #admin-sub-menu{
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
}
</style>
