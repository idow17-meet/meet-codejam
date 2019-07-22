<template is="transition-group">
<tr>
  <td>{{ rank.position }}</td>
  <td>
    <router-link :to="{name: 'groupProfile', params: {name: rank.groupName}}">{{ rank.groupName }}</router-link>
  </td>
  <td>{{ rank.score }}</td>
</tr>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { LeaderboardRank } from '@/classes'

@Component
export default class LeaderboardItem extends Vue {
  @Prop() public rank!: LeaderboardRank
}
</script>

<style lang='scss' scoped>

</style>
