import { MutationTree, Dictionary } from 'vuex'
import { ScoresState } from './types'
import { Score } from '@/classes'
import Vue from 'vue'


export const mutations: MutationTree<ScoresState> = {
  setScores(state, scores: Dictionary<Score[]>) {
    state.scores = scores
  },
  setGroupScores(state, {groupName, scores}: {groupName: string, scores: Score[]}) {
    if (groupName in state.scores) {
      state.scores[groupName] = scores
    } else {
      // New keys must be set in order to be reactive
      Vue.set(state.scores, groupName, scores)
    }
  },
  setGroupScore(state, {groupName, score}: {groupName: string, score: Score}) {
    if (groupName in state.scores) {
      const scoreIndex = state.scores[groupName].findIndex(
        (currentScore) => currentScore.problem.id === score.problem.id)
      if (scoreIndex > -1) {
        state.scores[groupName][scoreIndex] = score
      } else {
        state.scores[groupName].push(score)
      }
    } else {
      Vue.set(state.scores, groupName, [score])
    }
  },
}
