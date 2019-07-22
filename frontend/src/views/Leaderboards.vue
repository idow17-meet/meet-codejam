<template>
  <div>
    <div class="row">
      <div class="col-md-6 offset-md-3"><h1 id="title">Codejam Leaderboards</h1></div>
    </div>
    <div class="row">
      <div class="table-responsive offset-md-1 col-md-10">
        <table class="table table-hover">
          <thead class="thead-dark">
            <tr>
              <th>Rank</th>
              <th>Group Name</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody is="transition-group" name="leaderboard">
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

  private refreshTimer = 0
  private timerMax = 3 // The amount of seconds between refreshes
  private timerDistance = 1 // The value by which the timer decreases
  private ticksDelay = 1000 // The amount of miliseconds between ticks
  private intervalId = 0
  private loading = false

  private updateLeaderboards() {
    this.loading = true
    let self = this
    this.$store.dispatch('scores/fetchAllSolved')
    .then((response) => {
      self.loading = false
      self.refreshTimer = this.timerMax
    })
  }

  private tickRefresh() {
    this.refreshTimer -= this.timerDistance

    if (this.refreshTimer <= 0) {
      this.updateLeaderboards()
    }
  }

  private created() {
    this.intervalId = setInterval(this.tickRefresh, this.ticksDelay)
    this.tickRefresh()
    this.$store.dispatch('groups/fetchAll')
  }

  private destroyed() {
    clearInterval(this.intervalId)
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
  background-color: #181818;
}

.leaderboard-move {
  transition: transform 1s;
}
</style>
