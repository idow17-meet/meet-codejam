import { ActionTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'
import { Score, Problem } from '@/classes'
import { tempScores, tempScores2 } from './temporaryScores'


export const actions: ActionTree<ScoresState, RootState> = {
  fetchScores(context) {
    context.commit('setScores', {'THE UNICORNS': tempScores, 'MY GROUP': tempScores2})
  },
}
