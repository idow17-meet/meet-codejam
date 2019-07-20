import Vue from 'vue'
import Vuex, { StoreOptions } from 'vuex'
import { RootState } from '@/store/types'
import actions from './actions'
import scoresModule from './modules/scores'
import userModule from './modules/user'
import groupsModule from './modules/groups'

Vue.use(Vuex)

const storeOptions: StoreOptions<RootState> = {
  state: {
    version: '1.0.0',
  },
  modules: {
    scores: scoresModule,
    user: userModule,
    groups: groupsModule,
  },
  actions,
}

const store = new Vuex.Store<RootState>(storeOptions)

if (module.hot) {
  // accept actions and mutations as hot modules
  module.hot.accept(['./modules/scores'], () => {
    // require the updated modules
    // have to add .default here due to babel 6 module output
    const scoresModule = require('./modules/scores').default
    const userModule = require('./modules/user').default
    const groupsModule = require('./modules/groups').default
    // swap in the new modules and mutations
    store.hotUpdate({
      modules: {
        scores: scoresModule,
        user: userModule,
        groups: groupsModule,
      },
    })
  })
}

export default store
