<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import AboutCourse from './about-course.vue';
import check_auth, { api } from './checkAuth';
check_auth()

const route = useRoute()
const router = useRouter()

const data = ref({})
const points = ref<number>()
const cause = ref<string>()
const errors = ref({ 'points': false, 'cause': false })


async function get_info_course() {
    const id_course = route.params.id
    const response = await api.get(`/admin/confirmation/${id_course}`)
    data.value = response.data
}

async function accept_course() {
    const id_course = route.params.id
    if (!points.value) {
        errors.value.points = true
        return
    }
    errors.value.points = true
    await api.post('/admin/confirmation_accept', { id: id_course, points: points.value })
    router.push('/admin/confirmation')
}

async function cancel_course() {
    const id_course = route.params.id
    if (!cause.value) {
        errors.value.cause = true
        return
    }
    errors.value.cause = false
    await api.post('/admin/confirmation_cancel', { id: id_course, cause: cause.value })
    router.push('/admin/confirmation')
}

onMounted(async () => {
    await get_info_course()
})
</script>

<template>
    <Header></Header>

    <section class="courses-section py-20">
        <div class=" mb-30 ml-30">
            <h1 class="text-6xl">Confirmation</h1>
        </div>
        <AboutCourse :data="data" url_for_lesson="/admin/confirmation/detail/about_lesson/"></AboutCourse>
        <div class="flex flex-col items-center justify-center">
            <div class="flex w-8/12 items-center justify-center gap-30 mt-50 mb-20">
                <div class="flex gap-10">
                    <h2 class="cause-delete text-5xl">Points:</h2>
                    <input v-model="points" id="name" type="number" aria-describedby="helper-text-explanation"
                        :class="{ 'border-[#A8A8A8]': !errors.points, 'border-[#F10000]': errors.points }"
                        class="border text-xl rounded-2xl pl-4 h-13 pr-5   placeholder-[#545454] text-white"
                        placeholder="Number of points">
                </div>
                <button @click="accept_course"
                    class="button-delete bg-[rgba(11,255,47,0.50)] text-white py-4 px-13 text-3xl rounded-3xl cursor-pointer transition hover:bg-[rgba(11,255,47,0.60)] active:bg-[rgba(11,255,47,0.40)]">Add</button>


            </div>
            <div class="flex w-8/12 items-center justify-center gap-30 mt-50 mb-20">
                <div class="flex gap-10">
                    <h2 class="cause-delete text-5xl">Cause:</h2>
                    <textarea v-model="cause" id="description" placeholder="Cause delete" 
                    :class="{ 'border-[#A8A8A8]': !errors.cause, 'border-[#F10000]': errors.cause }"
                        class="w-102 h-46 p-4 text-white border rounded-xl placeholder-gray-500 resize-none"></textarea>
                </div>
                <div class="flex">
                    <button @click="cancel_course"
                        class="button-delete bg-[rgba(195,195,195,0.40)] text-white py-4 px-13 text-3xl rounded-3xl cursor-pointer transition hover:bg-[rgba(195,195,195,0.50)] active:bg-[rgba(195,195,195,0.30)]">Cancel</button>
                </div>
            </div>

        </div>
    </section>

    <Footer></Footer>
</template>

<style scoped>
.courses-section {
    background-image: url('../../public/courses/background.png');
    background-size: cover;
    background-position: center;
}

h1,
h2 {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}

.cause-delete {
    font-family: "Inter", sans-serif;
    font-weight: 800;
}

.button-delete {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
}

</style>