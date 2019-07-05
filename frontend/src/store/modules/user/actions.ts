import { ActionTree } from 'vuex'
import { UserState } from './types'
import { RootState } from '@/store/types'
import axios, { AxiosResponse } from 'axios'

export const actions: ActionTree<UserState, RootState> = {
  login(context, auth) {
    return new Promise((resolve, reject) => {
      axios.post('/api/auth/login', auth)
      .then((response) => {
        context.commit('login', response.data.groupId)
        resolve(response)
      })
      .catch((err) => {
        reject(err)
      })
    })
  },
  logout(context) {
    context.commit('logout')
  },
}
