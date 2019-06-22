import { MutationTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'
import { Group } from '@/classes'


export const mutations: MutationTree<GroupsState> = {
  setGroups: (state, groups: Group[]) => {state.groups = groups},
}
