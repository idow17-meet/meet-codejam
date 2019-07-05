import { MutationTree } from 'vuex'
import { UserState } from './types'
import { RootState } from '@/store/types'


export const mutations: MutationTree<UserState> = {
  login(state, groupId) {
    state.groupId = groupId
  },
  logout(state) {
    state.groupId = null
  },
}
