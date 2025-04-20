<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import Aside from './aside-admin.vue';
import check_auth, { api } from './checkAuth';
check_auth()


const courses = ref([])

const router = useRouter()

function about_course(id_course: number) {
    router.push(`/admin/detailing/${id_course}`)
}

async function all_courses() {
    const { data } = await api.get('/all_courses')
    courses.value = data
}

onMounted(async() => {
    await all_courses()
})
</script>

<template>
    <Header></Header>

    <div class="flex">
        <Aside class="w-1/4"></Aside>
        <main class="border-l border-[#101010] pl-15 pt-15 w-3/4">
            <div class="flex justify-between mr-20">
                <h1 class="text-7xl">All courses</h1>
                <form>
                    <label for="search"
                        class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
                    <div class="relative">
                        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                            </svg>
                        </div>
                        <input type="search" id="search"
                            class="block p-4 ps-10 text-md text-gray-900 border border-gray-300 rounded-3xl bg-[#0F0F0F] focus:ring-blue-500 focus:border-blue-500 dark:border-[#525252] dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Search" required />

                    </div>
                </form>
            </div>
            <div class="grid grid-cols-2 ml-20 mr-10 gap-10 mt-20 mb-20">
                <div v-for="course in courses" @click="about_course(course['id'])"
                    class="bg-[#0D0D0D] border-1 border-[#262626] p-10 rounded-[4vw] shadow-xl/80 ring-2 cursor-pointer transition hover:bg-[#171717] hover:-translate-y-0.5">
                    <div class="flex items-center justify-between">
                        <div class="flex flex-col gap-4">
                            <h2 class="h2-courses ml-5 text-3xl">{{ course['name'] }}</h2>
                            <p class="short-description text-lg w-70 h-15">{{ course['short_description'] }}</p>
                        </div>
                        <img class="w-20" :src="course['image_main']" alt="python logo">
                    </div>
                    <div class="flex justify-between ml-5 mr-10 mt-5">
                        <h3 class="text-2xl">{{ course['points'] }} points</h3>
                        <p class="avtor mt-2">by {{ course['author'] }}</p>

                    </div>
                </div>
            </div>
        </main>
    </div>

    <Footer></Footer>
</template>

<style scoped>
main {
    background-image: url('/profile/background.png');
    background-size: cover;
    background-position: center;
}

h1,
h2,
.avtor {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 600;
}

h2 {
    font-family: "Paytone One", sans-serif;
    font-weight: 400;
}

.short-description {
    color: #BBB4B4;
}

.h2-courses {
    font-family: "Inter", sans-serif;
    font-weight: 800;
}

h3 {
    color: #EC5AFF;
    font-family: "Inter", sans-serif;
    font-weight: 900;
}

.avtor {
    font-family: "Inter", sans-serif;
    font-weight: 400;
    font-style: italic;
}
</style>