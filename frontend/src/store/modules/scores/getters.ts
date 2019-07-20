import { GetterTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'
import { Score, LeaderboardRank, Group } from '@/classes'

export const getters: GetterTree<ScoresState, RootState> = {
  all: (state) => {
    return state.scores
  },
  solved: (state) => (groupName: string) => {
    const scores: Score[] = state.scores[groupName.toUpperCase()]
    if (!scores) {
      return []
    }
    return scores.filter((score) => {
      return score.currentPoints > 0
    })
  },
  getPosition: (state) => (problemName: string) => {
    const allScores: Score[][] = Object.values(state.scores)
    if (allScores.length === 0) {
      return -1
    }
    return Object.values(state.scores)[0].findIndex((score: Score) => score.problem.name === problemName) + 1
  },
  leaderboards: (state, getters, rootState, rootGetters) => {
    const ranks: LeaderboardRank[] = []

    // Calculate sum of scores for each group
    // tslint:disable-next-line: forin
    for (const groupId in state.scores) {
      const scores: Score[] = getters.solved(groupId)

      const points = scores.map((score) => score.currentPoints).reduce((prevPoints, currentPoints) => {
        prevPoints += currentPoints
        return prevPoints
      }, 0)

      const name = rootGetters['groups/name'](groupId) || groupId  // Revert to ID if groups haven't loaded yet
      ranks.push(new LeaderboardRank(0, name, points))
    }

    // Add groups with no solved scores
    for (const group of rootGetters['groups/all']) {
      if (ranks.findIndex((rank) => rank.groupName.toUpperCase() === group.id) === -1) {
        ranks.push(new LeaderboardRank(0, group.name, 0))
      }
    }
    // Then assign ranks
    ranks.sort((rank1, rank2) => rank2.score - rank1.score)
    // tslint:disable-next-line: forin
    for (const index in ranks) {
      ranks[index].position = Number(index) + 1
    }

    return ranks
  },
}
