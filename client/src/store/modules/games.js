import GamesService from '@/service/GamesService';

// state
const state = {
  games: [],
  selectedGameId: null,
  gameRosters: [],
};

// getters
const getters = {
  games(state) {
    return state.games;
  },
  selectedGameId(state) {
    return state.selectedGameId;
  },
  selectedGame(state) {
    return state.games.find((game) => game.gameID === state.selectedGameId);
  },
  gameById: (state) => (gameId) => {
    return state.games.find(game => game.gameID === gameId);
  },
  gamesByLeagueId: (state) => (leagueId) => {
    return state.games.filter(game => game.leagueID === leagueId);
  },
  gamesByTeamId: (state) => (teamId) => {
    return state.games.filter(game => game.homeTeamID === teamId || game.awayTeamID === teamId);
  },
  gamesSortedByDate(state) {
    const retObj = {};
    state.games.forEach((game) => {
      const gameDay = game.gameTime.split(' ')[0];
      if (retObj[gameDay]) {
        retObj[gameDay].push(game);
      } else {
        retObj[gameDay] = [game];
      }
    });
    return retObj;
  },
  gamesByLeagueIdSortedByDate: (state, getters) => (leagueId) => {
    const retObj = {};
    getters.gamesByLeagueId(leagueId).forEach((game) => {
      const gameDay = game.gameTime.split(' ')[0];
      if (retObj[gameDay]) {
        retObj[gameDay].push(game);
      } else {
        retObj[gameDay] = [game];
      }
    });
    return retObj;
  },
  gamesByTeamIdSortedByDate: (state, getters) => (teamId) => {
    const retObj = {};
    getters.gamesByTeamId(teamId).forEach((game) => {
      const gameDay = game.gameTime.split(' ')[0];
      if (retObj[gameDay]) {
        retObj[gameDay].push(game);
      } else {
        retObj[gameDay] = [game];
      }
    });
    return retObj;
  },
  gameRosters(state) {
    return state.gameRosters;
  },
  gameRosterByGameID: (state) => (gameID) => {
    return (state.gameRosters.find(gameRoster => gameRoster.gameID === gameID) || {}).players
      || [];
  },
  awayTeamGameRosterById: (state, getters) => (gameID) => {
    return getters.gameRosterByGameID(gameID).filter(player => {
      return player.teamID === getters.gameById(gameID).awayTeamID;
    });
  },
  awayGoalsByGameId: (state, getters) => (gameID) => {
    return getters.awayTeamGameRosterById(gameID).reduce((total, playerObj) => {
      return total + (playerObj.goals !== '' ? parseInt(playerObj.goals, 10) : 0);
    }, 0);
  },
  homeTeamGameRosterById: (state, getters) => (gameID) => {
    return getters.gameRosterByGameID(gameID).filter(player => {
      return player.teamID === getters.gameById(gameID).homeTeamID;
    });
  },
  homeGoalsByGameId: (state, getters) => (gameID) => {
    return getters.homeTeamGameRosterById(gameID).reduce((total, playerObj) => {
      return total + (playerObj.goals !== '' ? parseInt(playerObj.goals, 10) : 0);
    }, 0);
  },
};

// actions
const actions = {
  getLeagueGames({ dispatch, commit }, leagueId) {
    const payload = {
      leagueID: leagueId,
    };
    GamesService.getGames(payload).then((response) => {
      if (response && response.status === 200) {
        const commitPaylaod = {
          leagueID: leagueId,
          games: response.data.games,
        };
        commit('addLeagueGames', commitPaylaod);
        dispatch('getAllGameRosters');
      }
    });
  },
  getAllGameRosters({ getters, commit }) {
    getters.games.forEach(game => {
      const payload = {
        gameID: game.gameID,
      };
      GamesService.getGameRoster(payload).then((response) => {
        if (response && response.status === 200) {
          const commitPayload = {
            gameID: game.gameID,
            players: [
              ...response.data['game-roster'].home,
              ...response.data['game-roster'].away,
            ],
          };
          commit('addGameRoster', commitPayload);
        }
      });
    });
  },
  getSpecificGameRoster({ commit }, gameID) {
    const payload = {
      gameID,
    };
    GamesService.getGameRoster(payload).then((response) => {
      if (response && response.status === 200) {
        const commitPayload = {
          gameID,
          players: [
            ...response.data['game-roster'].home,
            ...response.data['game-roster'].away,
          ],
        };
        commit('addGameRoster', commitPayload);
      }
    });
  },
  setSelectedGameId({ commit }, newId) {
    commit('mutateSelectedGameId', newId);
  },
  createGame({ getters, dispatch }, gameObj) {
    gameObj.leagueID = getters.selectedLeagueId;
    return GamesService.createGame(gameObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          dispatch('getLeagueGames', getters.selectedLeagueId);
          return { retVal: true, retMsg: 'Game Created' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  editGame({ dispatch }, gameObj) {
    return GamesService.editGame(gameObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getLeagueGames', gameObj.leagueID);
          return { retVal: true, retMsg: 'Game Edited' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  submitGameRoster({ dispatch }, params) {
    const submitParams = {
      gameID: params.gameID,
      data: params,
    };
    return GamesService.submitGameRoster(submitParams).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          dispatch('getSpecificGameRoster', params.gameID);
          return { retVal: true, retMsg: 'Roster Submitted' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  submitGameRosterEdited({ dispatch }, params) {
    const submitParams = {
      gameID: params.gameID,
      data: params,
    };
    return GamesService.submitGameRosterEdited(submitParams).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          dispatch('getSpecificGameRoster', params.gameID);
          return { retVal: true, retMsg: 'Roster Submitted' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
};

// mutations
const mutations = {
  mutateGames(state, payload) {
    state.games = payload;
  },
  mutateSelectedGameId(state, id) {
    state.selectedGameId = id;
  },
  addLeagueGames(state, payload) {
    state.games = state.games.filter(game => game.leagueID !== payload.leagueID);
    state.games.push(...payload.games);
  },
  addGameRoster(state, payload) {
    state.gameRosters = state.gameRosters.filter(gameRoster => {
      return gameRoster.gameID !== payload.gameID;
    });
    state.gameRosters.push(payload);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
