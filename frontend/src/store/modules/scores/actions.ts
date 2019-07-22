import { ActionTree, Dictionary } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'
import { Score, IScore, Problem } from '@/classes'
import axios from 'axios'

function convertRawScore(rawScore: IScore): Score {
  const problem = new Problem(rawScore.problem)
  const score = new Score(rawScore)
  score.problem = problem
  return score
}

export const actions: ActionTree<ScoresState, RootState> = {
  fetchGroup(context, groupName: string) {
    return new Promise((resolve, reject) => {
      axios.get('/api/scores/' + groupName)
      .then((response) => {
        const rawScores: IScore[] = response.data
        const scores = rawScores.map((rawScore: IScore) => convertRawScore(rawScore))
        groupName = groupName.toUpperCase()
        context.commit('setGroupScores', {groupName, scores})
        resolve(response)
      })
      .catch((err) => {
        reject(err)
      })
    })
  },
  fetchSolved(context, problemName: string) {
    return new Promise((resolve, reject) => {
      axios.get(`/api/scores/?solved_only=1&problem_name=${problemName}`)
      .then((response) => {
        const solvedDict: Dictionary<IScore[]> = response.data
        for (const groupId in solvedDict) {
          if (solvedDict[groupId].length > 0) {
            solvedDict[groupId] = solvedDict[groupId].map((rawScore) => convertRawScore(rawScore))
            solvedDict[groupId].forEach((score) => {
              context.commit('setGroupScore', {groupName: groupId, score})
            })
          }
        }
        resolve(response)
      })
      .catch((err) => {
        reject(err)
      })
    })
  },
  fetchAllSolved(context) {
    return new Promise((resolve, reject) => {
      context.dispatch('fetchSolved', '')
      .then((response) => {
        resolve(response)
      })
      .catch((err) => {
        reject(err)
      })
    })
  },
  setGroupScore(context, {groupName, score}: {groupName: string, score: Score}) {
    context.commit('setGroupScore', {groupName, score})
  },
}
