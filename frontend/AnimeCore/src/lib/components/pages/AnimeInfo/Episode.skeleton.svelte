<div
    class="flex justify-between items-center md:items-start gap-3 flex-col md:flex-row animate-pulse w-full"
>
    <div class="flex w-full flex-col">
        <div class="flex">
            <div>
                <div class="flex gap-1">
                    <h1 class="font-bond text-lg text-white">
                        <button class="btn btn-square btn-sm w-14" />
                    </h1>
                    <button class="btn btn-square btn-sm " />
                </div>
                <episode-and-dub-container class="flex gap-4 mt-12">
                    <div class="flex gap-3">
                        <p class="font-bold flex gap-2 justify-center items-center">
                            <span class="text-3xl">
                                <button class="btn btn-square btn-sm" />
                            </span>
                            <span><button class="btn btn-square btn-sm w-14" /></span>
                        </p>
                        <div class="text-zinc-500 flex justify-center items-center">▪</div>
                        <div class="flex justify-center items-center">
                            <div class="flex flex-col gap-2">
                                <span class="text-white">
                                    <button class="btn btn-square btn-sm w-20" />
                                </span>
                                <span class="flex gap-3">
                                    {#each Array(2) as _}
                                        <span
                                            class="badge bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                        />
                                    {/each}
                                </span>
                            </div>
                        </div>
                        <div class="text-zinc-500 flex justify-center items-center">▪</div>
                        <div class="flex justify-center items-center gap-3">
                            {#each Array(3) as _}
                                <span
                                    class="badge bg-[#1E2036] badge-lg rounded-md border-transparent leading-6 text-sm font-bold capitalize"
                                />
                            {/each}
                        </div>
                    </div>
                </episode-and-dub-container>
            </div>
            <div class="flex w-full justify-end">
                <div class="flex justify-center gap-5">
                    <div class="flex flex-col w-[135px]">
                        <span><button class="btn btn-square btn-xs w-14" /></span>
                        <select class="select w-full bg-neutral" />
                    </div>
                    <div class="flex flex-col w-[135px]">
                        <span><button class="btn btn-square btn-xs w-14" /></span>
                        <select class="select w-full bg-neutral" />
                    </div>
                    <div class="flex translate-y-8">
                        <button class="btn btn-square" />
                    </div>
                </div>
            </div>
        </div>
        <div class="grid gap-x-20 gap-y-10 grid-cols-3 mt-10">
            {#each Array(9) as _}
                <episode-card-container class="flex flex-col gap-4">
                    <episode-card class="grid w-80 h-52 rounded-2xl relative">
                        <episode-card-background-image
                            class="w-80 h-52 rounded-2xl absolute inset-0 z-0 bg-[#1E2036]"
                        />
                        <episode-card-background-gradient
                            class="w-80 h-52 rounded-2xl absolute inset-0 z-10"
                        />
                        <episode-card-info
                            class="w-80 h-52 rounded-2xl absolute inset-0 z-20 font-bold"
                        />
                    </episode-card>
                    <episode-name class="text-zinc-200 text-center bg-[#1E2036]" />
                </episode-card-container>
            {/each}
        </div>
    </div>
</div>
