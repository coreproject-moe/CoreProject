<script lang="ts">
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import Arrow from "$icons/Arrow/Index.svelte";

    import { z } from "zod";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import { object_to_form_data } from "$functions/object_to_form_data";
    import * as _ from "lodash-es";
    import { reverse } from "$functions/urls";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { cn } from "$functions/classname";
    import { handle_input } from "../functions/handle_input";
    import { user_authenticated } from "$stores/user";
    import { enhance_anchor } from "$functions/anchor_enhancements";
    import { autofocus } from "$functions/autofocus";

    let form_is_submitable: boolean | null = null;

    let username_or_email = {
            value: "",
            error: new Array<string>()
        },
        password = {
            value: "",
            error: new Array<string>()
        };

    const handle_username_input = (event: Event) => {
            handle_input({ event, schema: z.string().min(1, "Please enter a **Email address** or **Username**"), error_field: username_or_email });
        },
        handle_password_input = (event: Event) => {
            handle_input({ event, schema: z.string().min(1, "**Password** can't be empty"), error_field: password });
        };

    const check_if_form_is_submittable = () => {
        form_is_submitable = [username_or_email, password].every((field) => {
            return field.value && _.isEmpty(field.error);
        });
    };

    const handle_submit = async () => {
        const form_data = await object_to_form_data({
            username: username_or_email.value,
            password: password.value
        });
        const res = await fetch(reverse("login-endpoint"), {
            method: "POST",
            body: form_data,
            headers: {
                "X-CSRFToken": get_csrf_token()
            }
        });
        if (res.ok) {
            user_authenticated.set(true);
        } else {
            throw new Error("Login failed");
        }
    };
</script>

{#if $user_authenticated}
    <div class="flex h-full flex-col items-start justify-center gap-[2vw]">
        <div class="flex items-center text-base font-bold uppercase leading-none tracking-widest text-white md:text-[1.5vw]">
            welcome back
            <!-- Show request.user -->
        </div>
        <div>
            Perhaps you meant to
            <a
                href={reverse("logout_view")}
                use:enhance_anchor={{ verb: "GET", target: "body" }}
                on:click|preventDefault={() => {
                    user_authenticated.set(false);
                }}
                class="text-base leading-none text-primary underline md:text-[1.1vw]"
            >
                logout
            </a>
            ?
        </div>
    </div>
{:else}
    <form
        use:autofocus
        on:submit|preventDefault={handle_submit}
        class="flex h-full flex-col justify-between"
    >
        <div>
            <span class="flex items-center text-lg font-bold uppercase leading-none tracking-widest text-warning md:text-[1.25vw]">hey there! let's login</span>
            <button
                on:click={() => window.history.back()}
                class="btn btn-link p-0 h-max min-h-full md:text-[1.25vw] md:gap-[0.5vw]"
            >
                <Arrow variant="fill" class="md:size-[1.25vw] -rotate-90" />
                Go Back
            </button>
        </div>

        <div class="flex flex-col gap-5 md:block">
            <div class="flex flex-col gap-2 md:gap-[0.5vw]">
                <label
                    for="username"
                    class="text-base font-semibold leading-none md:text-[1.1vw]"
                >
                    Email address / Username:
                </label>
                <input
                    bind:value={username_or_email.value}
                    on:input={handle_username_input}
                    on:input={check_if_form_is_submittable}
                    placeholder="sora_amamiya@coreproject.moe / soraamamiya#0001"
                    class="border-neutral focus:border-primary w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-colors duration-300 placeholder:text-white/50 md:rounded-[0.75vw] md:border-[0.2vw] p-3.5 md:px-[1.1vw] md:py-[0.8vw] leading-none md:text-[1.1vw]"
                />
                <div class="flex items-center gap-2 text-[0.7rem] leading-none md:gap-[0.5vw] md:text-[0.8vw]">
                    <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                    {#if _.isEmpty(username_or_email.error)}
                        <span>we’ll send you a verification email, so please ensure it’s active</span>
                    {:else}
                        <Markdown
                            class="text-error"
                            markdown={username_or_email.error.join("")}
                        />
                    {/if}
                </div>
            </div>
            <div class="flex flex-col gap-[0.3rem] md:mt-[1.5vw] md:gap-[0.5vw]">
                <label
                    for="username"
                    class="text-base font-semibold leading-none md:text-[1.1vw]"
                >
                    Password:
                </label>
                <div class="relative flex flex-col">
                    <input
                        bind:value={password.value}
                        on:input={handle_password_input}
                        on:input={check_if_form_is_submittable}
                        placeholder="enter your existing password"
                        class="border-neutral focus:border-primary w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-colors duration-300 placeholder:text-white/50 md:rounded-[0.75vw] md:border-[0.2vw] p-3.5 md:px-[1.1vw] md:py-[0.8vw] leading-none md:text-[1.1vw]"
                    />
                </div>
                <div class="text-surface-300 flex items-center gap-2 text-[0.7rem] leading-none md:gap-[0.5vw] md:text-[0.8vw]">
                    <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                    {#if _.isEmpty(password.error)}
                        <span>enter password of your account</span>
                    {:else}
                        <Markdown
                            class="text-error"
                            markdown={password.error.join("")}
                        />
                    {/if}
                </div>
            </div>
            <button class="btn btn-secondary flex h-max min-h-max flex-col items-start p-0 text-start text-base font-semibold leading-none text-primary underline md:mt-[2vw] md:text-[1vw]">
                &lt; forgot password? &gt;
            </button>
        </div>

        <div class="flex items-center justify-between">
            <div class="flex flex-col gap-1 md:gap-[0.5vw]">
                <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Don't have a core account?</span>
                <a
                    href={reverse("register_view")}
                    use:enhance_anchor={{ verb: "GET", target: "body" }}
                    class="btn btn-link p-0 size-max min-h-full text-base leading-none md:text-[1.1vw]"
                >
                    Register
                </a>
            </div>
            <button
                type="submit"
                class={cn(
                    form_is_submitable || "btn-disabled",
                    `btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.75vw] md:py-[1vw] md:px-[1.25vw] md:text-[0.95vw]`
                )}
            >
                <span>Continue</span>
                <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
            </button>
        </div>
    </form>
{/if}
