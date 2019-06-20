import { GetterTree } from 'vuex'
import { UserState } from './types'
import { RootState } from '@/store/types'

export const getters: GetterTree<UserState, RootState> = {
    userGroup: (state, getters, rootState, rootGetters) => {
        return rootGetters['groups/group'](state.groupId)
    },
}
