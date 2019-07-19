import { ActionTree } from 'vuex'
import { ScoresState } from './types'
import { RootState } from '@/store/types'
import { Score, IScore, Problem } from '@/classes'
import axios from 'axios'


export const actions: ActionTree<ScoresState, RootState> = {
  fetchGroup(context, groupName: string) {
    return new Promise((resolve, reject) => {
      axios.get('/api/scores/' + groupName)
      .then((response) => {
        const rawScores: IScore[] = response.data
        const scores = rawScores.map((rawScore: IScore) => new Score(rawScore))
        groupName = groupName.toUpperCase()
        context.commit('setGroupScores', {groupName, scores})
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
