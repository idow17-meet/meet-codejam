<template>
<div>
  <div class="row">
    <div class="col-md-3"></div>
    <div class="col-md-6">
      <h1><b>{{ problem.name }}</b></h1>
    </div>
    <div class="col-md-3"></div>
  </div>

  <div class="row">
    <div class="col-md-3 offset-md-2">
      <h2>Difficulty: {{ problem.difficulty }}</h2>
    </div>
    <div class="col-md-3 offset-md-2">
      <h2>Points: {{ problem.points }}</h2>
    </div>
    <div class="col-md-3"></div>
  </div>

  <div class="row problem-row">
    <div class="col-md-3"></div>
    <div class="col-md-6 problem">
      <p class="problem" v-html="problem.description"></p>
      <p class="problem" v-if="problem.hint">HINT: {{ problem.hint }}</p>
    </div>
    <div class="col-md-3"></div>
  </div>

  <div class="row">
    <div class="col-md-6 offset-md-3" v-if="!solved">
        <message-box messageType="error" v-if="error">{{ error }}</message-box>
        <div class="hint-div" v-if="!score.hintUsed">
          <div class="row">
            <div class="col-md-10">
                <p class="hint-alert">Using a hint will limit the maximum points to: {{ problem.points / 2 }}</p>
            </div>
            <div class="col-md-1">
              <input type="submit" class="btn btn-sm btn-info" value="Use Hint" @click.prevent="useHint">
            </div>
          </div>
        </div>
        <h4>Enter your answer below</h4>
        <form class="form justify-content-center" role="form" @submit.prevent="submitAnswer">
          <div class="form-group">
            <input class="form-control" id="answerbox" v-model="answer" placeholder="Answer here">
          </div>
          <div class="form-group">
            <textarea class="form-control" id="codebox" v-model="code" placeholder="Paste your code here" rows="10"></textarea>
          </div>
          <input class="btn btn-info" type="submit" value="Submit">
        </form>
    </div>
    <div class="col-md-6 offset-md-3" v-if="solved">
      <i class="fa fa-check" aria-hidden="true"></i>
    </div>
  </div>
  <div class="row" style="margin-top: 40px;">
    <div class="col-md-6 offset-md-3">
      <h3>Solved by:</h3>
      <h4 v-for="group in groupsSolved" :key="group.name"><router-link :to="{name: 'groupProfile', params: {name: group.name}}">{{ group.name }}</router-link></h4>
    </div>
  </div>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Group, Problem, Score, ScoreState } from '@/classes'
import MessageBox from '@/components/MessageBox.vue'
import Swal from 'sweetalert2'

@Component({components: { MessageBox }})
export default class ViewProblem extends Vue {
  // Display
  @Prop() private number!: number
  private score: Score = this.$store.getters['user/scores'][this.number - 1]
  private problem: Problem = this.score.problem
  private solved: boolean = this.score.state !== ScoreState.NOT_DONE

  get groupsSolved(): Group[] {
    return this.$store.getters['groups/solvedProblem'](this.problem.name)
  }

  // Form
  private answer: string = ''
  private code: string = ''
  private hint: string = ''
  private error: string = ''

  private useHint() {
    Swal.fire({
      type: 'question',
      title: 'Using A Hint',
      text: 'Are you sure you want to use a hint?',
      confirmButtonText: 'Yes, I\'m sure',
      cancelButtonText: 'Cancel',
      showCancelButton: true,
      reverseButtons: true,
      confirmButtonColor: '#aaaaaa',
      cancelButtonColor: '#1471a7',
    }).then((result) => {
      if (result.value) {
        this.$http.patch('/api/scores/' + this.problem.name + '/hint', {})
        .then((response) => {
          this.score.hintUsed = true
          this.problem.hint = response.data.hint
          this.error = ''
          Swal.fire(
            'Hint Used',
            'Hint used successfully!',
            'success',
          )
        })
        .catch((error) => {
          if (error.response.status === 404){
            Swal.fire(
              'No Available Hint',
              'This problem has no hint',
              'error'
            )
          } else {
            this.error = error.response.data.detail
          }
        })
      }
    })
  }

  private submitAnswer() {
    if (!this.isValidForm()) {
      return
    }

    this.error = ''
    this.$http.post('/api/scores/' + this.problem.name, {answer: this.answer, code: this.code})
    .then((response) => {
      if (response.data.correct) {
        Swal.fire(
          'Correct!',
          'Good job! Now on to the next one',
          'success',
        )
        this.solved = true
        this.score.currentPoints = response.data.points
        this.score.submittedCode = this.code
        this.score.submittedAnswer = this.answer
        this.$store.dispatch('scores/setGroupScore', {groupName: this.$store.getters['user/id'], score: this.score})
      } else {
        Swal.fire(
          'Incorrect Answer',
          'The given answer was incorrect. Keep trying though!',
          'error',
        )
      }
    })
    .catch((error) => {
      this.error = error.response.data.detail
    })
  }

  private isValidForm() {
    let valid = true
    if (!this.code) {
      this.error = 'Please submit your code as well.'
      valid = false
    }

    if (!this.answer) {
      this.error = 'No answer given'
      valid = false
    }

    return valid
  }
}
</script>


<style lang="scss" scoped>
.problem-row {
  margin-top: 20px;
}

div.problem {
  background-color: rgba(52, 175, 176, 0.6);
  border-radius: 5px;
  border: 2px solid white;
  margin-bottom: 10px;
}

p.problem, .hint-alert {
  text-align: left;
  margin: 5px;
}

.hint-div {
  margin-bottom: 10px;
}

.fa-check {
  font-size: 160px;
  color: rgb(119, 233, 119);
}
</style>
