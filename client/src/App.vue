<template>
  <div id="app">
    <ModalWrapper v-show='modalVisible'/>
    <UpcomingGamesHeader ref='upcoming-games-header' v-if="false"/>
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
      'getAllData',
    ]),
    handleScroll() {
      const navbar = document.getElementById('nav-menu-wrapper');
      const outerRouterWrapper = document.getElementById('router-view-outer-wrapper');
      const sticky = navbar.offsetTop;
      if (!this.nailNavMenu && window.pageYOffset >= sticky) {
        this.nailNavMenu = true;
        outerRouterWrapper.style.paddingTop = `${navbar.clientHeight}px`;
      }

      const upcomingGamesHeaderHeight = this.$refs['upcoming-games-header'] ?
        this.$refs['upcoming-games-header'].$el.clientHeight :
        0;
      const mainHeaderHeight = this.$refs['main-header'] ?
        this.$refs['main-header'].$el.clientHeight :
        0;
      const totalHeaderHeight = upcomingGamesHeaderHeight + mainHeaderHeight;
      if (this.nailNavMenu && (window.pageYOffset - totalHeaderHeight <= 0)) {
        this.nailNavMenu = false;
        outerRouterWrapper.style.paddingTop = '';
      }
    },
  },
  watch: {
    modalVisible(val) {
      if (val) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = 'auto';
      }
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    if (this.token) {
      this.retrieveUserFromToken();
    }
    document.body.style.overflow = 'auto';
    this.getAllData();
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
    padding: 0px 0px;
    background-color: $SECONDARY_COLOR;

    #router-view-inner-wrapper{
      background-color: $SECONDARY_COLOR;
    }
  }
}

.no-scroll{
  overflow: hidden;
}

</style>
