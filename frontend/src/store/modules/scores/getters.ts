import { GetterTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'
import { Score } from '@/classes'

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
}
