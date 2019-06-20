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
        <div class="col-md-3"></div>
        <div class="col-md-6">
            <!-- {% if state == states[2] %} -->
                <div class="hint-div">
                <!-- {% if problem.hint != "" %}
                    {% if not score.hint_used %} -->
                        <div class="row">
                            <div class="col-md-2">
                                <form  class="form justify-content-center" role="form" action="#broken">
                                    <input style="margin-bottom: 10px;margin-top: 10px;" id="useHintBtn" type="submit" class="btn btn-sm btn-info" value="Use Hint">
                                </form>
                            </div>
                            <div class="col-md-8">
                                    <p class="hint-alert">You get Only Half Of the Points - {{ problem.points / 2 }}</p>
                            </div>
                        </div>
                    <!-- {% endif %}
                {% endif %} -->
                </div>
                <h4>Enter your answer below</h4>
                <span class="error" id="wrong_answer" style="display: none;">Wrong Answer.</span>
                <span class="error" id="nocode" style="display: none;">Please submit your code!</span>
                <form onsubmit="return checkForm()" class="form justify-content-center" role="form" action="#broken" method="post">
                    <div class="form-group">
                        <input class="form-control" id="answerbox" name="answer" placeholder="Answer here">
                    </div>
                    <div class="form-group">
                        <textarea class="form-control" id="codebox" name="code" placeholder="Code here" rows="10"></textarea>
                    </div>
                    <input class="btn btn-info" type="submit"  value="Submit">
                </form>
                <i class="fa fa-check" aria-hidden="true"></i>
        </div>
        <div class="col-md-3"></div>
    </div>
    <div class="row" style="margin-top: 40px;">
        <div class="col-md-6 offset-md-3">
            <h3>Solved by:</h3>
            <h4 v-for="group in groupsSolved" :key="group.groupId"><a href="#broken">{{ group.name }}</a></h4>
        </div>
    </div>
</div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Group, Problem, Score } from '@/classes'

@Component
export default class ViewProblem extends Vue {
    @Prop() private number!: number
    private score: Score = this.$store.getters.userScores[this.number - 1]
    private problem: Problem = this.score.problem

    private groupsSolved: Group[] = [new Group('The Cool kidz', ['Ashley', 'John'], 'lmao')]
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
}

p.problem, .hint-alert {
    text-align: left;
    margin: 5px;
}
</style>
