<template>
  <div>
    <div class="row">
        <div class="col-md-4 offset-md-4"><h1 id="group-name" >{{ group.name }}</h1></div>
    </div>
    <div class="row" v-for="member in group.members" :key="member">
        <div class="col-md-4 offset-md-4"><h3>{{ member }}</h3></div>
    </div>
    <div class="row" style="margin-top: 20px;">
        <div class="col-md-4 offset-md-4"><h2>Solved Problems:</h2></div>
    </div>
    <div class="row row-badges">
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

@Component({components: { SolvedBadge }})
export default class GroupProfile extends Vue {
  @Prop() private name!: string
  private group: Group = this.$store.getters['groups/group'](this.name)
  private solvedScores: Score[] = this.$store.getters['scores/solved'](this.name)
}
</script>

<style lang="scss" scoped>
.row-badges {
    margin-left: 20px;
    margin-right: 20px;
}
</style>
