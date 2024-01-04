<script lang="ts">
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import * as z from "zod";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    import { object_to_form_data } from "$functions/object_to_form_data";
    import * as _ from "lodash-es";
    import { reverse } from "$functions/urls";
    import { get_csrf_token } from "$functions/get_csrf_token";
    import { onMount } from "svelte";
    import { string_to_boolean } from "$functions/string_to_bool";
    import { cn } from "$functions/classname";

    let user_authenticated: boolean | null = null,
        form_is_submitable = false;

    onMount(() => {
        user_authenticated = string_to_boolean(window.user_authenticated);
    });
    let username_or_email = {
            value: "",
            error: new Array<string>()
        },
        password = {
            value: "",
            error: new Array<string>()
        };

    const handle_username_input = (event: Event) => {
            const target = event.target as HTMLInputElement;

            const schema = z.string().min(1, "Please enter a **Email address** or **Username**");
            try {
                schema.parse(target.value);
                username_or_email.error = [];
            } catch (err) {
                if (err instanceof z.ZodError) {
                    username_or_email.error = Object.values(err.flatten().formErrors) as unknown as string[];
                }
            }
        },
        handle_password_input = (event: Event) => {
            const target = event.target as HTMLInputElement;

            const schema = z.string().min(1, "**Password** can't be empty");
            try {
                schema.parse(target.value);
            } catch (err) {
                if (err instanceof z.ZodError) {
                    password.error = Object.values(err.flatten().fieldErrors) as unknown as string[];
                }
            }
        };
    const handleSubmit = async () => {
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
            user_authenticated = true;
        } else {
            throw new Error("Login failed");
        }
    };

    $: {
        form_is_submitable = _.isEmpty(username_or_email.error) && _.isEmpty(password.error) && !_.isEmpty(username_or_email.value) && !_.isEmpty(password.value);
    }
</script>

{#if user_authenticated}
    <div class="flex h-full flex-col items-start justify-center gap-[2vw]">
        <div class="flex items-center text-base font-bold uppercase leading-none tracking-widest text-white md:text-[1.5vw]">
            welcome back
            <!-- Show request.user -->
        </div>
        <div>
            Perhaps you meant to
            <a
                href={reverse("logout_view")}
                class="text-base leading-none text-primary underline md:text-[1.1vw]"
            >
                logout
            </a>
            ?
        </div>
    </div>
{:else}
    <form
        on:submit|preventDefault={handleSubmit}
        class="flex h-full flex-col justify-between"
    >
        <span class="flex items-center text-lg font-bold uppercase leading-none tracking-widest text-white md:text-[1.5vw]">hey there! welcome back 👋</span>

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
                    placeholder="sora_amamiya@coreproject.moe / soraamamiya#0001"
                    class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                />
                <div class="text-surface-300 flex items-center gap-2 text-[0.7rem] leading-none md:gap-[0.5vw] md:text-[0.8vw]">
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
                        placeholder="enter your existing password"
                        class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
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
                <button class="text-start text-base leading-none text-primary underline md:text-[1.1vw]">Register</button>
            </div>
            <button
                type="submit"
                class={cn(
                    form_is_submitable || "btn-disabled",
                    `btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.5vw] md:p-[1vw] md:text-[0.95vw]`
                )}
            >
                <span>Continue</span>
                <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
            </button>
        </div>
    </form>
{/if}
