<script setup lang="ts">
import Header from '../header.vue';
import Aside from './aside.vue';
import Footer from '../footer.vue';
import check_auth from './checkAuth';
check_auth()

</script>

<template>
    <Header></Header>

    <div class="flex">
        <Aside class="w-1/4"></Aside>
        <main class="border-l border-[#101010] pl-20 pt-20 w-3/4">
            <div class="flex justify-between items-center">
                <h1 class="text-8xl">Your Courses</h1>
                <RouterLink to="/profile/create-course">
                    <button
                        class="button-confirm mr-40 text-shadow-xl text-xl h-13 w-30 rounded-2xl bg-[#00C11D] cursor-pointer transition hover:bg-[#00E522] active:bg-[#009E18]">Create</button>
                </RouterLink>

            </div>
            <div class="items-center flex flex-col mt-30">
                <p class="text-[#606060] text-2xl">You don't have your own courses yet  :(</p>
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

h1 {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 600;
}

.button-confirm {
    color: white;
}

.button-confirm {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}

p {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
}
</style>