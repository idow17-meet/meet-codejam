import { MutationTree, Dictionary } from 'vuex'
import { ScoresState } from './types'
import { Score } from '@/classes'
import { RootState } from '@/store/types'


export const mutations: MutationTree<ScoresState> = {
  setScores(state, scores: Dictionary<Score[]>) {
    state.scores = scores
  },
}
