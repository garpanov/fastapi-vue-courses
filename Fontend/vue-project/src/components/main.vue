<script setup lang="ts">
import Header from './header.vue'
import Footer from './footer.vue';
</script>

<template>
    <Header></Header>
    <main>
        <section class="relative page1">
            <img class="absolute z-10" src="../../public/main/neon_page.png" alt="neon_background">

            <h2 class="h2-page1 relative z-40 text-8xl leading-28 pt-20 pl-50 mt-2">Start your
                growth
                with <br>
                Satoshi Study</h2>
            <img class="relative mt-30" src="../../public/main/Hand_left.png" alt="hand_left">
            <div class="relative flex z-40 flex-col ml-45">
                <p class="p-page1 text-3xl">"Innovation distinguishes between a <br> leader and a follower"</p>
                <h3 class="h3-page1 text-3xl ml-80">— Steve Jobs</h3>
            </div>
        </section>

        <section id="home" class="page2 mt-70">
            <div class="flex justify-between">

                <div class="relative group w-full cursor-pointer">
                    <RouterLink to="/courses">
                        <img class="absolute z-10 opacity-100 group-hover:opacity-80 group-hover:-translate-y-2 transition"
                            src="../../public/main/girl_start_developing.png">
                        <div class="relative z-30 mt-140 ml-13">
                            <h2 class="h2-page2 text-7xl">Start developing</h2>
                            <p class="p-page2 opacity-0 group-hover:opacity-100 transition-opacity text-6xl mt-10">Open
                                new
                                paths for yourself <br> through courses</p>
                        </div>
                    </RouterLink>
                </div>

                <div class="relative group w-full cursor-pointer">
                    <img class="absolute z-10 opacity-100 group-hover:opacity-80 group-hover:-translate-y-2 transition"
                        src="../../public/main/mackbook_become_a_guide_.png">
                    <div class="relative z-30 ml-20 mt-20">
                        <h2 class="h2-page2 text-7xl">Become a guide</h2>
                        <p class="p-page2 opacity-0 group-hover:opacity-100 transition-opacity text-6xl mt-10">Create
                            your
                            own courses <br> by consolidating the material</p>
                    </div>

                </div>
            </div>
        </section>

        <section id="about" class="page3 relative mt-70 mb-50">
            <img class="absolute right-130" src="../../public/main/triangle.png">
            <img class="absolute mt-50" src="../../public/main/square.png">
            <img class="absolute bottom-0 right-90" src="../../public/main/semicircle.png">
            <div class="relative place-items-center py-30">
                <h2 class="h2-page3 text-8xl mr-200 mb-30">About</h2>
                <img class="absolute right-0 w-70" src="../../public/main/Hand_right.png">
                <img src="../../public/main/form_about_2.png">
            </div>
        </section>
    </main>
    <Footer></Footer>
</template>


<style scoped>
h2,
.p-page1,
.p-page2,
.h3-page1 {
    color: white;
}

.h2-page1,
.p-page1,
.p-page2 {
    font-family: "Roboto", sans-serif;
    font-weight: 300;
}

.h3-page1 {
    font-family: "Roboto", sans-serif;
    font-weight: 600;
}

.h2-page2 {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}

.h2-page3 {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
}
</style>
