<div class="relative duration-200 h-dvh">
    <img
        class="absolute w-full h-full object-cover transition-all"
        src="/static/public/images/mock/DeathNote-bg.avif"
        alt="/static/public/images/mock/DeathNote-bg.avif"
    />
    <div class="absolute inset-0 bg-gradient-to-r from-secondary/75 to-secondary/50"></div>
    <backdrop class="absolute inset-0 bg-transparent duration-300"></backdrop>

    <div class="absolute inset-0 bottom-[6vw] hidden flex-col items-center justify-center text-center md:flex text-white">
        <span class="text-[0.9vw] font-semibold uppercase leading-none">welcome to</span>
        <div class="mt-[0.75vw] flex items-center leading-none md:text-[1.5vw] font-semibold"> coreproject.moe </div>
        <span class="mt-[2.875vw] max-w-[22vw] text-[1.25vw] font-semibold leading-[1.75vw]"> Bridging the gap between streaming and torrenting sites with a modern and clean interface. </span>
        <span class="mt-[4vw] text-[1vw] font-semibold leading-none"> With a coreproject account, you can </span>
        <span class="mt-[0.5vw] max-w-[22vw] text-[1vw] font-medium leading-[1vw] text-surface-200"> continue on animecore, mangacore and soundcore with same account. </span>
    </div>
    <div class="absolute top-7 md:top-auto md:bottom-[1.85vw] left-7 md:left-[2vw] md:flex">
        <div class="flex flex-col gap-2 md:gap-[0.75vw]">
            <span class="text-[2.25vw] font-semibold uppercase leading-none tracking-widest text-white/75 md:text-[0.75vw]">Background from anime</span>
            <div class="flex items-center gap-[2vw] md:gap-[0.5vw]">
                <span class="text-[3vw] font-bold uppercase leading-none tracking-widest text-warning md:text-[1vw]">
                    <anime-name _="on change(anime_name) put anime_name into me"></anime-name>
                </span>
                <button _="on click trigger hyperscript:change_background">
                    <coreproject-icon-refresh class="w-4 md:w-[1vw]"></coreproject-icon-refresh>
                </button>
            </div>
        </div>
    </div>
</div>