<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import Markdown from "$components/minor/Markdown/Index.svelte";

    export let item: {
        created_at: string;
        user: {
            username: string;
            first_name: string;
            last_name: string;
            avatar: null | string;
            avatar_url: string;
        };
        text: string;
        path: string;
        children: number;
    };

    const comment_level = item.path.split(".").length; // this might help later

    // Object.entries(item).forEach(([key, obj]) => {
    //     if (typeof obj === "object" && key !== "user") {
    //         console.log()
    //     }
    // })
</script>

<div class="flex gap-3 md:gap-[0.75vw]">
    <div class="flex flex-col items-center md:gap-[1vw]">
        <a
            href="/user/"
            class="h-7 w-7 flex-shrink-0 md:h-[2vw] md:w-[2vw]"
        >
            <img
                alt=""
                src={item.user.avatar ?? item.user.avatar_url}
                class="h-full w-full shrink-0 rounded-full object-cover"
            />
        </a>
        <button class="h-full md:w-full flex justify-center group cursor-pointer active:scale-95 transition-transform">
            <div class="bg-neutral rounded-full md:w-[0.15vw] h-full group-hover:md:w-[0.2vw] group-hover:bg-warning transition-colors" />
        </button>
    </div>
    <div class="flex flex-col items-start gap-1 md:gap-[0.25vw]">
        <a
            href="/user/"
            class="flex flex-col text-xs leading-none md:text-[1vw]"
        >
            <div class="flex items-center md:gap-[0.5vw]">
                <div class="text-white">{`${item.user.first_name} ${item.user.last_name}`}</div>
                <div class="md:text-[0.75vw]">{item.user.username}</div>
            </div>
            <div class="text-surface-300 md:text-[0.75vw] md:leading-[1.5vw]">{new FormatDate(item.created_at).format_to_time_from_now}</div>
        </a>
        <div class="text-sm leading-snug text-accent md:text-[1vw] md:leading-[1.5vw]">
            <Markdown markdown={item.text} />
        </div>
        <div class="flex items-center gap-3 md:gap-[0.75vw]">
            <div class="flex items-center md:gap-[0.35vw]">
                <button class="btn md:h-max min-h-full btn-secondary p-0">
                    <coreproject-icon-arrow
                        class="md:w-[1.25vw]"
                        variant="outline"
                    ></coreproject-icon-arrow>
                </button>
                <span class="md:text-[0.9vw] font-semibold text-accent">106</span>
                <button class="btn md:h-max min-h-full btn-secondary p-0">
                    <coreproject-icon-arrow
                        class="md:w-[1.25vw] rotate-90"
                        variant="outline"
                    ></coreproject-icon-arrow>
                </button>
            </div>
            <button class="btn min-h-full md:h-max !bg-transparent p-0 text-xs md:text-[0.9vw] md:gap-[0.35vw]">
                <coreproject-icon-chat class="md:w-[1vw]"></coreproject-icon-chat>
                <span>Replay</span>
            </button>
            <button class="btn min-h-full md:h-max !bg-transparent p-0 text-xs md:text-[0.9vw] md:gap-[0.35vw]">
                <coreproject-icon-share class="md:w-[1vw]"></coreproject-icon-share>
                <span>Share</span>
            </button>
            <div class="dropdown">
                <div tabindex="0" role="button" class="btn btn-secondary p-0 h-max min-h-max md:gap-[0.15vw]">
                    <coreproject-icon-dot class="md:w-[0.2vw]"></coreproject-icon-dot>
                    <coreproject-icon-dot class="md:w-[0.2vw]"></coreproject-icon-dot>
                    <coreproject-icon-dot class="md:w-[0.2vw]"></coreproject-icon-dot>
                </div>
                <ul class="dropdown-content z-10 bg-neutral md:rounded-[0.25vw] overflow-hidden">
                    <li class="md:py-[0.5vw] md:px-[1vw] md:text-[1vw] hover:bg-primary hover:text-accent transition-colors cursor-pointer">
                        <span>Report</span>
                    </li>
                </ul>
            </div>
        </div>

        <!-- Render replies here -->
        {#if item.children !== 0}
            <div class="flex flex-col md:gap-[1.5vw] md:mt-[1.5vw]">
                {#each Object.entries(item) as [key, obj]}
                    <!-- Avoid user object -->
                    {#if typeof obj === "object" && key !== "user"}
                        <svelte:self item={obj} />
                    {/if}
                {/each}
            </div>
        {/if}
    </div>
</div>

{#if item.children > 1}
    <div class="flex items-end md:gap-[0.5vw] md:ml-[0.55vw]">
        <svg class="md:w-[2vw] text-neutral" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 15 15"><path fill="currentColor" fill-rule="evenodd" d="M9.877 12H11.5a.5.5 0 0 0 0-1H9.9c-1.128 0-1.945 0-2.586-.053c-.637-.052-1.057-.152-1.403-.328a3.5 3.5 0 0 1-1.53-1.53c-.176-.346-.276-.766-.328-1.403C4 7.045 4 6.228 4 5.1V3.5a.5.5 0 0 0-1 0v1.623c0 1.1 0 1.958.056 2.645c.057.698.175 1.265.434 1.775a4.5 4.5 0 0 0 1.967 1.967c.51.26 1.077.377 1.775.434C7.92 12 8.776 12 9.877 12Z" clip-rule="evenodd"/></svg>

        <button class="btn btn-secondary p-0 h-max min-h-max flex items-center md:gap-[0.75vw]">
            <div class="rotate-45 bg-neutral md:w-[1.5vw] md:h-[1.5vw] rounded-full grid place-items-center">
                <coreproject-icon-cross class="md:w-[1vw] text-accent p-0"></coreproject-icon-cross>
            </div>
            <span class="md:text-[1vw]">{item.children - 1} More</span>
        </button>
    </div>
{/if}
