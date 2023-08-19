<script lang="ts">
    import ArrowUpRight from "$icons/arrow_up_right.svelte";
    import Cross from "$icons/cross.svelte";
    import Info from "$icons/info.svelte";
    import Tick from "$icons/tick.svelte";
    import { ValidationMessage, reporter } from "@felte/reporter-svelte";
    import { validator } from "@felte/validator-zod";
    import { focusTrap } from "@skeletonlabs/skeleton";
    import { zxcvbn, zxcvbnOptions } from "@zxcvbn-ts/core";
    import * as zxcvbnCommonPackage from "@zxcvbn-ts/language-common";
    import * as zxcvbnEnPackage from "@zxcvbn-ts/language-en";
    import { createForm } from "felte";
    import { createEventDispatcher } from "svelte";
    import { z } from "zod";

    let password_strength = 0;

    const options = {
        dictionary: {
            ...zxcvbnCommonPackage.dictionary,
            ...zxcvbnEnPackage.dictionary
        }
    };

    zxcvbnOptions.setOptions(options);

    // Broken
    // See : https://github.com/pablo-abc/felte/issues/223#issuecomment-1510467575
    // Dont remove this unless you know what you are doing
    // Is meant to be a temporary workaround

    const dispatch = createEventDispatcher();

    const schema = z
        .object({
            email: z.string().email("Please enter a valid email address"),

            password: z
                .string()
                .min(8, "atleast_8")
                .refine((val) => /(?=.*[!@#$%^&*()_+|~\-=?;:'",.<>{}[\]\\/])/.test(val), "missing_one_special_character")
                .refine((val) => /(?=.*\d)/.test(val), "missing_one_number")
                .refine((val) => /(?=.*[A-Z])|(?=.*[a-z])/.test(val), "missing_one_upper_or_lowercase"),

            confirm_password: z.string()
        })
        .superRefine(({ password, confirm_password }, ctx) => {
            if (confirm_password !== password) {
                ctx.addIssue({
                    code: z.ZodIssueCode.custom,
                    message: "<b>Password</b> and <b>Confirm Password</b> doesn't match",
                    path: ["confirm_password"]
                });
            }
        });

    const { form, errors, data, touched } = createForm<z.infer<typeof schema>>({
        initialValues: {
            email: "",
            password: "",
            confirm_password: ""
        },
        onSubmit: async (values) => {
            dispatch("submit", values);
        },
        extend: [reporter, validator({ schema })],
        validate: (values) => {
            // Configure ZXCVBN
            if (values.password) {
                password_strength = zxcvbn(values.password).score;
            } else {
                password_strength = 0;
            }

            return undefined;
        }
    });

    const password_error_mapping: { [key: string]: string } = {
        atleast_8: "minimum 8 characters",
        missing_one_special_character: "minimum 1 special character",
        missing_one_number: "minimum 1 number",
        missing_one_upper_or_lowercase: "minimum 1 lower-case or upper-case character"
    };

    const core_color_mapping: { [key: string]: string } = {
        c: "text-surface-50",
        e: "text-surface-50",
        o: "text-warning-400",
        r: "text-surface-50"
    };
</script>

<form
    class="flex h-max w-full flex-col bg-surface-900 p-10 pb-[10vw] pt-[7vw] md:h-full md:justify-between md:rounded-none md:p-0"
    method="POST"
    use:form
    use:focusTrap={true}
>
    <form-fields>
        <div class="flex gap-2 whitespace-nowrap pb-10 font-bold uppercase leading-none tracking-widest text-white md:pb-[1.8vw] md:text-[1.2vw]">
            <p>create your</p>
            <p class="">
                {#each "core".split("") as item}
                    <span class={core_color_mapping[item]}>{item}</span>
                {/each}
            </p>
            <p>account</p>
        </div>
        <email-field class="flex flex-col gap-[0.3rem] md:gap-[0.75vw]">
            <label
                for="email"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                Email
            </label>
            <input
                name="email"
                id="email"
                placeholder="sora@coreproject.moe"
                class="h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
            />

            <ValidationMessage
                for="email"
                let:messages={message}
            >
                <span class="mt-[0.75vw] text-xs leading-none text-surface-300 md:mt-0 md:text-[0.75vw]">{@html message}</span>
                <div slot="placeholder">
                    <info class="flex items-center gap-2 md:gap-[0.5vw]">
                        <Info class="w-3 opacity-70 md:w-[0.75vw]" />
                        <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">we’ll send you a verification email, so please ensure it’s active</span>
                    </info>
                </div>
            </ValidationMessage>
        </email-field>

        <password-field>
            <label
                for="password"
                class="mt-4 text-lg font-semibold leading-none md:mt-[1.1vw] md:text-[1.1vw]"
            >
                Password
            </label>
            <input
                type="password"
                id="password"
                name="password"
                placeholder="enter a strong password"
                class="mt-[0.3rem] h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:mt-[0.7vw] md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
            />
            <password-strength class="mt-2 flex flex-col md:mt-[1vw]">
                <div class="grid grid-cols-4 gap-[1.5vw] md:gap-[0.75vw]">
                    {#each Array(password_strength) as _, index}
                        {@const backgrounds = ["bg-primary-800", "bg-primary-700", "bg-primary-600", "bg-primary-500"]}
                        <span class="{backgrounds[index]} col-span-1 h-[1.75vw] w-full rounded-[0.5vw] md:h-[0.625vw] md:rounded-[0.1875vw]" />
                    {/each}
                    {#each Array(4 - password_strength) as _}
                        <span class="col-span-1 h-[1.75vw] w-full rounded-[0.5vw] border-[0.4vw] border-primary-50/50 md:h-[0.625vw] md:rounded-[0.1875vw] md:border-[0.2vw]" />
                    {/each}
                </div>

                <div class="mt-3 md:mt-[1.25vw]">
                    <span class="text-sm font-semibold uppercase leading-none tracking-wider text-surface-50 md:text-[1vw]">must contain</span>
                    <div class="ml-2 mt-[0.4vw] flex flex-col gap-[0.1vw] md:w-3/5">
                        <ValidationMessage
                            for="password"
                            let:messages
                        >
                            <!-- So we get an array of items  -->
                            {#if Array.isArray(messages)}
                                <!-- Logics for cross and ticks -->
                                <div class="flex flex-col gap-1 md:gap-[0.3vw]">
                                    {#each Object.entries(password_error_mapping) as item}
                                        {@const object_key = item[0]}
                                        {@const object_value = item[1]}

                                        <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                            {#if messages.includes(object_key)}
                                                <div class="w-3 text-red-500 opacity-80 md:w-[0.9vw]">
                                                    <svelte:component this={Cross} />
                                                </div>
                                            {:else}
                                                <div class="w-3 text-primary-400 opacity-90 md:w-[0.7vw]">
                                                    <svelte:component this={Tick} />
                                                </div>
                                            {/if}
                                            <span class="col-span-11 w-max text-xs leading-none text-surface-300 md:text-[0.75vw]">{object_value}</span>
                                        </div>
                                    {/each}
                                </div>
                            {/if}
                            <div slot="placeholder">
                                <div class="flex flex-col gap-1 md:gap-[0.3vw]">
                                    {#each Object.values(password_error_mapping) as item}
                                        <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                            {#if $data.password && !$errors.password && $touched.password}
                                                <div class="w-3 text-primary-400 opacity-90 md:w-[0.7vw]">
                                                    <svelte:component this={Tick} />
                                                </div>
                                            {:else}
                                                <div class="w-3 text-red-500 opacity-80 md:w-[0.9vw]">
                                                    <svelte:component this={Cross} />
                                                </div>
                                            {/if}
                                            <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">{item}</span>
                                        </div>
                                    {/each}
                                </div>
                            </div>
                        </ValidationMessage>
                    </div>
                </div>
            </password-strength>
        </password-field>

        <confirm-password-field>
            <label
                for="confirm-password"
                class="mt-4 text-lg font-semibold leading-none md:mt-[2.2vw] md:text-[1.1vw]"
            >
                Confirm Password
            </label>
            <div class="relative flex flex-col md:mt-[0.7vw]">
                <input
                    type="password"
                    id="confirm_password"
                    name="confirm_password"
                    placeholder="re-enter your password"
                    class="mt-[0.3rem] h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:mt-0 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
                />
                <ValidationMessage
                    for="confirm_password"
                    let:messages={message}
                >
                    <span class="mt-2 text-xs leading-none text-surface-300 md:mt-[0.5vw] md:text-[0.75vw]">{@html message}</span>
                    <div slot="placeholder" />
                </ValidationMessage>
            </div>
        </confirm-password-field>
    </form-fields>

    <div class="mt-11 flex items-center justify-between md:mt-0">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-xs text-surface-100 md:text-[0.75vw]">Already have an account?</span>
            <a
                href="./login"
                class="text-base leading-none md:text-[1.1vw]"
            >
                Login
            </a>
        </div>
        <button
            type="submit"
            class="btn h-12 rounded-lg bg-secondary-800 p-0 px-5 text-base font-semibold leading-none md:h-[2.75vw] md:rounded-[0.5vw] md:px-[1.25vw] md:text-[0.95vw]"
        >
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
