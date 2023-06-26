<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import MessageCircle from "$icons/message_circle.svelte";

    import ImageLoader from "./image/image_loader.svelte";

    export let link: string;
    export let post_banner: string;
    export let post_title: string;
    export let post_description: string;
    export let author: string;
    export let posted_on_date: string;
    export let responses: number;
</script>

<a
    href={link}
    class="card w-full grid-cols-7 overflow-hidden rounded-lg !bg-surface-400 md:grid md:rounded-[0.625vw]"
>
    <post-banner class="col-span-2 h-16 md:h-full md:w-full block">
        <ImageLoader
            src={post_banner}
            alt={post_title}
            class="h-full w-full object-cover object-center"
        />
    </post-banner>

    <post-container class="flex h-36 flex-col justify-between p-3 md:col-span-5 md:h-full md:gap-[0.375vw] md:p-[1vw]">
        <post-head>
            <post-title class="line-clamp-2 text-xs font-extrabold md:text-[0.875vw] md:leading-[1.25vw]">
                {post_title}
            </post-title>
            <post-description class="mt-2 line-clamp-3 text-[0.6rem] font-medium leading-snug text-surface-50 md:mt-[0.5vw] md:line-clamp-2 md:text-[0.75vw] md:leading-[1.125vw]">
                {post_description}
            </post-description>
        </post-head>

        <post-infos class=" flex items-end justify-between text-[0.6rem] leading-none md:mt-[0.75vw] md:items-center md:text-[0.75vw]">
            <post-user-infos class="flex flex-col gap-1 md:flex-row md:items-center md:gap-[0.25vw]">
                <post-author-name>
                    Posted by <span class="text-[0.65rem] font-semibold md:text-[0.85vw]">{author}</span>
                </post-author-name>
                <post-uploaded-date class="text-surface-50">
                    {new FormatDate(posted_on_date).format_to_time_from_now}
                </post-uploaded-date>
            </post-user-infos>

            <post-responses class="flex items-center gap-1 md:gap-[0.25vw]">
                <MessageCircle class="w-3 md:w-[1vw]" />
                <responses-text>{responses}</responses-text>
            </post-responses>
        </post-infos>
    </post-container>
</a>
