import { GetterTree } from 'vuex'
import { GroupsState } from './types'
import { RootState } from '@/store/types'
import { Group, Score } from '@/classes'

export const getters: GetterTree<GroupsState, RootState> = {
    group: (state) => (groupName: string) => {
        if (!groupName) {
            return null
        }
        return state.groups.find((group) => group.name.toUpperCase() === groupName.toUpperCase())
    },
    allGroups: (state) => state.groups,
    solvedProblem: (state, getters, rootState, rootGetters) => (problemName: string) => {
        const groups: Group[] = []
        const scores = rootGetters.scores

        for (const groupId in scores) {
            if (scores[groupId].find((score: Score) => score.problem.name === problemName &&
                score.currentPoints > 0)) {
                const group = state.groups.find((group: Group) => group.id === groupId)
                if (group) {
                    groups.push(group)
                }
            }
        }

        return groups
    },
}
