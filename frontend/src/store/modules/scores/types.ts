import { Score } from '@/classes'
import { Dictionary } from 'vuex'

export interface ScoresState {
    scores: Dictionary<Score[]>
}
