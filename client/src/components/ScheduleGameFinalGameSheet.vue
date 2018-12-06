<template lang="html">
  <div id="schedule-game-final-game-sheet">
    <div id="roster-container">
      <div id="away-team-roster-container">
        <div class="team-name">
          <div class="team-name-text">
            {{ awayTeam.teamName }}
          </div>
          <div class="team-score">
            {{ awayFinalScore }}
          </div>
        </div>
        <div class="roster-table-container">
          <span
            class="text-message"
            :style="{
              'background-color': awayTeam.colour,
              'color': getTextColor(awayTeam),
            }">
            <span>
            </span>
            <span>
              Game Sheet
            </span>
            <span>
            </span>
          </span>
          <span>
            <el-table
              ref="team-roster-table"
              :data="awayTeamGameRoster"
              style="width: 100%"
              max-height="800">
              <el-table-column
                label="#"
                property="number"
                width="37px">
              </el-table-column>
              <el-table-column
                property="name"
                label="Name"
                min-width="120px">
              </el-table-column>
              <el-table-column
                label="G"
                property="goals">
              </el-table-column>
              <el-table-column
                label="CS"
                property="cleanSheet">
              </el-table-column>
              <el-table-column
                label="Y"
                property="yellowCards">
              </el-table-column>
              <el-table-column
                label="R"
                property="redCards">
              </el-table-column>
            </el-table>
          </span>
        </div>
      </div>


      <div id="home-team-roster-container">
        <div class="team-name">
          <div class="team-name-text">
            {{ homeTeam.teamName }}
          </div>
          <div class="team-score">
            {{ homeFinalScore }}
          </div>
        </div>
        <div class="roster-table-container">
          <span
            class="text-message"
            :style="{
              'background-color': homeTeam.colour,
              'color': getTextColor(homeTeam),
            }">
            <span>
            </span>
            <span>
              Game Sheet
            </span>
            <span>
            </span>
          </span>
          <span>
            <el-table
              ref="team-roster-table"
              :data="homeTeamGameRoster"
              style="width: 100%"
              max-height="800">
              <el-table-column
                label="#"
                property="number"
                width="37px">
              </el-table-column>
              <el-table-column
                property="name"
                label="Name"
                min-width="120px">
              </el-table-column>
              <el-table-column
                label="G"
                property="goals">
              </el-table-column>
              <el-table-column
                label="CS"
                property="cleanSheet">
              </el-table-column>
              <el-table-column
                label="Y"
                property="yellowCards">
              </el-table-column>
              <el-table-column
                label="R"
                property="redCards">
              </el-table-column>
            </el-table>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ScheduleGameFinalGameSheet',
  data() {
    return {
      awayTeamGameRoster: [],
      homeTeamGameRoster: [],
    };
  },
  computed: {
    ...mapGetters([
      'gameRosters',
      'selectedGame',
      'teamById',
      'selectedGameId',
    ]),
    awayTeam() {
      return this.teamById(this.selectedGame.awayTeamID);
    },
    homeTeam() {
      return this.teamById(this.selectedGame.homeTeamID);
    },
    fullGameRoster() {
      const gameRosterObj = this.gameRosters.find(gameRoster => {
        return gameRoster.gameID === this.selectedGameId;
      });
      return gameRosterObj ? gameRosterObj.players : [];
    },
    awayFinalScore() {
      return this.awayTeamGameRoster.reduce((total, playerObj) => {
        return total + (playerObj.goals !== '' ? parseInt(playerObj.goals, 10) : 0);
      }, 0);
    },
    homeFinalScore() {
      return this.homeTeamGameRoster.reduce((total, playerObj) => {
        return total + (playerObj.goals !== '' ? parseInt(playerObj.goals, 10) : 0);
      }, 0);
    },
  },
  methods: {
    ...mapActions([

    ]),
    setAwayTeamGameRoster() {
      this.awayTeamGameRoster = this.fullGameRoster.filter(player => {
        return player.teamID === this.selectedGame.awayTeamID;
      }).map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
      });
    },
    setHomeTeamGameRoster() {
      this.homeTeamGameRoster = this.fullGameRoster.filter(player => {
        return player.teamID === this.selectedGame.homeTeamID;
      }).map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
      });
    },
    getTextColor(team) {
      if (!team || !team.colour) return '';
      const hexString = team.colour.substring(1);
      let r = parseInt(hexString.substring(0, 2), 16);
      let g = parseInt(hexString.substring(2, 4), 16);
      let b = parseInt(hexString.substring(4), 16);
      r = this.colourConversion(r);
      g = this.colourConversion(g);
      b = this.colourConversion(b);
      const l = (0.2126 * r) + (0.7152 * g) + (0.0722 * b);
      // $DARK_TEXT & $SECONDARY_COLOR
      return l > 0.185 ? '#2c3e50' : '#fcfcfc'; // $DARK_TEXT
    },
    colourConversion(c) {
      c /= 255.0;
      if (c <= 0.03928) {
        c /= 12.92;
      } else {
        c = ((c + 0.055) / 1.055) ** 2.4;
      }
      return c;
    },
  },
  watch: {
    fullGameRoster() {
      this.setAwayTeamGameRoster();
      this.setHomeTeamGameRoster();
    },
  },
  mounted() {
    this.setAwayTeamGameRoster();
    this.setHomeTeamGameRoster();
  },
};
</script>

<style lang="scss">
@import '@/style/global.scss';

#schedule-game-final-game-sheet{
  display: flex;
  flex-direction: column;

  #roster-container{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    #away-team-roster-container,
    #home-team-roster-container{
      width: 47%;
    }
  }

  #footer{
    display: flex;
    flex-direction: column;
    align-self: center;
    width: 30%;
    margin-top: 12px;

    #score-container{
      font-size: 1.5rem;
      font-weight: bold;
    }

    #submit-button-container{

    }
  }

  .team-name{
    font-size: 1.4rem;
    font-weight: bold;
  }

  .roster-table-container{

  }

  .roster-table-container{
    display:flex;
    flex-direction: column;
    border: 1px solid $HOVER_GREY;
    border-radius: 8px;

    .text-message{
      border-radius: 8px 8px 0px 0px;
      padding-top: 8px;
      padding-bottom: 4px;
      padding-right: 8px;
      padding-left: 8px;
      font-weight: bold;
      background-color: green;
      display: flex;
      justify-content: space-between;
    }

    .submit-roster-button{
      margin: 8px 0px;
    }
  }
}
</style>
