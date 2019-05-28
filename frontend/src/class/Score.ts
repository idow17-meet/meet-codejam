export default class Score {
  constructor(
    public groupId: string,
    public problemId: string,
    public currentPoints: number = 0,
    public hintUsed: boolean = false,
    public submittedAnswer?: string,
    public submittedCode?: string,
    public scoreId?: string,
  ) {}
}
