export interface IGroup {
  name: string
  members: string[]
}


export class Group {
  public name: string
  public members: string[]

  constructor(group: IGroup) {
    this.name = group.name
    this.members = group.members
  }

  get id() {
    return this.name.toUpperCase()
  }
}
