import { Problem } from '@/classes'

export class Score {
  constructor(
    public problem: Problem,
    public currentPoints: number = 0,
    public hintUsed: boolean = false,
    public submittedAnswer?: string,
    public submittedCode?: string,
    public scoreId?: string,
  ) {}

  get state() {
    if (this.currentPoints === 0) {
      return 'Not Done'
    } else if (this.currentPoints === this.problem.points) {
      return 'Strike (Max Score)'
    } else {
      return 'Split (Partial Score)'
    }
  }
}
