import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { UserState } from './types'
import { mutations } from './mutations'
import { actions } from './actions'
import { getters } from './getters'


const tempGroupId = 'THE UNICORNS'


const state: UserState = {
  groupId: tempGroupId,
}

const userModule: Module<UserState, RootState> = {
  state,
  mutations,
  actions,
  getters,
}

export default userModule
