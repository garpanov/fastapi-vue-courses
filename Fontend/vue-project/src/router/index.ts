import { createRouter, createWebHistory } from 'vue-router'

import Main from '../components/main.vue'
import Courses from '../components/courses/courses.vue'
import Course from '../components/courses/course.vue'
import Login from '../components/login/login.vue'
import Login2 from '../components/login/login2.vue'
import Register from '../components/login/register.vue'
import Register2 from '../components/login/register2.vue'
import Welcome from '../components/profile/welcome.vue'
import CoursePrivate from '../components/profile/course-private.vue'
import CoursePrivateInfo from '../components/profile/course-private-info.vue'
import MyCourses from '../components/profile/my-courses.vue'
import Shop from '../components/profile/shop.vue'
import CreateCourse from '../components/profile/create-course.vue'
import Admin from '@/components/admin/admin.vue'
import Detailing from '@/components/admin/detailing.vue'
import Confirmation from '@/components/admin/confirmation.vue'
import ConfirmationDetail from '@/components/admin/confirmation-detail.vue'
import Aboutlesson from '@/components/admin/about_lesson.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Main,
    },
    {
      path: '/courses',
      name: 'courses',
      component: Courses,
    },
    {
      path: '/course/:id_course',
      name: 'about-course',
      component: Course,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/login/password',
      name: 'login-password',
      component: Login2,
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/register/password',
      name: 'register-password',
      component: Register2
    },
    {
      path: '/profile',
      name: 'profile',
      component: Welcome
    },
    {
      path: '/course-private/:course_id',
      name: 'course-private',
      component: CoursePrivate,
    },
    {
      path: '/course-private/lesson/:course_id/:lesson_id',
      name: 'course-private-info',
      component: CoursePrivateInfo,
    },
    {
      path: '/profile/my-course',
      name: 'my-course',
      component: MyCourses,
    },
    {
      path: '/profile/shop',
      name: 'shop',
      component: Shop,
    },
    {
      path: '/profile/create-course',
      name: 'create-course',
      component: CreateCourse,
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
    },
    {
      path: '/admin/detailing/:id_course',
      name: 'admin detailing',
      component: Detailing,
    },
    {
      path: '/admin/confirmation',
      name: 'admin confirmation',
      component: Confirmation,
    },
    {
      path: '/admin/confirmation/detail/:id',
      name: 'admin confirmation detail',
      component: ConfirmationDetail,
    },
    {
      path: '/admin/confirmation/detail/about_lesson/:id_course/:id_lesson',
      name: 'admin confirmation lesson detail',
      component: Aboutlesson,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    // Всегда прокручиваем в начало страницы при переходе
    return { top: 0 }
  }
})

export default router
