<script lang="ts">
    import CoreText from "$icons/CoreText/Index.svelte";
    import Tick from "$icons/Tick/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import { beforeUpdate, createEventDispatcher } from "svelte";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import * as _ from "lodash-es";
    import { z } from "zod";
    import { handle_input } from "../../functions/handle_input";
    import { zxcvbn, zxcvbnOptions, type OptionsType } from "@zxcvbn-ts/core";

    beforeUpdate(async () => {
        const zxcvbnCommonPackage = await import("@zxcvbn-ts/language-common");
        const zxcvbnEnPackage = await import("@zxcvbn-ts/language-en");
        const zxcvbnCsPackage = await import("@zxcvbn-ts/language-cs");
        const zxcvbnDePackage = await import("@zxcvbn-ts/language-de");
        const zxcvbnEsEsPackage = await import("@zxcvbn-ts/language-es-es");
        const zxcvbnFiPackage = await import("@zxcvbn-ts/language-fi");
        const zxcvbnFrPackage = await import("@zxcvbn-ts/language-fr");
        const zxcvbnIdPackage = await import("@zxcvbn-ts/language-id");
        const zxcvbnItPackage = await import("@zxcvbn-ts/language-it");
        const zxcvbnJaPackage = await import("@zxcvbn-ts/language-ja");
        const zxcvbnNlBePackage = await import("@zxcvbn-ts/language-nl-be");
        const zxcvbnPlPackage = await import("@zxcvbn-ts/language-pl");
        const zxcvbnPtBrPackage = await import("@zxcvbn-ts/language-pt-br");

        const options: OptionsType = {
            translations: zxcvbnEnPackage.translations,
            graphs: zxcvbnCommonPackage.adjacencyGraphs,
            dictionary: {
                ...zxcvbnCommonPackage.dictionary,
                ...zxcvbnCsPackage.dictionary,
                ...zxcvbnDePackage.dictionary,
                ...zxcvbnEsEsPackage.dictionary,
                ...zxcvbnFiPackage.dictionary,
                ...zxcvbnFrPackage.dictionary,
                ...zxcvbnIdPackage.dictionary,
                ...zxcvbnItPackage.dictionary,
                ...zxcvbnJaPackage.dictionary,
                ...zxcvbnNlBePackage.dictionary,
                ...zxcvbnPlPackage.dictionary,
                ...zxcvbnPtBrPackage.dictionary,
                ...zxcvbnEnPackage.dictionary,

                // Check inputs
                userInputs: [password.value, email.value, confirm_password.value]
            },
            useLevenshteinDistance: true
        };

        zxcvbnOptions.setOptions(options);
    });

    let email = {
            value: "",
            error: new Array<string>()
        },
        password = {
            value: "",
            error: new Array<string>()
        },
        confirm_password = {
            value: "",
            error: new Array<string>()
        };
    let password_strength = 0;

    const dispatch = createEventDispatcher();

    const password_error_mapping: { [key: string]: string } = {
        atleast_8: "minimum 8 characters",
        missing_one_special_character: "minimum 1 special character",
        missing_one_number: "minimum 1 number",
        missing_one_upper_or_lowercase: "minimum 1 lower-case or upper-case character"
    };

    // Bindings

    function handle_submit() {
        if (password.value === confirm_password.value) {
            dispatch("submit", {
                email: email.value,
                password: password.value
            });
        }
    }

    const handle_email_input = (event: Event) => {
            handle_input({ event: event, schema: z.string().email("Please enter a valid email address"), error_field: email });
        },
        handle_password_input = (event: Event) => {
            handle_input({
                event: event,
                schema: z
                    .string()
                    .min(8, "atleast_8")
                    .refine((val) => /(?=.*[!@#$%^&*()_+|~\-=?;:'",.<>{}[\]\\/])/.test(val), "missing_one_special_character")
                    .refine((val) => /(?=.*\d)/.test(val), "missing_one_number")
                    .refine((val) => /(?=.*[A-Z])|(?=.*[a-z])/.test(val), "missing_one_upper_or_lowercase"),
                error_field: password
            });

            if (password.value) {
                password_strength = zxcvbn(password.value).score;
            } else {
                password_strength = 0;
            }
        },
        handle_confirm_password = (event: Event) => {
            handle_input({
                event: event,
                schema: z.string(),
                error_field: confirm_password
            });
            if (confirm_password.value !== password.value) {
                confirm_password.error = [...confirm_password.error, `**Password** and **Confirm Password** must match`];
            }
        };
</script>

<form
    on:submit|preventDefault={handle_submit}
    class="flex h-full flex-col justify-between"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:gap-[0.5vw] md:text-[1.2vw]">
        <span class="inline-flex gap-2 md:gap-[0.5vw]">
            create your
            <CoreText />
            account
        </span>
        <span class="text-xs font-medium uppercase text-white/90 md:text-[1vw]">unlock the anime world - join us!</span>
    </div>
    <div class="flex flex-col gap-5 md:gap-[1.5vw]">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label
                for="email"
                class="mt-4 text-lg font-semibold leading-none md:mt-[1.1vw] md:text-[1.1vw]"
            >
                Email:
            </label>
            <input
                bind:value={email.value}
                on:input|preventDefault={handle_email_input}
                placeholder="Email address"
                class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if _.isEmpty(email.error) || _.isEmpty(email.value)}
                    <span>we’ll send you a verification email, so please ensure it’s active</span>
                {:else}
                    <span class="text-error">{email.error.join("")}</span>
                {/if}
            </div>
        </div>
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label
                for="password"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                Password:
            </label>
            <input
                bind:value={password.value}
                on:input={handle_password_input}
                placeholder="Password"
                class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex flex-col">
                <div class="grid grid-cols-4 gap-[1.5vw] md:gap-[0.75vw]">
                    {#each Array(4).fill(0) as _}
                        <span class="h-[1.75vw] rounded-[0.5vw] border-white/25 transition-colors md:h-[0.75vw] md:rounded-[0.1875vw] md:border-[0.15vw]"></span>
                    {/each}
                </div>

                <div class="mt-3 md:mt-[1.25vw]">
                    <span class="text-surface-50 text-sm font-semibold uppercase leading-none tracking-wider md:text-[1vw]">must contain</span>

                    <div class="flex flex-col gap-1 md:mt-[0.5vw] md:gap-[0.3vw]">
                        {#each Object.entries(password_error_mapping) as item}
                            {@const key = item[0]}
                            {@const value = item[1]}

                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                {#if (_.isEmpty(password.error) && _.isEmpty(password.value)) || (password.value && password.error.includes(key))}
                                    <Tick class="w-3 text-primary opacity-30 transition-opacity md:w-[1vw]" />
                                {:else}
                                    <!-- Filled tick  -->
                                    <Tick class="w-3 text-primary transition-opacity md:w-[1vw]" />
                                {/if}

                                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.75vw]">{value}</span>
                            </div>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.5vw]">
            <label
                for="confirm-password"
                class="text-lg font-semibold leading-none md:text-[1.1vw]"
            >
                Confirm Password:
            </label>
            <input
                bind:value={confirm_password.value}
                on:input={handle_confirm_password}
                placeholder="Confirm Password"
                class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 text-xs leading-none md:gap-[0.5vw] md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if _.isEmpty(confirm_password.error) || _.isEmpty(confirm_password.value)}
                    <span>Please make sure you enter the same password in both fields</span>
                {:else}
                    <Markdown
                        class="text-error"
                        markdown={confirm_password.error.join("")}
                    />
                {/if}
            </div>
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
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
