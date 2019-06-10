import Vue from 'vue'
import Vuex, { StoreOptions } from 'vuex'
import { RootState } from '@/store/types'
import scoreModule from './modules/scores'
import userModule from './modules/user'

Vue.use(Vuex)

const storeOptions: StoreOptions<RootState> = {
  state: {
    version: '1.0.0',
  },
  modules: {
    scoreModule,
    userModule,
  },
}

const store = new Vuex.Store<RootState>(storeOptions)

if (module.hot) {
  // accept actions and mutations as hot modules
  module.hot.accept(['./modules/scores'], () => {
    // require the updated modules
    // have to add .default here due to babel 6 module output
    const scoreModule = require('./modules/scores').default
    const userModule = require('./modules/user').default
    // swap in the new modules and mutations
    store.hotUpdate({
      modules: {
        scoreModule,
        userModule,
      },
    })
  })
}

store.dispatch('fetchScores')

export default store
