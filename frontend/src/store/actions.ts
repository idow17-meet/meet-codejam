import { ActionTree } from 'vuex'
import { RootState } from './types'


const actions: ActionTree<RootState, RootState> = {
  fetchBaseState(context) {
    context.dispatch('scores/fetchGroup', context.getters['user/id'])
    context.dispatch('groups/fetchOne', context.getters['user/id'])
  },
}

export default actions
