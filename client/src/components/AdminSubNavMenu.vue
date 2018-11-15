<template>
  <div id="admin-sub-nav-menu">
    <div id="admin-sub-menu-container">
      <ul id="admin-sub-menu">
        <li
          :class="{'is-active': curRoute.includes('admin-leagues')}"
          @click="handleAdminNavMenuSelect('leagues')">
          <span>
            Leagues
          </span>
        </li>
        <li
          :class="{'is-active': curRoute.includes('admin-teams')}"
          @click="handleAdminNavMenuSelect('teams')">
          <span>
            Teams
          </span>
        </li>
        <li
          :class="{'is-active': curRoute === 'admin-players'}"
          @click="handleAdminNavMenuSelect('players')">
          <span>
            Players
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

    ]),
    curRoute() {
      return this.$route.name;
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
