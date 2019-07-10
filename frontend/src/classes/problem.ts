export interface IProblem {
  name: string
  difficulty: number
  description: string
  points: number
  hint?: string
}


export class Problem  {
  public name: string
  public difficulty: number
  public description: string
  public points: number
  public hint?: string

  constructor(problem: IProblem) {
    this.name = problem.name
    this.difficulty = problem.difficulty
    this.description = problem.description
    this.points = problem.points
    this.hint = problem.hint
  }

  get id() {
    return this.name.toUpperCase()
  }
}
