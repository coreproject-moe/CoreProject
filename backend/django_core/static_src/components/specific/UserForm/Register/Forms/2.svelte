<script lang="ts">
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import { createEventDispatcher } from "svelte";
    import { z } from "zod";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import { handle_input } from "../../functions/handle_input";
    import _ from "lodash-es";
    import { OTP_LENGTH } from "$constants/otp";
    import { reverse } from "$functions/urls";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { FETCH_TIMEOUT } from "$constants/fetch";

    let form_is_submitable: boolean | null = null;

    const dispatch = createEventDispatcher();

    let username = {
            value: "",
            error: new Array<string>()
        },
        otp = {
            value: "",
            error: new Array<string>()
        };

    function check_if_form_is_submitable() {
        form_is_submitable = [username, otp].every((field) => {
            return field.value && _.isEmpty(field.error);
        });
    }
    // Functions

    const handle_username_input = async (event: Event) => {
            handle_input({
                event: event,
                schema: z
                    .string()
                    .min(4, "**Username** must be at least 4 characters long")
                    .refine((val) => /(?=.*^[a-zA-Z0-9_-]+#[0-9]{4}$)/.test(val), "**Username** is not valid for this regex `^[a-zA-Z0-9_-]+#[0-9]{4}$`"),
                error_field: username
            });

            if (username.value) {
                const res = await fetch(reverse("username-validity-endpoint"), {
                    method: "POST",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        "X-CSRFToken": get_csrf_token()
                    },
                    signal: AbortSignal.timeout(FETCH_TIMEOUT),
                    body: JSON.stringify({
                        username: username.value
                    })
                });

                // 302 = username found
                // 404 = not found

                switch (Number(res.status)) {
                    case 302:
                        username.error = [...username.error, `Username **${username.value}** is already taken`];
                        break;
                    case 404:
                        break;
                    default:
                        throw new Error("Not Implemented");
                }
            }
        },
        handle_otp_input = (event: Event) => {
            handle_input({
                event: event,
                schema: z
                    .string()
                    .refine((val) => /^\d+$/.test(val), "**OTP** must be a number")
                    .refine((val) => new RegExp(`^\\d{${OTP_LENGTH}}$`).test(val), `**OTP** must contain ${OTP_LENGTH} numbers`),
                error_field: otp
            });
        };

    function handle_submit() {
        dispatch("submit", {
            username: username.value,
            otp: otp.value
        });
    }
</script>

<form
    on:submit|preventDefault={handle_submit}
    class="flex h-full flex-col justify-between"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:gap-[0.5vw] md:text-[1.2vw]">
        <span class="text-base font-bold uppercase tracking-widest md:text-[1.2vw]">choose your username and verify</span>
        <span class="text-xs font-medium uppercase text-white/90 md:text-[1vw]">Secure Your Spot in the Anime Community!</span>
    </div>
    <div class="flex flex-col gap-5 md:gap-[1.5vw]">
        <div class="flex w-full flex-col gap-[0.3rem] md:gap-[0.35vw]">
            <label
                for="username"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                Username:
            </label>
            <input
                bind:value={username.value}
                on:input|preventDefault={handle_username_input}
                on:input={check_if_form_is_submitable}
                name="username"
                placeholder="Username eg: sora#4444"
                class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="text-surface-300 flex items-start gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if !_.isEmpty(username.error)}
                    <Markdown
                        class="text-error"
                        markdown={username.error.join("")}
                    />
                {:else}
                    <span>you can change username in your user settings later, so go bonkers!</span>
                {/if}
            </div>
        </div>
        <div class="flex w-full flex-col gap-[0.3rem] md:gap-[0.35vw]">
            <label
                for="otp"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                OTP:
            </label>
            <input
                bind:value={otp.value}
                on:input={handle_otp_input}
                on:input={check_if_form_is_submitable}
                name="otp"
                placeholder="One Time Password"
                class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="text-surface-300 flex items-start gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if !_.isEmpty(otp.error)}
                    <Markdown
                        class="text-error"
                        markdown={otp.error.join("")}
                    />
                {:else}
                    <span>if you didn’t receive the code, check your spam folder. Or use the resend button</span>
                {/if}
            </div>
        </div>
        <div class="mt-3 flex flex-col items-start gap-2 md:mt-0 md:gap-[0.5vw]">
            {#each [`< resend code >`, `< change email >`] as item}
                <button class="btn btn-secondary flex h-max min-h-max flex-col items-start p-0 text-base font-semibold leading-none text-primary underline md:text-[1vw]">{item}</button>
            {/each}
        </div>
    </div>
    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Already have an account?</span>
            <button class="text-start text-base leading-none text-primary underline md:text-[1.1vw]">Login</button>
        </div>
        <button
            type="submit"
            class:btn-disabled={!form_is_submitable}
            class="btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.5vw] md:p-[1vw] md:text-[0.95vw]"
        >
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
