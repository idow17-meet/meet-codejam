import { GetterTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'

export const getters: GetterTree<ScoresState, RootState> = {
  scores: (state: any) => {
    return state.scores
  },
}
