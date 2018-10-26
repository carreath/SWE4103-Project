<template>
  <div id="calendar">
    <div class="calendar-parent">
      <calendar-view
        :events="displayedGameObjects"
        :show-date="showDate"
        :time-format-options="{hour: 'numeric', minute:'2-digit'}"
        :enable-drag-drop="false"
        :disable-past="disablePast"
        :disable-future="disableFuture"
        :show-event-times="showEventTimes"
        :display-period-uom="displayPeriodUom"
        :display-period-count="displayPeriodCount"
        :starting-day-of-week="startingDayOfWeek"
        :class="themeClasses"
        :eventContentHeight="eventContentHeight"
        @click-date="onClickDay"
        @click-event="onClickEvent">
        <calendar-view-header
          slot="header"
          slot-scope="{ headerProps }"
          :header-props="headerProps"
          @input="setShowDate" />
      </calendar-view>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import {
  CalendarView,
  CalendarViewHeader,
  CalendarMathMixin,
} from 'vue-simple-calendar';

require('vue-simple-calendar/static/css/default.css');
require('vue-simple-calendar/static/css/holidays-us.css');

export default {
  name: 'Calendar',
  components: {
    CalendarView,
    CalendarViewHeader,
  },
  mixins: [CalendarMathMixin],
  data() {
    return {
      showDate: this.thisMonth(1),
      message: '',
      startingDayOfWeek: 0,
      disablePast: false,
      disableFuture: false,
      displayPeriodUom: 'month',
      displayPeriodCount: 1,
      showEventTimes: true,
      newEventTitle: '',
      newEventStartDate: '',
      newEventEndDate: '',
      useDefaultTheme: false,
      useHolidayTheme: true,
      eventContentHeight: '2.2em',
      selectedLeague: 1,
      displayedGameObjects: [],
    };
  },
  computed: {
    ...mapGetters([
      'gamesByLeagueId',
      'selectedLeagueId',
      'selectedGameId',
      'teamById',
      'gamesByTeamId',
      'selectedTeamId',
    ]),
    userLocale() {
      return this.getDefaultBrowserLocale;
    },
    dayNames() {
      return this.getFormattedWeekdayNames(this.userLocale, 'long', 0);
    },
    themeClasses() {
      return {
        'theme-default': this.useDefaultTheme,
        'holiday-us-traditional': this.useHolidayTheme,
        'holiday-us-official': this.useHolidayTheme,
      };
    },
  },
  methods: {
    ...mapActions([
      'setSelectedGameId',
    ]),
    generateGameObjs() {
      const selectedames = this.selectedTeamId ?
        this.gamesByTeamId(this.selectedTeamId) :
        this.gamesByLeagueId(this.selectedLeagueId);
      const leagueGamesForCalendar = selectedames.map((gameObj) => {
        let gameObjForCalendar = {
          id: gameObj.gameID,
          startDate: `${gameObj.date}T${gameObj.time}`,
          title: `${gameObj.field} - ${this.teamById(gameObj.awayTeamID).teamName} vs. ${this.teamById(gameObj.homeTeamID).teamName}`,
        };
        if (gameObj.status === 'Cancelled') {
          gameObjForCalendar.classes = 'cancelled-event';
        }
        if (this.selectedGameId === gameObj.gameID) {
          gameObjForCalendar.classes = 'selected-event';
        }
        return gameObjForCalendar;
      });
      this.displayedGameObjects = leagueGamesForCalendar;
    },
    thisMonth(d, h, m) {
      const t = new Date();
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
    },
    onClickDay(d) {
      // console.log('DATE CLICKED: ', d);
      this.message = `You clicked: ${d.toLocaleDateString()}`;
    },
    onClickEvent(e) {
      // console.log('EVENT: ', e.id);
      // this.message = `You clicked: ${e.title}`;
      this.setSelectedGameId(e.id);
    },
    setShowDate(d) {
      this.message = `Changing calendar view to ${d.toLocaleDateString()}`;
      this.showDate = d;
    },
    clickTestAddEvent() {
      this.events.push({
        startDate: this.newEventStartDate,
        endDate: this.newEventEndDate,
        title: this.newEventTitle,
      });
      this.message = 'You added an event!';
    },
  },
  watch: {
    selectedGameId() {
      this.generateGameObjs();
    },
    selectedTeamId() {
      this.generateGameObjs();
    },
  },
  mounted() {
    this.newEventStartDate = this.isoYearMonthDay(this.today());
    this.newEventEndDate = this.isoYearMonthDay(this.today());
    this.generateGameObjs();
  },
};
</script>

<style lang="scss">
@import '@/style/global.scss';

#calendar{
  display: flex;
  flex-direction: column;
  width: 100%;

  .calendar-parent {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    overflow-x: hidden;
    overflow-y: hidden;
    background-color: $SECONDARY_COLOR;
    height: 80vh;
    min-height: 550px;

    /* Header */
    .cv-header,
    .cv-header-day {
      background-color: #f7f7f7;
    }

    .cv-header .periodLabel {
      font-size: 1.5rem;
    }

    .cv-header button {
      color: #7f7f7f;
      margin: 0px 4px;
    }

    .cv-header button:disabled {
      color: #ccc;
      background-color: #f7f7f7;
    }

    .cv-header .cv-header-nav .previousYear,
    .cv-header .cv-header-nav .nextYear{
      display: none;
    }

    /* Grid */
    .cv-day.today {
      background-color: #ffe;
    }

    .cv-day.past {
      background-color: #fafafa;
    }

    .cv-day.outsideOfMonth {
      background-color: #f7f7f7;
    }

    /* Events */
    .cv-event {
      border-color: #e0e0f0;
      border-radius: 0.5em;
      background-color: #2577db;
      color: #fcfcfc;
      white-space: normal;
      font-size: 0.8rem;
      text-align: left;
      line-height: 1em;
      height: 2.3em;
      text-overflow: ellipsis;

      &:hover{
        cursor: pointer;
      }
    }

    .cv-event.cancelled-event{
      background: $CANCELLED_RED;
      color: $SECONDARY_COLOR;
      transition: 0.2s;

      span{
        color: $SECONDARY_COLOR;
        transition: 0.2s;
      }
    }

    .cv-event.selected-event{
      background: #d8eaff;
      color: $PRIMARY_COLOR;
      transition: 0.2s;

      span{
        color: $PRIMARY_COLOR;
        transition: 0.2s;
      }
    }

    .cv-event.continued::before,
    .cv-event.toBeContinued::after {
      content: " \21e2 ";
      color: #999;
    }

    .cv-event.toBeContinued {
      border-right-style: none;
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
    }

    .cv-event.isHovered.hasUrl {
      text-decoration: underline;
    }

    .cv-event.continued {
      border-left-style: none;
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
    }

    /* Event Times */
    .cv-event .startTime,
    .cv-event .endTime {
      font-weight: bold;
      color: #fcfcfc;
    }

    /* Drag and drop */
    .cv-day.draghover {
      box-shadow: inset 0 0 0.2em 0.2em yellow;
    }
  }
}
</style>
