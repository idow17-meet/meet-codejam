import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { UserState } from './types'
import { mutations } from './mutations'
import { actions } from './actions'
import { getters } from './getters'


const state: UserState = {
  groupId: null,
}

const namespaced = true

const userModule: Module<UserState, RootState> = {
  state,
  mutations,
  actions,
  getters,
  namespaced,
}

export default userModule
