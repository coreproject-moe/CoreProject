<script lang="ts">
    import Navbar from "$components/specific/Navbar/Index.svelte";
    import CoreProjectIcon from "$icons/CoreProject/Index.svelte";
    import CoreProjectText from "$icons/CoreProjectText/Index.svelte";
    import Search from "$icons/Search/Index.svelte";
</script>

<div class="bg-secondary min-h-dvh w-screen overflow-x-hidden">
    <navbar class="absolute inset-x-0 top-0 flex h-[4.5rem] items-center justify-between bg-secondary/95 p-3 backdrop-blur-3xl md:static md:h-[8.5vh] md:bg-secondary md:p-[1vw]">
        <a href="/">
            <CoreProjectIcon class="w-9 md:w-[2.25vw] md:pt-[0.75vw]" />
        </a>
        <div class="relative flex items-center md:static">
            <div class="absolute left-1/2 -translate-x-1/2">
                <a href="/anime" class="hidden md:flex">
                    <CoreProjectText class="!text-[1.75vw] !m-0" />
                </a>
                <form class="relative flex h-12 w-[65vw] items-center md:hidden">
                    <button class="btn absolute left-4 p-0 !bg-transparent border-none" aria-label="Search">
                        <Search class="w-5 text-neutral-content/75" />
                    </button>
                    <input
                        type="text"
                        placeholder="Search for animes, mangas..."
                        class="h-full w-full rounded-lg border-none bg-neutral/75 pl-12 text-base font-semibold text-accent shadow-lg !ring-0 placeholder:font-medium placeholder:text-surface-200"
                    />
                </form>
            </div>
        </div>
        <Navbar />
    </navbar>
</div>
