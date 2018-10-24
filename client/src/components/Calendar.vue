<template>
  <div id="calendar">
    {{  message }}
    <div class="calendar-parent">
      <calendar-view
        :events="events"
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
        :period-changed-callback="periodChanged"
        @drop-on-date="onDrop"
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
      events: [
        {
          id: 0,
          startDate: this.thisMonth(15, 18, 30),
          title: 'Single-day event with a long title',
        },
        {
          id: 1,
          startDate: this.thisMonth(20),
          title: 'My Birthday!',
          classes: 'birthday',
          url: 'https://en.wikipedia.org/wiki/Birthday',
        },
        {
          id: 2,
          startDate: this.thisMonth(5),
          title: 'Color event',
          classes: 'purple',
        },
        {
          id: 3,
          startDate: this.thisMonth(29),
          title: 'Same day 1',
        },
        {
          id: 4,
          startDate: '2018-10-24T11:00:00',
          title: 'GAME DAY',
        },
      ],
    };
  },
  computed: {
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
    // eslint-disable-next-line
    periodChanged(range, eventSource) {
      // Demo does nothing with this information, just including the method to
      // demonstrate how you can listen for changes to the displayed range and
      // react to them (by loading events, etc.)
      // console.log(eventSource);
      // console.log(range);
    },
    thisMonth(d, h, m) {
      const t = new Date();
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
    },
    onClickDay(d) {
      this.message = `You clicked: ${d.toLocaleDateString()}`;
    },
    onClickEvent(e) {
      console.log('EVENT: ', e);
      this.message = `You clicked: ${e.title}`;
    },
    setShowDate(d) {
      this.message = `Changing calendar view to ${d.toLocaleDateString()}`;
      this.showDate = d;
    },
    onDrop(event, date) {
      this.message = `You dropped ${event.id} on ${date.toLocaleDateString()}`;
      // Determine the delta between the old start date and the date chosen,
      // and apply that delta to both the start and end date to move the event.
      const eLength = this.dayDiff(event.startDate, date);
      event.originalEvent.startDate = this.addDays(event.startDate, eLength);
      event.originalEvent.endDate = this.addDays(event.endDate, eLength);
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
  mounted() {
    this.newEventStartDate = this.isoYearMonthDay(this.today());
    this.newEventEndDate = this.isoYearMonthDay(this.today());
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
    height: 100vh;

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
      text-overflow: ellipsis;
      font-size: 0.8rem;
    }

    .cv-event.purple {
      background-color: #f0e0ff;
      border-color: #e7d7f7;
    }

    .cv-event.orange {
      background-color: #ffe7d0;
      border-color: #f7e0c7;
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
