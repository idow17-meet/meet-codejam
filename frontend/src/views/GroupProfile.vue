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
            <div class="solved-badge">
                <div class="solved-badge-title">
                    <router-link :to="{name: 'viewProblem', params: {number: $store.getters.getScorePosition(score.problem.name)}}"><h3>{{ score.problem.name }} <i class="fa fa-check" aria-hidden="true"></i></h3></router-link>
                </div>
                <div class="solved-badge-content">
                    <p>Score: {{ score.currentPoints }} / {{ score.problem.points }}</p>
                    <p>Difficulty: {{ score.problem.difficulty }}</p>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Group, Score} from '@/classes'

@Component
export default class GroupProfile extends Vue {
  @Prop() private name!: string
  private group: Group = this.$store.getters['groups/group'](this.name)
  private solvedScores: Score[] = this.$store.getters.solvedScores(this.name)
}
</script>

<style lang="scss" scoped>
.solved-badge
{
    padding: 0px;
    background-color: white;
    color: black;
    box-shadow: 0 16px 32px 0 rgba(0, 0, 0, 0.5), 0 12px 40px 0 rgba(0, 0, 0, 0.7);
    margin-top: 30px;
    margin-bottom: 15px;
}

.solved-badge-title
{
    background-color: lightblue;
    width: 100%;
    padding: 10px;
    border-bottom: 2px black solid;
    vertical-align: middle !important;
}

.solved-badge-content
{
    padding: 20px;
}

.solved-badge-title a {
    color: rgb(25, 25, 83);
}

.solved-badge-title a:hover{
    text-decoration: none;
    color: rgb(80, 80, 184);
}

.row-badges {
    margin-left: 20px;
    margin-right: 20px;
}
</style>
