<template>
<tr :class="rowClass">
  <td>{{ number }}</td>
  <td>
    <router-link :to="{name: 'viewProblem', params: {number: number}}">{{ score.problem.name }}</router-link>
  </td>
  <td class='difficulty-row'>
    <div class='difficulty-container'>
      <div class='difficulty-slider' :style="{width: score.problem.difficulty + '%', backgroundColor: sliderColor}"></div>
    </div>
  </td>
  <td>{{ score.currentPoints }}/{{ score.problem.points }}</td>
  <td>{{ score.state }}</td>
</tr>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import Score from '@/classes/Score'

const sliderRed = '#eb7575'
const sliderOrange = '#fac878'
const sliderGreen = '#9bf79b'

const rowClassMapping: any = {'Strike (Max Score)': 'table-success',
                              'Split (Partial Score)': 'table-warning',
                              'Not Done': ''}

@Component
export default class ScoreItem extends Vue {
  @Prop() public score!: Score
  @Prop() public number!: number

  get sliderColor() {
    const difficulty = this.score.problem.difficulty
    if (difficulty < 25) {
      return sliderGreen
    } else if (difficulty < 50) {
      return sliderOrange
    }

    return sliderRed
  }

  get rowClass() {
    return rowClassMapping[this.score.state]
  }
}
</script>

<style lang='scss' scoped>
.difficulty-row
{
  position: relative;
}

.difficulty-container
{
  position: absolute;
  top: 50%;
  margin-top: -10px;
  width: 90%;
  height: 20px;
  background-color: white;
  border: 1px solid black;
}

.difficulty-slider
{
  position: relative;
  height: 100%;
}
</style>
