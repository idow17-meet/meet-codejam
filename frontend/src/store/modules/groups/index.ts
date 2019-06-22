import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { GroupsState } from './types'
import { mutations } from './mutations'
import { actions } from './actions'
import { getters } from './getters'

const state: GroupsState = {
  groups: [],
}

const namespaced: boolean = true

const groupsModule: Module<GroupsState, RootState> = {
  state,
  mutations,
  actions,
  getters,
  namespaced,
}

export default groupsModule
