<template>
  <div id="admin-leagues-create">
    <div id="title-container">
      <div id="title">
        Create League
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminLeaguesCreate',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'leagues',
    ]),
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([

    ]),
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-leagues-create{

}
</style>
