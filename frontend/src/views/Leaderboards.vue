<template>
  <div>
    <div class="row">
      <div class="col-md-6 offset-md-3"><h1 id="title">Codejam Leaderboards</h1></div>
    </div>
    <div class="row">
      <div class="table-responsive offset-md-1 col-md-10">
        <table class="table table-hover table-borderless">
          <thead class="thead-dark">
            <tr>
              <th>Rank</th>
              <th>Group Name</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            <leaderboard-item v-for="rank in ranks" :rank=rank :key=rank.groupName></leaderboard-item>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { LeaderboardRank } from '@/classes'
import LeaderboardItem from '@/components/LeaderboardItem.vue'

@Component({components: { LeaderboardItem }})
export default class Leaderboards extends Vue {
  private tempRank = new LeaderboardRank(1, 'My Group', 9001)
  get ranks() {return this.$store.getters['scores/leaderboards']}

  private created() {
    this.$store.dispatch('scores/fetchAllSolved')
    this.$store.dispatch('groups/fetchAll')
  }
}
</script>

<style lang="scss" scoped>
#title {
  font-weight: 600;
}

table {
  background-color: white;
  color: black;
}

.table .thead-dark th {
  border-top-color: #181818;
  background-color: #181818;
}
</style>
