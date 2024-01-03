<script lang="ts">
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import { createEventDispatcher } from "svelte";
    import * as z from "zod";
    import Markdown from "$components/minor/Markdown/Index.svelte";

    const dispatch = createEventDispatcher();
    const OTP_LENGTH = 5;

    let form_data = {
        username: "",
        otp: "",
    }, form_errors: {
        username?: string;
        otp?: string;
    } = {};

    const schema = z.object({
        username: z.string()
            .min(1, "Username can't be empty")
            .refine((val) => /(?=.*^[a-zA-Z0-9_-]+#[0-9]{4}$)/.test(val), "Username is not valid for this regex `^[a-zA-Z0-9_-]+#[0-9]{4}$`"),

        otp: z.string()
            .refine((val) => /^\d+$/.test(val), "OTP must be a number")
            .refine((val) => new RegExp(`^\\d{${OTP_LENGTH}}$`).test(val), `OTP must contain ${OTP_LENGTH} numbers`),
    });

    // Functions
    function validateZod() {
        try {
            schema.parse(form_data);
            // if valid
            form_errors = {};
        } catch (err) {
            if (err instanceof z.ZodError) {
                form_errors = err.flatten().fieldErrors;
            }
        }
    }

    // Bindings
    function handleInput() {
        validateZod();
    }

    function handleSubmit() {
        validateZod();

        if (Object.values(form_errors).some((err) => err)) return;
        dispatch("submit", {
            username: form_data.username,
            otp: form_data.otp
        });
    }
</script>

<form
    on:submit|preventDefault={handleSubmit}
    class="flex flex-col justify-between h-full"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:text-[1.2vw] md:gap-[0.5vw]">
        <span class="text-base font-bold uppercase tracking-widest md:text-[1.2vw]">choose your username and verify</span>
        <span class="uppercase text-xs md:text-[1vw] font-medium text-white/90">Secure Your Spot in the Anime Community!</span>
    </div>
    <div class="flex flex-col gap-5 md:gap-[1.5vw]">
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.35vw] w-full">
            <label for="username" class="text-lg font-semibold md:text-[1.1vw] leading-none">
                Username:
            </label>
            <input
                bind:value={form_data.username}
                on:input={handleInput}
                name="username"
                placeholder="Username eg: sora#4444"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-start gap-2 md:gap-[0.5vw] text-xs text-surface-300 md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if form_errors.username}
                    <span class="text-error">{form_errors.username[0]}</span>
                {:else}
                    <span>you can change username in your user settings later, so go bonkers!</span>
                {/if}
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.35vw] w-full">
            <label for="otp" class="text-lg font-semibold md:text-[1.1vw] leading-none">
                OTP:
            </label>
            <input
                bind:value={form_data.otp}
                on:input={handleInput}
                name="otp"
                placeholder="One Time Password"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-start gap-2 md:gap-[0.5vw] text-xs text-surface-300 md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if form_errors.otp}
                    <span class="text-error">{form_errors.otp[0]}</span>
                {:else}
                    <span>if you didn’t receive the code, check your spam folder. Or use the resend button</span>
                {/if}
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
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
