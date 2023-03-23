<script lang="typescript">
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

{#if mobile}
    <div class="mt-10 flex w-full animate-pulse flex-col text-white md:mt-0">
        <span class="text-2xl font-bold">Episodes</span>
        <div class="divider before:bg-white after:bg-white" />
        <div class="flex justify-between">
            <div class="btn-wide btn-square btn-sm btn flex text-xl font-bold" />
            <div class="flex gap-4">
                <div class="btn-square btn-sm btn" />
                <div class="btn-square btn-sm btn" />
            </div>
        </div>
        {#each Array(9) as item}
            <div class="relative my-4 flex h-16 w-[90vw] items-center rounded-lg bg-[#1E2036]" />
        {/each}
    </div>
{:else}
    <div
        class="flex w-full animate-pulse flex-col items-center justify-between gap-3 md:flex-row md:items-start"
    >
        <div class="flex w-full flex-col">
            <div class="flex">
                <div>
                    <div class="flex gap-1">
                        <h1 class="font-bond text-lg text-white">
                            <button class="btn-square btn-sm btn w-14" />
                        </h1>
                        <button class="btn-square btn-sm btn " />
                    </div>
                    <episode-and-dub-container class="mt-12 flex gap-4">
                        <div class="flex gap-3">
                            <p class="flex items-center justify-center gap-2 font-bold">
                                <span class="text-3xl">
                                    <button class="btn-square btn-sm btn" />
                                </span>
                                <span><button class="btn-square btn-sm btn w-14" /></span>
                            </p>
                            <div class="flex items-center justify-center text-zinc-500">▪</div>
                            <div class="flex items-center justify-center">
                                <div class="flex flex-col gap-2">
                                    <span class="text-white">
                                        <button class="btn-square btn-sm btn w-20" />
                                    </span>
                                    <span class="flex gap-3">
                                        {#each Array(2) as _}
                                            <span
                                                class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6"
                                            />
                                        {/each}
                                    </span>
                                </div>
                            </div>
                            <div class="flex items-center justify-center text-zinc-500">▪</div>
                            <div class="flex items-center justify-center gap-3">
                                {#each Array(3) as _}
                                    <span
                                        class="badge badge-lg rounded-md border-transparent bg-[#1E2036] text-sm font-bold capitalize leading-6"
                                    />
                                {/each}
                            </div>
                        </div>
                    </episode-and-dub-container>
                </div>
                <div class="flex w-full justify-end">
                    <div class="flex justify-center gap-5">
                        <div class="flex w-[135px] flex-col">
                            <span><button class="btn-square btn-xs btn w-14" /></span>
                            <select class="select w-full bg-neutral" />
                        </div>
                        <div class="flex w-[135px] flex-col">
                            <span><button class="btn-square btn-xs btn w-14" /></span>
                            <select class="select w-full bg-neutral" />
                        </div>
                        <div class="flex translate-y-8">
                            <button class="btn-square btn" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="mt-10 grid grid-cols-3 gap-x-20 gap-y-10">
                {#each Array(9) as _}
                    <episode-card-container class="flex flex-col gap-4">
                        <episode-card class="relative grid h-52 w-80 rounded-2xl">
                            <episode-card-background-image
                                class="absolute inset-0 z-0 h-52 w-80 rounded-2xl bg-[#1E2036]"
                            />
                            <episode-card-background-gradient
                                class="absolute inset-0 z-10 h-52 w-80 rounded-2xl"
                            />
                            <episode-card-info
                                class="absolute inset-0 z-20 h-52 w-80 rounded-2xl font-bold"
                            />
                        </episode-card>
                        <episode-name class="bg-[#1E2036] text-center text-zinc-200" />
                    </episode-card-container>
                {/each}
            </div>
        </div>
    </div>
{/if}
