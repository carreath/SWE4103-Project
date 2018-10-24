<template>
  <div id="calendar">
    <div class="calendar-parent">
      <calendar-view
        :events="events"
        :show-date="showDate"
        :time-format-options="{hour: 'numeric', minute:'2-digit'}"
        :enable-drag-drop="true"
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
// For testing against the published version
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
      /* Show the current month, and give it some fake events to show */
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
      useDefaultTheme: true,
      useHolidayTheme: true,
      events: [
        {
          id: 'e0',
          startDate: this.thisMonth(15),
          title: 'Single-day event with a long title',
        },
        {
          id: 'e1',
          startDate: this.thisMonth(7, 9, 25),
          endDate: this.thisMonth(10, 16, 30),
          title: 'Multi-day event with a long title and times',
        },
        {
          id: 'e2',
          startDate: this.thisMonth(20),
          title: 'My Birthday!',
          classes: 'birthday',
          url: 'https://en.wikipedia.org/wiki/Birthday',
        },
        {
          id: 'e3',
          startDate: this.thisMonth(5),
          endDate: this.thisMonth(12),
          title: 'Multi-day event',
          classes: 'purple',
        },
        {
          id: 'foo',
          startDate: this.thisMonth(29),
          title: 'Same day 1',
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
    periodChanged(range, eventSource) {
      // Demo does nothing with this information, just including the method to
      // demonstrate how you can listen for changes to the displayed range and
      // react to them (by loading events, etc.)
      console.log(eventSource);
      console.log(range);
    },
    thisMonth(d, h, m) {
      const t = new Date();
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
    },
    onClickDay(d) {
      this.message = `You clicked: ${d.toLocaleDateString()}`;
    },
    onClickEvent(e) {
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

<style lang="scss" scoped>
#calendar{

  .calendar-parent {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    overflow-x: hidden;
    overflow-y: hidden;
    max-height: 80vh;
    background-color: white;
  }
}
</style>
