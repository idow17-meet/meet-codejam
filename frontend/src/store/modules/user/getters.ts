import { GetterTree } from 'vuex'
import { UserState } from './types'
import { RootState } from '@/store/types'

export const getters: GetterTree<UserState, RootState> = {
    group: (state, getters, rootState, rootGetters) => {
        return rootGetters['groups/group'](state.groupId)
    },
    scores: (state, getters, rootState, rootGetters) => {
        if (state.groupId) {
            return rootGetters.scores[state.groupId]
        } else {
            return []
        }
    },
    loggedIn: (state) => {
        return state.groupId != null
    },
}
