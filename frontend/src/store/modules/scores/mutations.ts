import { MutationTree } from 'vuex'
import { ScoresState } from './types'
import { Score } from '@/classes'
import { RootState } from '@/store/types'


export const mutations: MutationTree<ScoresState> = {
  setScores(state, scores: Score[]) {
    state.scores = scores
  },
}
