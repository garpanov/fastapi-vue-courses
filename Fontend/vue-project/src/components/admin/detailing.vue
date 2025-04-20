<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import AboutCourse from './about-course.vue';
import check_auth, { api } from './checkAuth';
check_auth()

const route = useRoute()
const router = useRouter()

const data = ref({})
const cause = ref({'text': '', 'error': false})

async function get_info_course() {
    const id_course = route.params.id_course
    const { data: result } = await api.get(`/admin/info_course/${id_course}`)
    data.value = result
}

async function delete_course() {
    const id_course = route.params.id_course
    if (!cause.value.text) {
        cause.value.error = true
        return
    }
    cause.value.error = false
    await api.delete('/admin/delete_course', { data: { id: id_course, cause: cause.value.text } })
    router.push('/admin')
}

onMounted(async () => {
    await get_info_course()
})
</script>

<template>
    <Header></Header>

    <section class="courses-section py-20">
        <div class=" mb-30 ml-30">
            <h1 class="text-6xl">Detailing</h1>
        </div>
        <AboutCourse :data="data" url_for_lesson="/course-private/lesson/"></AboutCourse>
        <div class="flex justify-center">
            <div class="flex w-8/12 justify-between items-center mt-50 mb-20">
                <div class="flex gap-10">
                    <h2 class="cause-delete text-5xl">Cause:</h2>
                    <textarea v-model="cause.text" id="description" placeholder="Cause delete"
                        :class="{ 'border-[#A8A8A8]': !cause.error, 'border-[#F10000]': cause.error }"
                        class="w-102 h-46 p-4 text-white border rounded-xl placeholder-gray-500 resize-none"></textarea>
                </div>
                <button @click="delete_course"
                    class="button-delete bg-[rgba(255,35,35,0.70)] text-white mt-40 py-4 px-13 text-3xl rounded-3xl cursor-pointer transition hover:bg-[rgba(255,35,35,0.80)] active:bg-[rgba(255,35,35,0.50)]">Delete</button>
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

h1, h2 {
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