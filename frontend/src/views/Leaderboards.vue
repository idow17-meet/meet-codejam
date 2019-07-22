<template>
  <div>
    <div class="row title-row">
      <div class="col-md-4 offset-md-4 flex-col"><h1 id="title">Codejam Leaderboards</h1></div>
      <div class="col-md-2 offset-md-2 flex-col btn-col">
        <button class="btn btn-info" @click.prevent="updateLeaderboards">
          <span>refresh </span>
          <font-awesome-icon icon="sync-alt" class="ld ld-spin" v-if="loading"></font-awesome-icon>
          <span v-if="!loading">({{ refreshTimer }})</span>
        </button>
      </div>
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

  private timerMax = 10 // The amount of seconds between refreshes
  private refreshTimer = this.timerMax
  private timerDistance = 1 // The value by which the timer decreases
  private ticksDelay = 1000 // The amount of miliseconds between ticks
  private intervalId = 0
  private loading = false

  private updateLeaderboards() {
    this.loading = true
    const self = this
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
    this.updateLeaderboards()
    this.$store.dispatch('groups/fetchAll')
  }

  private destroyed() {
    clearInterval(this.intervalId)
  }
}
</script>

<style lang="scss" scoped>
@import '../assets/styles/lib/loading';
@import '../assets/styles/lib/loading-btn';

#title {
  font-weight: 600;
  margin-bottom: 0;
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

.flex-col {
  display: flex;
  align-items: center;
}

.btn {
  font-family: 'Proxima Nova';
  font-weight: bold;
  width: 110px;
}

.title-row {
  margin-bottom: 20px;
}

@media (min-width: 768px) {
    .offset-md-2.btn-col {
       margin-left: 15.3%;
    }
}
</style>
