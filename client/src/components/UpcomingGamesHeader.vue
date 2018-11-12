<template>
  <div
    id="upcoming-games-header"
    ref="upcoming-games-header">
    <div
      id="left-arrow-icon-container"
      @click="scrollLeft">
      <i class="el-icon-arrow-left"></i>
    </div>
    <div
      id="upcoming-games-header-scroll-container"
      ref="upcoming-games-header-scroll-container">
      <div
        id="prev-day-games-container"
        ref="prev-day-games-container">
        <div class="date-container">
          {{ tempYesterdaysGames.date }}
        </div>
        <PreviousGameCard
          v-for="gameObj in tempYesterdaysGames.games"
          :key="gameObj.id"
          :game="gameObj"/>
      </div>
      <div
        id="day-game-container"
        v-for="dayGameObj in tempUpcomingGames"
        :key="dayGameObj.date">
        <div class="date-container">
          {{ dayGameObj.date }}
        </div>
        <UpcomingGameCard
          v-for="gameObj in dayGameObj.games"
          :key="gameObj.id"
          :game="gameObj"/>
      </div>
    </div>
    <div
      id="right-arrow-icon-container"
      @click="scrollRight">
      <i class="el-icon-arrow-right"></i>
    </div>
    <div id="calendar-icon-container">
      <i class="el-icon-date"></i>
    </div>
  </div>
</template>

<script>
import PreviousGameCard from '@/components/PreviousGameCard.vue';
import UpcomingGameCard from '@/components/UpcomingGameCard.vue';

export default {
  name: 'UpcomingGamesHeader',
  components: {
    PreviousGameCard,
    UpcomingGameCard,
  },
  data() {
    return {
      tempYesterdaysGames: {
        date: 'Oct 14',
        games: [
          {
            id: '1',
            homeTeam: 'TeamA',
            awayTeam: 'TeamB',
            league: 'League A',
            fieldName: 'Field A',
            time: '8:00 PM',
            homeScore: '3',
            awayScore: '2',
          },
          {
            id: '2',
            homeTeam: 'TeamC',
            awayTeam: 'TeamD',
            league: 'League A',
            fieldName: 'Field B',
            time: '8:00 PM',
            homeScore: '1',
            awayScore: '0',
          },
          {
            id: '3',
            homeTeam: 'TeamX',
            awayTeam: 'TeamY',
            league: 'League B',
            fieldName: 'Field B',
            time: '9:15 PM',
            homeScore: '2',
            awayScore: '5',
          },
        ],
      },
      tempUpcomingGames: [
        {
          date: 'Oct 15',
          games: [
            {
              id: '1',
              homeTeam: 'TeamA',
              awayTeam: 'TeamB',
              league: 'League A',
              fieldName: 'Field A',
              time: '8:00 PM',
            },
            {
              id: '2',
              homeTeam: 'TeamC',
              awayTeam: 'TeamD',
              league: 'League A',
              fieldName: 'Field B',
              time: '8:00 PM',
            },
            {
              id: '3',
              homeTeam: 'TeamX',
              awayTeam: 'TeamY',
              league: 'League B',
              fieldName: 'Field B',
              time: '9:15 PM',
            },
          ],
        },
        {
          date: 'Oct 16',
          games: [
            {
              id: '4',
              homeTeam: 'TeamA',
              awayTeam: 'TeamC',
              league: 'League A',
              fieldName: 'Field A',
              time: '8:00 PM',
            },
            {
              id: '5',
              homeTeam: 'TeamB',
              awayTeam: 'TeamD',
              league: 'League A',
              fieldName: 'Field B',
              time: '8:00 PM',
            },
            {
              id: '6',
              homeTeam: 'TeamX',
              awayTeam: 'TeamY',
              league: 'League B',
              fieldName: 'Field A',
              time: '9:15 PM',
            },
          ],
        },
        {
          date: 'Oct 17',
          games: [
            {
              id: '7',
              homeTeam: 'TeamA',
              awayTeam: 'TeamC',
              league: 'League A',
              fieldName: 'Field A',
              time: '8:00 PM',
            },
            {
              id: '8',
              homeTeam: 'TeamB',
              awayTeam: 'TeamD',
              league: 'League A',
              fieldName: 'Field B',
              time: '8:00 PM',
            },
            {
              id: '9',
              homeTeam: 'TeamX',
              awayTeam: 'TeamY',
              league: 'League B',
              fieldName: 'Field A',
              time: '9:15 PM',
            },
          ],
        },
      ],
    };
  },
  methods: {
    scrollRight() {
      const upcomingGamesHeader = this.$refs['upcoming-games-header'];
      const scrollContainer = this.$refs['upcoming-games-header-scroll-container'];
      scrollContainer.scrollLeft += (upcomingGamesHeader.clientWidth - 132);
    },
    scrollLeft() {
      const upcomingGamesHeader = this.$refs['upcoming-games-header'];
      const scrollContainer = this.$refs['upcoming-games-header-scroll-container'];
      scrollContainer.scrollLeft -= (upcomingGamesHeader.clientWidth - 132);
    },
  },
  mounted() {
    const previousGamesHeader = this.$refs['prev-day-games-container'];
    const scrollContainer = this.$refs['upcoming-games-header-scroll-container'];
    scrollContainer.scrollLeft += previousGamesHeader.clientWidth;
    document.getElementById('upcoming-games-header-scroll-container').classList.add('smoothScroll');
  },
};

</script>

<style lang='scss' scoped>
#upcoming-games-header {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 9vh;
  min-height: 58px;

  #left-arrow-icon-container,
  #right-arrow-icon-container,
  #calendar-icon-container{
    height: calc(100% - 2px);
    width: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    border: 1px solid #d2d2d2;
    z-index: 1;

    &:hover{
      cursor: pointer;
      box-shadow: 0 0 4px 0 rgba(0,0,0,.5);

      i{
        font-weight: bold;
      }
    }
  }

  .smoothScroll{
    scroll-behavior: smooth;
  }

  #upcoming-games-header-scroll-container{
    overflow-x: auto;
    overflow-y: hidden;
    width: calc(100% - 120px);
    display: flex;
    flex-direction: row;
    border-bottom: 1px solid #d2d2d2;
    border-top: 1px solid #d2d2d2;

    #prev-day-games-container{
      display: flex;
      flex-direction: row;
      align-items: center;
    }

    .date-container{
      height: calc(100% + 1px);
      background: #e8e8e8;
      border-right: 1px solid #d2d2d2;
      display: flex;
      align-items: center;
      font-weight: bold;
      width: 40px;
      user-select: none;
    }

    #day-game-container{
      display: flex;
      flex-direction: row;
      align-items: center;
    }
  }
}
</style>
