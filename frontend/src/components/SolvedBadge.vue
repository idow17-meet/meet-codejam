<template>
<div class="solved-badge">
  <div class="solved-badge-title">
    <router-link :to="{name: 'viewProblem', params: {number: $store.getters['scores/getPosition'](score.problem.name)}}"><h3>{{ score.problem.name }} <i class="fa fa-check" aria-hidden="true"></i></h3></router-link>
  </div>
  <div class="solved-badge-content">
    <p>Score: {{ score.currentPoints }} / {{ score.problem.points }}</p>
    <p>Difficulty: {{ score.problem.difficulty }}</p>
  </div>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Score } from '@/classes'

@Component
export default class SolvedBadge extends Vue {
  @Prop() public score!: Score
}
</script>

<style lang='scss' scoped>
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
</style>
