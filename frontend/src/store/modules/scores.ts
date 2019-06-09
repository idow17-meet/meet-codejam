import { Module } from 'vuex'
import { Score, Problem } from '@/classes'

// Static scores here until rest api integration
const tempScores = [
  // Score #1
  new Score (
    new Problem (
      'Factorials Factory',
      10,
      'Some description',
      8000,
      '1',
    ),
  ),
  // Score #2
  new Score (
    new Problem (
      'Palindromic Number',
      37,
      'Some description noitpircsed emoS',
      18700,
      '2',
    ),
  ),
  new Score (
    new Problem (
      'Ladder Climbing',
      75,
      '#Some<br>#Description<br>#Here',
      37000,
      '3',
    ),
    37000,
  ),
]


// Actual module
const state = {
  scores: [],
}

const mutations = {
  setScores(state: any, scores: Score[]) {
    state.scores = scores
  },
}

const actions = {
  fetchScores(context: any) {
    context.commit('setScores', tempScores)
  },
}

const getters = {
  scores: (state: any) => {
    return state.scores
  },
}

const scoreModule: Module<any, any> = {
  state,
  mutations,
  actions,
  getters,
}

export default scoreModule
