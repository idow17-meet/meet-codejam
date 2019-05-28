export default class Group {
  constructor(
    public name: string,
    public members: string[],
    public password: string,
    public hidden: boolean = false,
    public admin: boolean = false,
    public groupId?: string,
  ) {}
}
