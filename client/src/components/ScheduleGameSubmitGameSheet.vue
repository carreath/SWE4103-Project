<template lang="html">
  <div id="schedule-game-submit-game-sheet">


    <div id="away-team-roster-container">
      <div class="team-name">
        {{ awayTeam.teamName }}
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
            Submit Game Sheet
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
              label="Name">
            </el-table-column>
            <el-table-column
              label="G"
              property="goals">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="2"
                  v-model="scope.row.goals">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              label="CS"
              property="cleanSheet">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="1"
                  v-model="scope.row.cleanSheet">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              label="Y"
              property="yellowCards">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="1"
                  v-model="scope.row.yellowCards">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              label="R"
              property="redCards">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="1"
                  v-model="scope.row.redCards">
                </el-input>
              </template>
            </el-table-column>
          </el-table>
        </span>
      </div>
    </div>


    <div id="home-team-roster-container">
      <div class="team-name">
        {{ homeTeam.teamName }}
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
            Submit Game Sheet
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
              label="Name">
            </el-table-column>
            <el-table-column
              label="G"
              property="goals">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="2"
                  v-model="scope.row.goals">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              label="CS"
              property="cleanSheet">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="1"
                  v-model="scope.row.cleanSheet">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              label="Y"
              property="yellowCards">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="1"
                  v-model="scope.row.yellowCards">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              label="R"
              property="redCards">
              <template
                slot-scope="scope">
                <el-input
                  size="mini"
                  maxlength="1"
                  v-model="scope.row.redCards">
                </el-input>
              </template>
            </el-table-column>
          </el-table>
        </span>
      </div>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ScheduleGameSubmitGameSheet',
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
    awayTeamGameRoster() {
      const awayTeamRoster = this.fullGameRoster.filter(player => {
        return player.teamID === this.selectedGame.awayTeamID;
      }).map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
      });
      return awayTeamRoster;
    },
    homeTeamGameRoster() {
      const awayTeamRoster = this.fullGameRoster.filter(player => {
        return player.teamID === this.selectedGame.homeTeamID;
      }).map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
      });
      return awayTeamRoster;
    },
  },
  methods: {
    ...mapActions([

    ]),
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
};
</script>

<style lang="scss">
@import '@/style/global.scss';

#schedule-game-submit-game-sheet{
  display: flex;
  justify-content: space-around;

  #away-team-roster-container,
  #home-team-roster-container{
    width: 45%;
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
    height: 100%;
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
