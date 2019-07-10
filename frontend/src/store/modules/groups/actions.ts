import { ActionTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'
import { Group } from '@/classes'

// Default constant group until backend integration
const defaultGroups = [new Group({name: 'The Unicorns', members: ['Yousef', 'Mariah', 'Daniel', 'Yael']}),
                       new Group({name: 'My Group', members: ['Yossi', 'Abed', 'Kobi', 'Ahmad']})]


export const actions: ActionTree<GroupsState, RootState> = {
  fetchGroups(context) {
    context.commit('setGroups', defaultGroups)
  },
}
