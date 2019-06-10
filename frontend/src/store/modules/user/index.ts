import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { UserState } from './types'
import { Group } from '@/classes'
import { mutations } from './mutations'
import { actions } from './actions'
import { getters } from './getters'

// Default constant group until backend integration
const defaultGroup = new Group('The Unicorns', ['Yousef', 'Mariah', 'Daniel', 'Yael'], 'THE UNICORNS')

const state: UserState = {
  group: defaultGroup,
}

const userModule: Module<UserState, RootState> = {
  state,
  mutations,
  actions,
  getters,
}

export default userModule
