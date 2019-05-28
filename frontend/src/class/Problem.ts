export default class Problem  {
  constructor(
    public name: string,
    public difficulty: number,
    public description: string,
    public points: number,
    public answer: string,
    public problemId: string,
    public hint?: string,
  ) {}
}
