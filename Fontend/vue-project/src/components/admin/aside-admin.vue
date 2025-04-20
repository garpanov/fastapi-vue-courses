<script setup lang="ts">

</script>

<template>
    <aside class="wrapper h-screen">
        <div class="py-7 px-8 border-b border-[#101010]">
            <h1 class="text-4xl">Garpanov</h1>
        </div>
        <div class="flex flex-col pt-20 pl-10 gap-10">
            <RouterLink to="/admin">
                <h3 class="text-5xl cursor-pointer hover:scale-101 transition hover:translate-x-1 w-fit">All courses
                </h3>
            </RouterLink>
            <RouterLink to="/admin/confirmation">
                <h3 class="text-5xl cursor-pointer hover:scale-101 transition hover:translate-x-1 w-fit">Confirmation</h3>
            </RouterLink>
        </div>
        <div class="flex justify-between w-full pl-14 pr-20 mt-105 cursor-pointer group">
            <h4 class="text-5xl">Exit</h4>
            <img class="opacity-70 group-hover:opacity-100 group-hover:scale-101 group-hover:translate-x-1 transition"
                src="/profile/arrow.png" alt="arrow">
        </div>
    </aside>
</template>

<style scoped>
.wrapper {
    background-color: black;
    background-size: cover;
    background-position: center;
}

h1,
h3,
h4 {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
}

h3 {
    font-family: "Roboto Slab", serif;
    font-weight: 900;
}

h4 {
    font-family: "Roboto Slab", serif;
    font-weight: 300;
}
</style>