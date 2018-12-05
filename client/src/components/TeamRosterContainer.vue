<template lang="html">
  <div id="team-roster-container">
    <div class="team-name">
      {{ team.teamName }}
    </div>

    <div class="roster-table-container">
      <span
        class="text-message"
        :style="{
          'background-color': team.colour,
          'color': getTextColor,
        }">
        <span :style="{'width': getWidth}">
        </span>
        <span>
          {{ rosterTableHeader }}
        </span>
        <span>
          <el-button
            plain
            v-if="userIsTeamManager && !managerEditing"
            size="mini"
            icon="el-icon-edit"
            @click="handleRosterEditClick(true)">
          </el-button>
          <el-button
            plain
            v-if="userIsTeamManager && managerEditing"
            size="mini"
            icon="el-icon-close"
            @click="handleRosterEditClick(false)">
          </el-button>
        </span>
      </span>

      <span>
        <span
          v-if="teamGameRosterSubmitted && !managerEditing">
          <el-table
            ref="team-roster-table"
            :data="teamGameRoster"
            style="width: 100%"
            max-height="800">
            <el-table-column
              label="#"
              property="number"
              width="100px">
            </el-table-column>
            <el-table-column
              property="name"
              label="Name">
            </el-table-column>
          </el-table>
        </span>

        <span
          v-show="userIsTeamManager && managerEditing">
          <el-table
            ref="submit-roster-table"
            :data="teamPlayers"
            style="width: 100%"
            max-height="800"
            @row-click="handleRowClick"
            @selection-change="handleSelectionChange">
            <el-table-column
              type="selection">
            </el-table-column>
            <el-table-column
              label="#"
              property="number"
              width="70px">
              <template
                slot-scope="scope">
                <el-input
                  size="medium"
                  maxlength="2"
                  :disabled="!selectedTeamRoster.find(x => x.playerID === scope.row.playerID)"
                  v-model="scope.row.number">
                </el-input>
              </template>
            </el-table-column>
            <el-table-column
              property="name"
              label="Name">
            </el-table-column>
          </el-table>
          <el-button
            class="submit-roster-button"
            type="primary"
            size="mini"
            plain
            v-if="userIsTeamManager"
            @click="submitGameRosterClicked"
            :disabled="selectedTeamRoster.length < 1">
            Submit Roster
          </el-button>
        </span>
      </span>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'TeamRosterContainer',
  props: {
    team: Object,
  },
  data() {
    return {
      selectedTeamRoster: [],
      managerEditing: false,
    };
  },
  computed: {
    ...mapGetters([
      'user',
      'playersByTeamId',
      'selectedGameId',
      'gameRosters',
    ]),
    getWidth() {
      if (this.teamGameRosterSubmitted && this.userIsTeamManager) {
        return this.managerEditing ? '44px' : '44px';
      }
      return '0px';
    },
    userIsTeamManager() {
      if (this.user && this.team.managerID === this.user.userID) {
        return true;
      }
      return false;
    },
    teamPlayers() {
      return this.playersByTeamId(this.team.teamID).map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
      });
    },
    teamGameRoster() {
      const gameRosterObj = this.gameRosters.find(gameRoster => {
        return gameRoster.gameID === this.selectedGameId;
      });
      if (!gameRosterObj) {
        return null;
      }
      const teamRoster = gameRosterObj.players.filter(player => player.teamID === this.team.teamID);
      const teamRosterFormatted = teamRoster.map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
      });
      return teamRosterFormatted;
    },
    teamGameRosterSubmitted() {
      return (this.teamGameRoster || []).length > 0;
    },
    rosterTableHeader() {
      if (this.teamGameRosterSubmitted) {
        return 'Game Roster';
      }
      return this.userIsTeamManager ? 'Submit Roster' : 'No Roster Submitted';
    },
    getTextColor() {
      if (!this.team || !this.team.colour) return '';
      const hexString = this.team.colour.substring(1);
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
  },
  methods: {
    ...mapActions([
      'submitGameRoster',
    ]),
    colourConversion(c) {
      c /= 255.0;
      if (c <= 0.03928) {
        c /= 12.92;
      } else {
        c = ((c + 0.055) / 1.055) ** 2.4;
      }
      return c;
    },
    handleRosterEditClick(val) {
      this.managerEditing = val;
      this.$nextTick().then(() => {
        this.teamGameRoster.forEach(rosterPlayer => {
          this.teamPlayers.forEach((teamPlayer, index) => {
            if (teamPlayer.playerID === rosterPlayer.playerID) {
              teamPlayer.number = rosterPlayer.number;
              this.$refs['submit-roster-table'].toggleRowSelection(this.teamPlayers[index], true);
            }
          });
        });
      });
    },
    handleRowClick(row, event, column) {
      if (column.label !== '#') {
        this.$refs['submit-roster-table'].toggleRowSelection(row);
      }
    },
    handleSelectionChange(val) {
      this.selectedTeamRoster = val;
    },
    submitGameRosterClicked() {
      if (this.selectedTeamRoster.length === 0) {
        return;
      }
      if (this.selectedTeamRoster.find(x => !x.number)) {
        this.$message({
          showClose: true,
          message: 'Please Enter All Selected Player Numbers',
          type: 'error',
        });
        return;
      }
      const submitParams = {
        gameID: this.selectedGameId,
        players: this.selectedTeamRoster,
      };
      this.submitGameRoster(submitParams).then(response => {
        if (response.retVal) {
          this.errMsg = null;
        } else {
          this.$message({
            showClose: true,
            message: 'OOPS! Sometihng Went Wrong',
            type: 'error',
          });
        }
      });
    },
  },
  mounted() {
  },
};
</script>

<style lang="scss" scoped>
@import '@/style/global.scss';

#team-roster-container{
  width: 100;

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
