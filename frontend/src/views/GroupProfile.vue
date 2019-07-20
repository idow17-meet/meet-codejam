<template>
  <div v-if="group">
    <div class="row">
        <div class="col-md-4 offset-md-4"><h1 id="group-name" >{{ group.name }}</h1></div>
    </div>
    <div class="row" v-for="member in group.members" :key="member">
        <div class="col-md-4 offset-md-4"><h3>{{ member }}</h3></div>
    </div>
    <div class="row solved-row">
        <div class="col-md-4 offset-md-4"><h2>Solved Problems:</h2></div>
    </div>
    <div class="row badges-row" v-if="solvedScores">
        <div class="col-md-4" v-for="score in solvedScores" :key="score.problem.name">
            <solved-badge :score="score"></solved-badge>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Group, Score} from '@/classes'
import SolvedBadge from '@/components/SolvedBadge.vue'
import { Route } from 'vue-router'
import { AxiosError } from 'axios'

@Component({components: { SolvedBadge }})
export default class GroupProfile extends Vue {
  @Prop() private name!: string
  get group(): Group {return this.$store.getters['groups/one'](this.name)}
  get solvedScores(): Score[] {return this.$store.getters['scores/solved'](this.name)}

  private created() {
    if (this.solvedScores.length === 0) {
      const promise = this.$store.dispatch('scores/fetchGroup', this.name)
      this.redirectIfNotFound(promise)
    }

    if (!this.group) {
      const promise = this.$store.dispatch('groups/fetchOne', this.name)
      this.redirectIfNotFound(promise)
    }
  }

  private redirectIfNotFound(promise: Promise<any>) {
    promise.catch((error: AxiosError<any>) => {
      if (error.response && error.response.status === 404) {
          this.$router.push({name: 'notFound'})
        }
    })
  }
}
</script>

<style lang="scss" scoped>
.badges-row {
    margin-left: 20px;
    margin-right: 20px;
}

.solved-row {
  margin-top: 20px;
}
</style>
