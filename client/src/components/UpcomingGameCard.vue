<template>
  <div id="upcoming-game-card">
    <div id="game-card-left">
      <div id="away-team">
        {{ game.awayTeam }}
      </div>
      <div id="home-team">
        {{ game.homeTeam }}
      </div>
    </div>
    <div id="game-card-right">
      <div id="game-time">
        {{ game.time }}
      </div>
      <div id="game-field">
        {{ game.fieldName }}
      </div>
      <div id="game-league">
        {{ game.league }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UpcomingGameCard',
  props: {
    game: Object,
  },
};
</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#upcoming-game-card{
  height: calc(100% - 2px);
  width: 184px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding: 4px 0px;
  border: 1px solid #d2d2d2;
  user-select: none;

  &:hover{
    cursor: pointer;
    box-shadow: 0 0 4px 0 rgba(0,0,0,.5);
    background: #d8eaff;
    color: $PRIMARY_COLOR;
  }

  #game-card-left{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 0px 8px;
  }

  #game-card-right{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-left: 8px;
    margin-right: 4px;

    #game-time{
      font-size: 0.7rem;
      white-space:nowrap;
    }

    #game-field,
    #game-league{
      font-size: 0.5rem;
      white-space:nowrap;
    }
  }
}
</style>
