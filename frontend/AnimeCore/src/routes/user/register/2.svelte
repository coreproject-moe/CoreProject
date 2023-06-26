<script lang="ts">
    import ArrowUpRight from "$icons/arrow_up_right.svelte";
    import Info from "$icons/info.svelte";
    import { ValidationMessage, reporter } from "@felte/reporter-svelte";
    import { validator } from "@felte/validator-zod";
    import { focusTrap } from "@skeletonlabs/skeleton";
    import { createForm } from "felte";
    import { createEventDispatcher } from "svelte";
    import { z } from "zod";

    // Broken
    // See : https://github.com/pablo-abc/felte/issues/223#issuecomment-1510467575
    // Dont remove this unless you know what you are doing
    // Is meant to be a temporary workaround

    const dispatch = createEventDispatcher();

    const schema = z.object({
        username: z.string(),
        otp: z.string()
    });
    const { form } = createForm<z.infer<typeof schema>>({
        initialValues: {
            username: "",
            otp: ""
        },
        onSubmit: async (values) => {
            dispatch("submit", values);
        },
        extend: [reporter, validator({ schema })]
    });
</script>

<form
    class="flex h-max w-full flex-col bg-surface-900 p-10 pb-[10vw] pt-[7vw] md:h-full md:justify-between md:rounded-none md:p-0"
    use:form
    use:focusTrap={true}
>
    <div class="flex flex-col items-start gap-[1.5vw]">
        <form-title>
            <span class="text-base font-bold uppercase tracking-widest md:text-[1.2vw]">choose your username and verify</span>
        </form-title>

        <username-field class="mt-[4vw] w-full">
            <label
                for="username"
                class="text-lg font-semibold md:text-[1.1vw]"
            >
                Username
            </label>
            <input
                name="username"
                placeholder="choose any username"
                class="mt-[0.25vw] h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
            />
            <ValidationMessage
                for="username"
                let:messages={message}
            >
                <span class="mt-[0.75vw] text-xs text-surface-300 md:mt-[0.5vw] md:text-[0.75vw]">{@html message}</span>
                <div slot="placeholder">
                    <info class="mt-[0.75vw] flex items-start gap-2 md:mt-[0.5vw]">
                        <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                        <span class="text-xs text-surface-300 md:text-[0.75vw]">you can change username in your user settings later, so go bonkers!</span>
                    </info>
                </div>
            </ValidationMessage>
        </username-field>

        <otp-field class="mt-2 w-full md:mt-0">
            <label
                for="otp"
                class="text-lg font-semibold md:text-[1.1vw]"
            >
                One Time Verification Code
            </label>
            <input
                name="otp"
                placeholder="enter the code"
                class="mt-[0.25vw] h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
            />
            <ValidationMessage
                for="otp"
                let:messages={message}
            >
                <span class="mt-[0.75vw] text-xs text-surface-300 md:mt-[0.5vw] md:text-[0.75vw]">{@html message}</span>

                <div slot="placeholder">
                    <info class="mt-[0.75vw] flex items-start gap-2 md:mt-[0.5vw]">
                        <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                        <span class="text-xs text-surface-300 md:text-[0.75vw]">if you didn’t receive the code, check your spam folder. Or use the resend button</span>
                    </info>
                </div>
            </ValidationMessage>
        </otp-field>

        <div class="mt-3 flex flex-col items-start md:mt-0">
            <button
                type="button"
                class="btn p-0 text-base font-semibold text-primary-600 underline md:text-[1vw]"
            >
                {@html `< resend code >`}
            </button>
            <button
                type="button"
                class="btn p-0 text-base font-semibold text-primary-600 underline md:text-[1vw]"
            >
                {@html `< change email >`}
            </button>
        </div>
    </div>

    <div class="mt-10 flex items-center justify-between md:mt-0">
        <div class="flex flex-col gap-1 md:gap-0">
            <span class="text-xs text-surface-100 md:text-[0.75vw]">Already have an account?</span>
            <a
                href="./login"
                class="text-base md:text-[1.1vw]"
            >
                Login
            </a>
        </div>
        <button
            type="submit"
            class="btn h-12 rounded-lg bg-secondary-800 p-0 px-5 text-base font-semibold md:h-[2.75vw] md:rounded-[0.5vw] md:px-[1.25vw] md:text-[0.95vw]"
        >
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
