<script lang="ts">
    import CoreText from "$icons/CoreText/Index.svelte";
    import Tick from "$icons/Tick/Index.svelte";
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import { createEventDispatcher } from "svelte";
    import z from "zod";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import * as  _ from "lodash-es";

    let form_data = {
        email: "",
        password: "",
        confirm_password: ""
    }, form_errors: {
        email?: string[],
        password?: string[],
        confirm_password?: string[]
    } = {};

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
            if (!_.isEqual(password, confirm_password)) {
                ctx.addIssue({
                    code: z.ZodIssueCode.custom,
                    message: "<b>Password</b> and <b>Confirm Password</b> must be same",
                    path: ["confirm_password"]
                });
            }
        });

    const password_error_mapping: { [key: string]: string } = {
        atleast_8: "minimum 8 characters",
        missing_one_special_character: "minimum 1 special character",
        missing_one_number: "minimum 1 number",
        missing_one_upper_or_lowercase: "minimum 1 lower-case or upper-case character"
    };

    // Functions
    function validateZod() {
        try {
            schema.parse(form_data);
            // clear errors if valid
            form_errors = {};
        } catch (err) {
            if (err instanceof z.ZodError) {
                form_errors = err.flatten().fieldErrors;
                // console.log(err.flatten().fieldErrors);
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
            email: form_data.email,
            password: form_data.password,
            confirm_password: form_data.confirm_password
        });
    }
</script>

<form
    on:submit|preventDefault={handleSubmit}
    class="flex flex-col justify-between h-full"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:text-[1.2vw] md:gap-[0.5vw]">
        <span class="inline-flex gap-2 md:gap-[0.5vw]">
            create your
            <CoreText />
            account
        </span>
        <span class="uppercase text-xs md:text-[1vw] font-medium text-white/90">unlock the anime world - join us!</span>
    </div>
    <div class="flex flex-col gap-5 md:gap-[1.5vw]">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label for="email" class="mt-4 text-lg font-semibold leading-none md:mt-[1.1vw] md:text-[1.1vw]">
                Email:
            </label>
            <input
                bind:value={form_data.email}
                on:input={handleInput}
                name="email"
                placeholder="Email address"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 md:gap-[0.5vw] leading-none text-xs md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if form_errors.email}
                    <span>{form_errors.email[0]}</span>
                {:else}
                    <span>we’ll send you a verification email, so please ensure it’s active</span>
                {/if}
            </div>
        </div>
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label for="password" class="text-lg font-semibold leading-none md:text-[1.1vw]">
                Password:
            </label>
            <input
                bind:value={form_data.password}
                on:input={handleInput}
                name="password"
                placeholder="Password"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex flex-col">
                <div class="grid grid-cols-4 gap-[1.5vw] md:gap-[0.75vw]">
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                </div >

                <div class="mt-3 md:mt-[1.25vw]">
                    <span class="text-sm font-semibold uppercase leading-none tracking-wider text-surface-50 md:text-[1vw]">must contain</span>

                    <div class="flex flex-col gap-1 md:gap-[0.3vw] md:mt-[0.5vw]">
                        {#each Object.entries(password_error_mapping) as item}
                            {@const key = item[0]}
                            {@const value = item[1]}

                            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                                {#if form_errors.password || form_data.password}
                                    {#if form_errors.password && form_errors.password.includes(key)}
                                        <Tick class="opacity-30 w-3 text-primary md:w-[1vw] transition-opacity" />
                                    {:else}
                                        <Tick class="w-3 text-primary md:w-[1vw] transition-opacity" />
                                    {/if}
                                {:else}
                                    <Tick class="opacity-30 w-3 text-primary md:w-[1vw] transition-opacity" />
                                {/if}
                                <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">{value}</span>
                            </div>
                        {/each}
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.5vw]" >
            <label for="confirm-password" class="text-lg font-semibold leading-none md:text-[1.1vw]">
                Confirm Password:
            </label>
            <input
                bind:value={form_data.confirm_password}
                on:input={handleInput}
                name="confirm_password"
                placeholder="Confirm Password"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 md:gap-[0.5vw] leading-none text-xs md:text-[0.75vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if form_errors.confirm_password}
                    <Markdown markdown={form_errors.confirm_password[0]} />
                {:else}
                    <span>Please make sure you enter the same password in both fields</span>
                {/if}
            </div>
        </div>
    </div>
    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-xs leading-none text-surface-100 md:text-[0.75vw]">Already have an account?</span>
            <button class="text-start text-base leading-none md:text-[1.1vw] text-primary underline">
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
