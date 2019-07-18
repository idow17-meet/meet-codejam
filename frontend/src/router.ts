import Vue from 'vue'
import Router, { Route } from 'vue-router'
import store from './store'
import Home from './views/Home.vue'
import ViewProblem from './views/ViewProblem.vue'
import GroupProfile from './views/GroupProfile.vue'
import Login from './views/Login.vue'
import NotFound from './views/NotFound.vue'

Vue.use(Router)

const router = new Router({
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
          const scores = store.getters['user/scores']
          return scores && param <= scores.length && param >= 1
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
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        public: true,
      },
    },
    {
      path: '/404',
      name: 'notFound',
      component: NotFound,
      meta: {
        public: true,
      },
    },
    {
      path: '*',
      redirect: {name: 'notFound'},
    },
  ],
})


router.beforeEach((to, from, next) => {
  if (to.meta.public) {
    next()
  }
  // Require auth
  if (!store.getters['user/loggedIn']) {
    next('login')
  }
  next()
})

export default router
