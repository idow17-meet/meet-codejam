import { Problem, IProblem } from '@/classes'


export interface IScore {
  problem: IProblem | Problem
  currentPoints?: number
  hintUsed?: boolean
  submittedAnswer?: string
  submittedCode?: string
}


export class Score {
  public problem: Problem
  public currentPoints: number
  public hintUsed: boolean
  public submittedAnswer?: string
  public submittedCode?: string

  constructor(score: IScore) {
    this.problem = new Problem(score.problem)
    this.currentPoints = score.currentPoints || 0
    this.hintUsed = score.hintUsed || false
    this.submittedAnswer = score.submittedAnswer
    this.submittedCode = score.submittedCode
  }

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
