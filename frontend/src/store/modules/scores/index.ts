import { Module } from 'vuex'
import { RootState } from '@/store/types'
import { ScoresState } from './types'
import { Score } from '@/classes'
import { mutations } from './mutations'
import { actions } from './actions'
import { getters } from './getters'

const state: ScoresState = {
  scores: {},
}

const namespaced = true

const scoresModule: Module<ScoresState, RootState> = {
  state,
  mutations,
  actions,
  getters,
  namespaced,
}

export default scoresModule
