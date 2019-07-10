import { GetterTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'
import { Score } from '@/classes'

export const getters: GetterTree<ScoresState, RootState> = {
  all: (state) => {
    return state.scores
  },
  solved: (state) => (groupName: string) => {
    return state.scores[groupName.toUpperCase()].filter((score) => {
      return score.currentPoints > 0
    })
  },
  getPosition: (state) => (problemName: string) => {
    return Object.values(state.scores)[0].findIndex((score: Score) => score.problem.name === problemName) + 1
  },
}
