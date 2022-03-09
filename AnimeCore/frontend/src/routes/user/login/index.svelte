<script lang="ts">
    import { page } from "$app/stores";
    import { browser } from "$app/env";

    import { trapFocus } from "$lib/functions/trapFocus";
    import { isUserAuthenticated, userToken } from "$store/users";

    import { tokenObtainUrl } from "$urls/restEndpoints";
    import { signupPageUrl } from "$urls/pageUrlEndpoints";

    import { projectName } from "$lib/constants/frontend/projectName";

    // Bind it to show or hide passwords
    let passwordShown = false;

    // Bindable variables.
    let username = "";
    let password = "";

    // Show error message if theres an error.
    let errorMessage = "";

    const handlePasswordInput = async (e: Event) => {
        const target = e.target as HTMLInputElement;
        password = target?.value;
    };

    const handleFormSubmit = async () => {
        try {
            const res = await fetch(tokenObtainUrl, {
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json"
                },
                method: "POST",
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });
            const data = await res.json();

            if (res?.ok) {
                userToken.set(data);

                // Goto Next page if it exists else redirect to home.
                const next = $page.url.searchParams.get("next");
                browser && next ? (window.location.href = next) : (window.location.href = "/home/");
            }
            errorMessage = data.detail;
        } catch (err) {
            if (err instanceof Error) {
                userToken.set({ refresh: "", access: "" });
                errorMessage = "Cannot POST to Backend | Is backend down ? 🤔";
                console.error(`Can't POST to backend | Reason : ${err.message}`);
            }
        }
    };
</script>

<svelte:head>
    <title>Login Page | {projectName}</title>
</svelte:head>

{#if errorMessage}
    <div class="columns is-mobile is-centered">
        <div class="column is-narrow">
            <p class="error">{errorMessage}</p>
        </div>
    </div>
{/if}

{#if $isUserAuthenticated}

    <div class="columns is-mobile is-centered">
        <div class="column is-narrow">
            <p class="has-text-white">You are already logged in 😕</p>
        </div>
    </div>

{:else}

    <form on:submit|preventDefault={handleFormSubmit} method="POST" use:trapFocus>
        <div class="items field is-horizontal pt-3">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            name="username"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Username / Email"
                            maxlength={50}
                            required={true}
                            bind:value={username}
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
                            maxlength={1024}
                            minlength={8}
                            required={true}
                            on:input={handlePasswordInput}
                        />
                        <span
                            class="icon is-small is-right is-clickable is-unselectable"
                            on:click={async () => {
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
                <a class="has-text-white" rel="external" href="/"> Forgot password? </a>
            </div>
        </div>
        <div class="level-right">
            <div class="level-item is-size-7">
                <p class="has-text-white is-font-face-ubuntu">
                    New here?
                    <span class="has-text-link">
                        <a class="has-text-white is-underlined" rel="external" href={signupPageUrl}>
                            Register an account
                        </a>
                    </span>
                </p>
            </div>
        </div>
    </div>
    
{/if}
