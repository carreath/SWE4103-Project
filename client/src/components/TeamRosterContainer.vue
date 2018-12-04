<template lang="html">
  <div id="team-roster-container">
    <div class="team-name">
      {{ team.teamName }}
    </div>
    <!-- TODO if roster is submitted -->
    <div
      class="roster-table-container"
      v-if="false">

    </div>
    <div
      v-else
      class="no-roster-submitted-container">
      <span
        class="text-message"
        :style="{
          'background-color': team.colour,
          'color': getTextColor,
        }">
        No Roster Submitted
      </span>
      <span>
        <span
          v-if="userIsTeamManager">
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
        </span>
        <el-button
          class="submit-roster-button"
          type="primary"
          size="mini"
          plain
          v-if="userIsTeamManager"
          @click="submitGameRoster">
          Submit Roster
        </el-button>
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
      teamPlayers: [],
      selectedTeamRoster: [],
    };
  },
  computed: {
    ...mapGetters([
      'user',
      'playersByTeamId',
    ]),
    userIsTeamManager() {
      if (this.user && this.team.managerID === this.user.userID) {
        return true;
      }
      return false;
    },
    getTextColor() {
      if (!this.team) return '';
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
    createTeamRosterList() {
      this.teamPlayers = this.playersByTeamId(this.team.teamID).map(player => {
        return {
          ...player,
          name: `${player.firstName} ${player.lastName}`,
        };
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
    submitGameRoster() {
      console.log('selected: ', this.selectedTeamRoster);
    },
  },
  mounted() {
    this.createTeamRosterList();
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

  .no-roster-submitted-container{
    display:flex;
    flex-direction: column;
    height: 100%;
    border: 1px solid $HOVER_GREY;
    border-radius: 8px;

    .text-message{
      border-radius: 8px 8px 0px 0px;
      padding-top: 8px;
      padding-bottom: 4px;
      font-weight: bold;
      background-color: green;
    }

    .submit-roster-button{
      margin: 8px 0px;
    }
  }
}
</style>
