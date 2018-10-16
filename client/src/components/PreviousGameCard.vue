<template>
  <div id="previous-game-card">
    <div id="game-card-left">
      <div
        id="away-team"
        :class="{'boldText': game.awayScore > game.homeScore}">
        {{ game.awayTeam }}&nbsp;&nbsp;{{ game.awayScore }}
      </div>
      <div
        id="home-team"
        :class="{'boldText': game.awayScore < game.homeScore}">
        {{ game.homeTeam }}&nbsp;&nbsp;{{ game.homeScore }}
      </div>
    </div>
    <div id="game-card-right">
      <div id="game-result">
        Final
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
export default{
  name: 'PreviousGameCard',
  props: {
    game: Object,
  },
};
</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#previous-game-card{
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
    white-space: nowrap;

    .boldText{
      font-weight: bold;
    }
  }

  #game-card-right{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-left: 8px;
    margin-right: 4px;

    #game-result{
      font-size: 0.7rem;
      font-weight: bold;
      white-space: nowrap;
    }

    #game-field,
    #game-league{
      font-size: 0.5rem;
      white-space:nowrap;
    }
  }
}
</style>
