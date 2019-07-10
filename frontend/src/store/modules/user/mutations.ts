import { MutationTree } from 'vuex'
import { UserState } from './types'
import { RootState } from '@/store/types'


export const mutations: MutationTree<UserState> = {
  login(state, groupId: string) {
    state.groupId = groupId.toUpperCase()
    localStorage.setItem('groupId', groupId.toUpperCase())
  },
  logout(state) {
    state.groupId = null
    localStorage.removeItem('groupId')
  },
}
