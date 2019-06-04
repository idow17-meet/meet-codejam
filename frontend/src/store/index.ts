import Vue from 'vue'
import Vuex from 'vuex'
import scoreModule from './modules/scores'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    scoreModule,
  },
})
