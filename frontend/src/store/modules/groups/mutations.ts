import { MutationTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'
import { Group } from '@/classes'


export const mutations: MutationTree<GroupsState> = {
  setGroups: (state, groups: Group[]) => {state.groups = groups},
  setGroup(state, group: Group) {
    const groupIndex = state.groups.findIndex((currentGroup) => currentGroup.id === group.id)
    if (groupIndex === -1) {
      state.groups.push(group)
    } else {
      state.groups[groupIndex] = group
    }
  },
}
