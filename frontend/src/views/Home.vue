<template>
<div>
  <!-- Title and user -->
  <div class="row">
    <div class="col-12 col-md-10 offset-0 offset-md-1">
      <span class="logo">me<i>e</i>t codejam 2019</span>
    </div>
  </div>
  <div class="row">
    <div class="col-10 offset-1">
      <h2 id="usernameheader">Hello, {{ user }}</h2>
    </div>
  </div>

  <!-- Problems -->
  <div class="row">
    <div class="table-responsive offset-md-1 col-md-10">
      <table class="table table-hover">
        <thead class="thead-dark">
          <tr>
            <th>No.</th>
            <th>Name</th>
            <th>Difficulty</th>
            <th>Score</th>
            <th>State</th>
          </tr>
        </thead>
        <tbody>
          <!-- Fill with ScoreItems -->
          <score-item v-for="(score, index) in $store.getters.scores" :key="score.problem.id" :score="score" :number="index + 1"></score-item>
        </tbody>
      </table>
    </div>
  </div>

</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import ScoreItem from '@/components/ScoreItem.vue'
import { Score, Problem } from '@/classes'

@Component({components: {ScoreItem}})
export default class Home extends Vue {
  // Static placeholder values until backend integration
  public user: string = 'Danny'
}
</script>

<style lang="scss" scoped>
@import "~@/assets/styles/_variables.scss";

.logo {
  font-family: ArcherPro;
  position: relative;
  font-size: 60px;
  color: $brand-teal;
}

.logo i {
  font-size: 100%;
  font-family: ArcherPro;
  -webkit-transform: translateZ(0) scaleX(-1);
  -moz-transform: translateZ(0) scaleX(-1);
  -ms-transform: translateZ(0) scaleX(-1);
  -o-transform: translateZ(0) scaleX(-1);
  transform: translateZ(0) scaleX(-1);
  filter: FlipH;
  display: inline-block;
  line-height: inherit;
}

i {
  font-style: normal;
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
