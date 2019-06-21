import Vue from 'vue'
import Router, { Route } from 'vue-router'
import store from './store'
import Home from './views/Home.vue'
import ViewProblem from './views/ViewProblem.vue'
import GroupProfile from './views/GroupProfile.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/problem/:number',
      name: 'viewProblem',
      component: ViewProblem,
      props: true,
      beforeEnter: (to, from, next) => {
        function isValid(param: number) {
           return param <= store.getters.userScores.length && param >= 1
        }

        if (!isValid(Number(to.params.number))) {
          next('404')
        }

        next()
       },
    },
    {
      path: '/group/:name',
      name: 'groupProfile',
      component: GroupProfile,
      props: true,
      // Validate group exists
      beforeEnter: (to, from, next) => {
        function isValid(name: string) {
           return name.toUpperCase() in store.getters.scores && store.getters['groups/group'](name)
        }

        if (!isValid(to.params.name)) {
          next('404')
        }

        next()
       },
    },
     // TODO: Add 404 instead of redirecting home
    {
      path: '*',
      name: 'notFound',
      redirect: {name: 'home'},
    },
  ],
})
