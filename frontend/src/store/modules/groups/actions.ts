import { ActionTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'
import { Group } from '@/classes'

// Default constant group until backend integration
const defaultGroups = [new Group('The Unicorns', ['Yousef', 'Mariah', 'Daniel', 'Yael'], 'THE UNICORNS'),
                       new Group('Awesomers', ['Yossi', 'Abed', 'Kobi', 'Ahmad'], 'AWESOMERS')]


export const actions: ActionTree<GroupsState, RootState> = {
  fetchGroups(context) {
    context.commit('setGroups', defaultGroups)
  },
}
