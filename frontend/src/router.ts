import Vue from 'vue'
import Router, { Route } from 'vue-router'
import store from './store'
import Home from './views/Home.vue'
import ViewProblem from './views/ViewProblem.vue'
import GroupProfile from './views/GroupProfile.vue'
import Login from './views/Login.vue'

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
           return param <= store.getters['user/scores'].length && param >= 1
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
           return name.toUpperCase() in store.getters['scores/all'] && store.getters['groups/group'](name)
        }

        if (!isValid(to.params.name)) {
          next('404')
        }

        next()
       },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        public: true,
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
