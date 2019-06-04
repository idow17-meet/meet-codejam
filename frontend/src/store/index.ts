import Vue from 'vue'
import Vuex from 'vuex'
import scoreModule from './modules/scores'


Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    scoreModule,
  },
})


if (module.hot) {
  // accept actions and mutations as hot modules
  module.hot.accept(['./modules/scores'], () => {
    // require the updated modules
    // have to add .default here due to babel 6 module output
    const scoreModule = require('./modules/scores').default
    // swap in the new modules and mutations
    store.hotUpdate({
      modules: {
        scoreModule,
      },
    })
  })
}

store.dispatch('fetchScores')

export default store
