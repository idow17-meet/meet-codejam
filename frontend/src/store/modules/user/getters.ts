import { GetterTree } from 'vuex'
import { UserState } from './types'
import { RootState } from '@/store/types'

export const getters: GetterTree<UserState, RootState> = {
    group: (state) => {
        return state.group
    },
}
