<script lang="ts">
    import { fade } from "svelte/transition";

    import * as yup from "yup";
    import { createForm } from "felte";

    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";

    import { page } from "$app/stores";
    import { goto } from "$app/navigation";

    import { trapFocus } from "$lib/functions/trapFocus";
    import { projectName } from "$lib/constants/frontend/project";

    import { tokenObtainUrl } from "$urls/restEndpoints";
    import { isUserAuthenticated, userToken } from "$store/users";

    // Bind it to show or hide passwords
    let passwordShown = false;

    // Show error message if theres an error.

    let errorMessage = "";

    const schema = yup.object({
        username_or_email: yup
            ?.string()
            ?.required("Did you type your <b>Email</b> or <b>Username</b> ? 🤔"),
        password: yup
            ?.string()
            ?.required("How can <b>one</b> create <b>ones</b> account without <b>Password</b> ? 🤔")
            ?.max(1024, "<b>Password</b> must be less than <b>1024 Characters<b/>")
    });
    const { form } = createForm<yup.InferType<typeof schema>>({
        extend: [
            validator({ schema }),
            reporter({
                tippyProps: {
                    theme: "black",
                    allowHTML: true
                }
            })
        ],
        onSubmit: async (values) => {
            try {
                const res = await fetch(tokenObtainUrl, {
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json"
                    },
                    method: "POST",
                    body: JSON.stringify({
                        username: values?.username_or_email,
                        password: values?.password
                    })
                });
                const data = await res.json();
                if (res?.ok) {
                    $userToken = data;
                    $isUserAuthenticated = true;
                    // Goto Next page if it exists else redirect to home.
                    const next = $page.url.searchParams.get("next");
                    goto(next ? next : "/anime");
                }
                errorMessage = data.detail;
            } catch (err) {
                if (err instanceof Error) {
                    $userToken = { refresh: "", access: "" };
                    errorMessage = "Cannot POST to Backend | Is backend down ? 🤔";
                    console.error(`Can't POST to backend | Reason : ${err?.message}`);
                }
            }
        }
    });
</script>

<svelte:head>
    <title>Login Page | {projectName}</title>
</svelte:head>

{#if errorMessage}
    <div class="columns is-mobile is-centered" transition:fade>
        <div class="column is-narrow">
            <p class="error">{errorMessage}</p>
        </div>
    </div>
{/if}

{#if $isUserAuthenticated}
    <div transition:fade>
        <p class="has-text-white has-text-centered">You are already logged in 😕</p>
        <p class="has-text-white has-text-centered">
            Do you plan on <a class="has-text-white is-underlined" href="/user/logout"
                >Logging out?
            </a>👀
        </p>
    </div>
{:else}
    <form method="POST" use:form use:trapFocus transition:fade>
        <div class="items field is-horizontal pt-3">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            name="username_or_email"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Username / Email"
                        />
                        <span class="icon is-small is-left">
                            <ion-icon
                                class="has-text-white is-size-4"
                                name="person-circle-outline"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items field is-horizontal pt-3">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left has-icons-right">
                        <input
                            type={passwordShown ? "text" : "password"}
                            name="password"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Password"
                        />
                        <span
                            class="icon is-small is-right is-clickable is-unselectable"
                            on:click|preventDefault={async () => {
                                passwordShown = !passwordShown;
                            }}
                        >
                            👀
                        </span>
                        <span class="icon is-small is-left">
                            <ion-icon class="has-text-white is-size-4" name="lock-closed-outline" />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items columns is-mobile is-centered pt-3">
            <div class="column is-narrow">
                <button
                    class="button is-rounded is-centered has-text-white has-border-gray is-black"
                >
                    Sign in
                </button>
            </div>
        </div>
    </form>
    <div class="level is-mobile pt-4">
        <div class="level-left">
            <div class="level-item is-size-7">
                <a class="has-text-white" href="/"> Forgot password? </a>
            </div>
        </div>
        <div class="level-right">
            <div class="level-item is-size-7">
                <p class="has-text-white is-font-face-ubuntu">
                    New here?
                    <span class="has-text-link">
                        <a
                            class="has-text-white is-underlined"
                            sveltekit:prefetch
                            href="/user/register"
                        >
                            Register an account
                        </a>
                    </span>
                </p>
            </div>
        </div>
    </div>
{/if}
