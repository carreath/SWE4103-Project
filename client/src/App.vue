<template>
  <div id="app">
    <ModalWrapper v-show='modalVisible'/>
    <UpcomingGamesHeader ref='upcoming-games-header'/>
    <MainHeader ref="main-header"/>
    <div
      id="nav-menu-wrapper"
      :class="{'sticky': nailNavMenu}">
      <NavMenu/>
      <AdminSubNavMenu v-if="curRoute.includes('admin')"/>
      <ScheduleSubNavMenu v-if="curRoute === 'schedule'"/>
    </div>
    <div
      id="router-view-outer-wrapper"
      class="router-view-outer-wrapper">
      <div id="router-view-inner-wrapper">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import MainHeader from './components/MainHeader.vue';
import ModalWrapper from './components/ModalWrapper.vue';
import UpcomingGamesHeader from './components/UpcomingGamesHeader.vue';
import NavMenu from './components/NavMenu.vue';
import AdminSubNavMenu from './components/AdminSubNavMenu.vue';
import ScheduleSubNavMenu from './components/ScheduleSubNavMenu.vue';

export default{
  name: 'App',
  components: {
    MainHeader,
    ModalWrapper,
    UpcomingGamesHeader,
    NavMenu,
    AdminSubNavMenu,
    ScheduleSubNavMenu,
  },
  data() {
    return {
      nailNavMenu: false,
    };
  },
  computed: {
    ...mapGetters([
      'modalVisible',
      'token',
    ]),
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([
      'setUser',
      'retrieveUserFromToken',
    ]),
    handleScroll() {
      const navbar = document.getElementById('nav-menu-wrapper');
      const outerRouterWrapper = document.getElementById('router-view-outer-wrapper');
      const sticky = navbar.offsetTop;
      if (!this.nailNavMenu && window.pageYOffset >= sticky) {
        this.nailNavMenu = true;
        outerRouterWrapper.style.paddingTop = `${navbar.clientHeight}px`;
      }
      const upcomingGamesHeaderHeight = this.$refs['upcoming-games-header'].$el.clientHeight;
      const mainHeaderHeight = this.$refs['main-header'].$el.clientHeight;
      const totalHeaderHeight = upcomingGamesHeaderHeight + mainHeaderHeight;
      if (this.nailNavMenu && (window.pageYOffset - totalHeaderHeight <= 0)) {
        this.nailNavMenu = false;
        outerRouterWrapper.style.paddingTop = '';
      }
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    if (this.token) {
      this.retrieveUserFromToken();
    }
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
};

</script>

<style lang="scss">
@import '@/style/global.scss';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 16px;

  .sticky {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 10;
  }

  .router-view-outer-wrapper{
    padding: 0px 20px;
    background-color: $SECONDARY_COLOR;

    #router-view-inner-wrapper{
      background-color: $SECONDARY_COLOR;
    }
  }
}

</style>
