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
    };
</script>

<div>
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
            <div class="h-full md:w-[0.1vw] bg-neutral hover:md:w-[0.15vw] hover:bg-accent cursor-pointer transition-colors" />
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
                <button class="btn min-h-full md:h-max !bg-transparent p-0">
                    <!-- {% include "icons/like.html" with class="w-3 text-surface-300 md:w-[1vw]" %} -->
                    <likes class="text-xs md:text-[0.75vw]">106</likes>
                </button>
                <button class="text-surface-50 btn min-h-full md:h-max !bg-transparent p-0 text-xs uppercase md:text-[0.8vw]">
                    Replay
                </button>
            </div>
        </div>
    </div>
</div>
