<template>
  <div id="admin-sub-nav-menu">
    <div id="admin-sub-menu-container">
      <ul id="admin-sub-menu">
        <li>
          <span>
            Leagues
          </span>
        </li>
        <li>
          <span>
            Teams
          </span>
        </li>
        <li>
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
  },
  methods: {
    ...mapActions([

    ]),
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
  background-color: $HOVER_LIGHT_GREY;
  transition: 0.3s;

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
        padding: 10px 20px;
        user-select: none;
      }

    }
  }
}
</style>
