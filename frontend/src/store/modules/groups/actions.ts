import { ActionTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'
import { Group, IGroup } from '@/classes'
import axios from 'axios'


export const actions: ActionTree<GroupsState, RootState> = {
  fetchAll(context) {
    return new Promise((resolve, reject) => {
      axios.get('/api/groups/')
      .then((response) => {
        let groups: IGroup[] = response.data.groups
        groups = groups.map((rawGroup) => new Group(rawGroup))
        context.commit('setGroups', groups)
        resolve(response)
      })
      .catch((err) => {
        reject(err)
      })
    })
  },
  fetchOne(context, groupName: string) {
    return new Promise((resolve, reject) => {
      axios.get('/api/groups/' + groupName)
      .then((response) => {
        const group = new Group(response.data)
        context.commit('setGroup', group)
        resolve(response)
      })
      .catch((err) => {
        reject(err)
      })
    })
  },
}
