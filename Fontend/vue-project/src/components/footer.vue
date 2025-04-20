<script setup lang="ts">

</script>

<template>
    <footer id="contact" class="mt-20 mb-10">
        <div class="ml-50 mr-25 flex justify-between">
            <div class="mt-10">
                <h3 class="h3-footer mb-3 text-4xl">Contact</h3>
                <p class="p-footer text-xl">Email: fppe980@gmail.com</p>
                <p class="p-footer text-xl">Location: Dnipro, Ukraine</p>
            </div>

            <div class="place-items-center mt-50">
                <div class="flex gap-30">
                    <a href="https://www.instagram.com/sasha_prilep/" target="_blank" rel="noopener noreferrer">
                        <img class="cursor-pointer hover:scale-105 transition" src="../../public/main/Instagram.png"
                            alt="Instagram" />
                    </a>
                    <a href="https://github.com/garpanov" target="_blank" rel="noopener noreferrer">
                        <img class="cursor-pointer hover:scale-105 transition" src="../../public/main/Github.png"
                            alt="Github">
                    </a>
                    <a href="https://t.me/garpanov" target="_blank" rel="noopener noreferrer">
                        <img class="cursor-pointer hover:scale-105 transition" src="../../public/main/Telegram.png"
                            alt="Telegram">
                    </a>
                    <a href="https://discord.com/users/574597793558167552" target="_blank" rel="noopener noreferrer">
                        <img class="cursor-pointer hover:scale-105 transition" src="../../public/main/Discord.png"
                            alt="Discord">
                    </a>
                </div>
            </div>

            <div class="place-items-center">
                <h1 class="h1-footer text-6xl">Satoshi Study.</h1>
                <p class="p-footer mt-50">© Satoshi Study, all rights reserved.</p>

            </div>
        </div>

    </footer>
</template>


<style scoped>
h1,
h3,
p {
  color: white;
}

.h1-footer {
  font-family: "Roboto", sans-serif;
  font-weight: 800;
}

.h3-footer {
  font-family: "Inter", sans-serif;
  font-weight: 500;
}

.p-footer {
  font-family: "Inter", sans-serif;
  font-weight: 400;
}
</style>
