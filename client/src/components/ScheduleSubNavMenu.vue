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
                  @click="handleScheduleSelectedViewClick('Calendar')"
                  :class="{'boldText': scheduleSelectedView === 'Calendar'}">
                  Calendar
                </div>
                <div
                  @click="handleScheduleSelectedViewClick('Table')"
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
                <span v-if="!selectedTeamId">All Teams</span>
                <span v-else>{{ selectedTeam.teamName }}</span>
                <font-awesome-icon icon="caret-down" />
              </div>
              <div
                class="schedule-view-dropdown-content"
                :class="{'show-schedule-view-dropdown-content': scheduleTeamDropdownVisible}"
                @mouseover="scheduleTeamDropdownContentHover=true"
                @mouseleave="scheduleTeamDropdownContentHover=false">
                <div @click="handleTeamClick(null)">All Teams</div>
                <div
                  v-for="team in teamsByLeagueId(selectedLeagueId)"
                  :key="team.teamID"
                  @click="handleTeamClick(team.teamID)">
                  {{ team.teamName }}
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
      'teamsByLeagueId',
      'selectedLeagueId',
      'selectedTeam',
      'selectedTeamId',
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
      'setSelectedTeamId',
    ]),
    handleScheduleSelectedViewClick(view) {
      this.scheduleViewDropdownContentHover = false;
      this.setScheduleSelectedView(view);
    },
    handleTeamClick(teamID) {
      this.scheduleTeamDropdownContentHover = false;
      this.setSelectedTeamId(teamID);
    },
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
        width: 120px;

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

          span{
            margin-right: 4px;
          }
        }

        .schedule-view-dropdown-content{
          display: none;
          position: absolute;
          background-color: #f9f9f9;
          box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
          z-index: 10;
          border-radius: 0px 0px 6px 6px;
          width: 120px;

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
