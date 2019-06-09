export class Problem  {
  constructor(
    public name: string,
    public difficulty: number,
    public description: string,
    public points: number,
    public id: string,
    public hint?: string,
  ) {}
}
