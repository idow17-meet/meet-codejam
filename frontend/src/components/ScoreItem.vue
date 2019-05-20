<template>
<tr>
  <td>{{ score.position }}</td>
  <td>
    <a href=#broken>{{ score.problem.name }}</a>
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
import { Vue, Component, Prop } from 'vue-property-decorator';

const sliderRed = '#eb7575';
const sliderOrange = '#fac878';
const sliderGreen = '#9bf79b';

@Component({'name': 'score-item'})
export default class ScoreItem extends Vue {
  @Prop() public score!: any;

  get sliderColor() {
    const difficulty = this.score.problem.difficulty;
    if (difficulty < 25) {
      return sliderGreen;
    } else if (difficulty < 50) {
      return sliderOrange;
    }

    return sliderRed;
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
