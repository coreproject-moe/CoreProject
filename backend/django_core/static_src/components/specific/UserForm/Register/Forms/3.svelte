<script lang="ts">
    import CoreText from "$icons/CoreText/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
</script>

<form
    on:submit|preventDefault
    class="flex flex-col justify-between h-full"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:text-[1.2vw] md:gap-[0.5vw]">
        <span class="flex items-center text-base font-bold uppercase tracking-widest text-white md:text-[1.2vw]">
            welcome to&nbsp;
            <CoreText />
            project
        </span>
        <span class="uppercase text-xs md:text-[1vw] font-medium text-white/90">Your Anime Sanctuary Awaits!</span>
    </div>
    <div class="flex flex-col gap-5 items-start md:gap-[3vw]">
        <div class="flex flex-col md:gap-[1.5vw]">
            <span class="text-lg font-semibold text-primary-500 md:text-[1.5vw] leading-none">Account Summary</span>
            <div class="flex flex-col md:gap-[0.5vw]">
                <span class="text-lg font-medium md:text-[1.1vw] leading-none">Username:</span>
                <span class="text-base font-medium text-accent md:text-[1.1vw] leading-none">
                    dummy username
                </span>
            </div>
            <div class="flex flex-col md:gap-[0.5vw]">
                <span class="text-lg font-medium md:text-[1.1vw] leading-none">Email:</span>
                <span class="text-base font-medium text-accent md:text-[1.1vw] leading-none">
                    dummy email
                </span>
            </div>
        </div>
        <div class="mt-3 flex flex-col gap-2 md:gap-[0.5vw] items-start md:mt-0">
            <button class="btn btn-secondary p-0 h-max min-h-max text-base font-semibold leading-none text-primary underline md:text-[1vw] flex flex-col items-start">
                &lt; resend code &gt;
            </button>
            <button class="btn btn-secondary p-0 h-max min-h-max text-base font-semibold leading-none text-primary underline md:text-[1vw] flex flex-col items-start">
                &lt; change email &gt;
            </button>
        </div>
    </div>
    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-xs leading-none text-surface-100 md:text-[0.75vw]">Already have an account?</span>
            <button
                class="text-start text-base leading-none md:text-[1.1vw] text-primary underline"
            >
                Login
            </button>
        </div>
        <button
            type="submit"
            class="btn btn-primary text-accent rounded-lg text-base font-semibold md:rounded-[0.5vw] md:text-[0.95vw] leading-none h-max min-h-max md:p-[1vw] p-4"
        >
            <span>Finish</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
