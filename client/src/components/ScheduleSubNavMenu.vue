<template>
  <div id="schedule-sub-nav-menu">
    <div id="schedule-sub-menu-container">
      <ul id="schedule-sub-menu">
        <li>

          <div
            id="schedule-view-dropdown-container">
            <div class="schedule-view-dropdown">
              <div
                class="schedule-view-dropdown-button"
                @mouseover="scheduleViewDropdownButtonHover=true"
                @mouseleave="scheduleViewDropdownButtonHover=false"
                :class="{'lightGreyBackground': scheduleViewDropdownContentHover}">
                {{ scheduleSelectedView }}
                <font-awesome-icon icon="caret-down" />
              </div>
              <div
                class="schedule-view-dropdown-content"
                :class="{'show-schedule-view-dropdown-content': scheduleViewDropdownVisible}"
                @mouseover="scheduleViewDropdownContentHover=true"
                @mouseleave="scheduleViewDropdownContentHover=false">
                <div
                  @click="setScheduleSelectedView('Calendar')"
                  :class="{'boldText': scheduleSelectedView === 'Calendar'}">
                  Calendar
                </div>
                <div
                  @click="setScheduleSelectedView('Table')"
                  :class="{'boldText': scheduleSelectedView === 'Table'}">
                  Table
                </div>
              </div>
            </div>
          </div>

        </li>
        <li>

          <div
            id="schedule-team-dropdown-container">
            <div class="schedule-view-dropdown">
              <div
                class="schedule-view-dropdown-button"
                @mouseover="scheduleTeamDropdownButtonHover=true"
                @mouseleave="scheduleTeamDropdownButtonHover=false"
                :class="{'lightGreyBackground': scheduleTeamDropdownContentHover}">
                All Teams
                <font-awesome-icon icon="caret-down" />
              </div>
              <div
                class="schedule-view-dropdown-content"
                :class="{'show-schedule-view-dropdown-content': scheduleTeamDropdownVisible}"
                @mouseover="scheduleTeamDropdownContentHover=true"
                @mouseleave="scheduleTeamDropdownContentHover=false">
                <div>
                  Team A
                </div>
                <div>
                  Team B
                </div>
              </div>
            </div>
          </div>

        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ScheduleSubNavMenu',
  data() {
    return {
      scheduleViewDropdownButtonHover: false,
      scheduleViewDropdownContentHover: false,
      scheduleTeamDropdownButtonHover: false,
      scheduleTeamDropdownContentHover: false,
    };
  },
  computed: {
    ...mapGetters([
      'scheduleSelectedView',
    ]),
    curRoute() {
      return this.$route.name;
    },
    scheduleViewDropdownVisible() {
      return this.scheduleViewDropdownButtonHover || this.scheduleViewDropdownContentHover;
    },
    scheduleTeamDropdownVisible() {
      return this.scheduleTeamDropdownButtonHover || this.scheduleTeamDropdownContentHover;
    },
  },
  methods: {
    ...mapActions([
      'setScheduleSelectedView',
    ]),
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#schedule-sub-nav-menu{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  border-bottom: 1px solid $HOVER_GREY;
  background-color: $VERY_LIGHT_GREY;
  transition: 0.3s;
  font-size: 0.9rem;

  #schedule-sub-menu{
    padding: 0px 20px;
    font-weight: bold;
    display: flex;
    list-style-type: none;
    margin: 0;
    height: 100%;

    #schedule-view-dropdown-container,
    #schedule-team-dropdown-container{
      display: flex;
      align-items: center;
      color: $PRIMARY_TO_FADE;
      transition: 0.3s;
      user-select: none;


      .schedule-view-dropdown{
        .schedule-view-dropdown-button{
          border: none;
          outline: none;
          color: $PRIMARY_TO_FADE;
          padding: 10px 20px;
          margin: 0;
          transition: 0.3s;

          &:hover{
            background-color: $HOVER_GREY;
            cursor: pointer;
          }
        }

        .schedule-view-dropdown-content{
          display: none;
          position: absolute;
          background-color: #f9f9f9;
          box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
          z-index: 10;
          border-radius: 0px 0px 6px 6px;
          width: 114px;

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

        .show-schedule-view-dropdown-content{
          display: block;
        }
      }
    }

  }
}
</style>
