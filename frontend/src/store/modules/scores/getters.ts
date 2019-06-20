import { GetterTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'

export const getters: GetterTree<ScoresState, RootState> = {
  scores: (state) => {
    return state.scores
  },
  solvedScores: (state) => (groupName: string) => {
    return state.scores[groupName.toUpperCase()].filter((score) => {
      return score.currentPoints === score.problem.points
    })
  },
}
