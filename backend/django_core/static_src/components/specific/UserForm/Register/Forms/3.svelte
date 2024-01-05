<script lang="ts">
    import CoreText from "$icons/CoreText/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";

    export let pages_state: [{ email: string }, { username: string }];

    const combined_state = Object.assign({}, ...pages_state);
</script>

<form
    on:submit|preventDefault
    class="flex h-full flex-col justify-between"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:gap-[0.5vw] md:text-[1.2vw]">
        <span class="flex items-center text-base font-bold uppercase tracking-widest text-white md:text-[1.2vw]">
            welcome to&nbsp;
            <CoreText />
            project
        </span>
        <span class="text-xs font-medium uppercase text-white/90 md:text-[1vw]">Your Anime Sanctuary Awaits!</span>
    </div>
    <div class="flex flex-col items-start gap-5 md:gap-[3vw]">
        <div class="flex flex-col md:gap-[1.5vw]">
            <span class="text-primary-500 text-lg font-semibold leading-none md:text-[1.5vw]">Account Summary</span>
            <div class="flex flex-col md:gap-[0.5vw]">
                <span class="text-lg font-medium leading-none md:text-[1.1vw]">Username:</span>
                <span class="text-base font-medium leading-none text-accent md:text-[1.1vw]">
                    {combined_state.username}
                </span>
            </div>
            <div class="flex flex-col md:gap-[0.5vw]">
                <span class="text-lg font-medium leading-none md:text-[1.1vw]">Email:</span>
                <span class="text-base font-medium leading-none text-accent md:text-[1.1vw]">
                    {combined_state.email}
                </span>
            </div>
        </div>
        <div class="mt-3 flex flex-col items-start gap-2 md:mt-0 md:gap-[0.5vw]">
            <button class="btn btn-secondary flex h-max min-h-max flex-col items-start p-0 text-base font-semibold leading-none text-primary underline md:text-[1vw]">&lt; resend code &gt;</button>
            <button class="btn btn-secondary flex h-max min-h-max flex-col items-start p-0 text-base font-semibold leading-none text-primary underline md:text-[1vw]">&lt; change email &gt;</button>
        </div>
    </div>
    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Already have an account?</span>
            <button class="text-start text-base leading-none text-primary underline md:text-[1.1vw]">Login</button>
        </div>
        <button
            type="submit"
            class="btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.5vw] md:p-[1vw] md:text-[0.95vw]"
        >
            <span>Finish</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
