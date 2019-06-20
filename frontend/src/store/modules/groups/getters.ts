import { GetterTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'

export const getters: GetterTree<GroupsState, RootState> = {
    group: (state) => (groupName: string) => {
        if (!groupName) {
            return null
        }
        return state.groups.find((group) => group.id === groupName.toUpperCase())
    },
    allGroups: (state) => state.groups,
}
