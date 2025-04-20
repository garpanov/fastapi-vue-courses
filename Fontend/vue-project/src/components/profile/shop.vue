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
            <h1 class="text-8xl">Shop</h1>
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
</style>