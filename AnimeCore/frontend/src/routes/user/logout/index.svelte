<script lang="ts">
    // This constant is very useful. PLease stay at top
    const homePage = "/anime";

    import { browser } from "$app/env";
    import { page } from "$app/stores";

    import { userToken } from "$store/users";
    import { tokenBlacklistUrl } from "$urls/restEndpoints";
    import { onMount } from "svelte";

    let errorMessage: string;
    let logoutState: boolean;
    let timeout = 3000;
    let interval: NodeJS.Timer;

    const next = $page.url.searchParams.get("next") ?? homePage;

    onMount(async () => {
        logoutState = false;
    });

    setTimeout(async () => {
        await fetch(tokenBlacklistUrl, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                refresh: $userToken.refresh
            })
        })
            .then((response) => {
                if (!response.ok) {
                    throw response;
                }
                userToken.set({ refresh: "", access: "" });
                browser && localStorage.removeItem("tokens");

                logoutState = true;
            })
            .catch((error) => {
                if (typeof error.json === "function") {
                    error.json().then((jsonError: { detail: string }) => {
                        errorMessage = jsonError.detail;
                    });
                }
            });
    }, 3000);

    $: {
        if (!logoutState) {
            interval = setInterval(async () => {
                timeout = timeout - 1000;
                if (timeout <= 0) {
                    clearInterval(interval);
                }
            }, 1000);
        }
    }

    $: {
        if (logoutState) {
            timeout = 3000;
            interval = setInterval(async () => {
                timeout = timeout - 1000;
                if (timeout <= 0) {
                    clearInterval(timeout);
                }
            }, 1000);
        }
    }
    // Goto Next page if it exists else redirect to home.
    $: browser && logoutState && timeout === 0 ? (window.location.href = next) : null;
</script>

{#if logoutState}
    <div class="has-text-centered">
        <p class="has-text-white">Successfully logged out</p>
        <p class="has-text-white">Where do you wanna go?</p>
        <br />
        <p class="has-text-white">
            <a class="has-text-white is-underlined" href="user/login">Login Page</a> |
            <a class="has-text-white is-underlined" href={homePage}>Home Page</a>
        </p>
        <br />
        <p class="has-text-white">
            If no option is picked we'll redirect to "{next}" {timeout / 1000}s
        </p>
    </div>
{:else}
    <div class="has-text-centered">
        <p class="has-text-white">
            {#if timeout > 0}
                Logging out in {timeout / 1000}s {timeout === 3000
                    ? "😱"
                    : timeout === 2000
                    ? "😨"
                    : timeout === 1000
                    ? "😭"
                    : null}
            {:else}
                What did go wrong ? 😟 <br /> Probably this : {errorMessage}
            {/if}
        </p>
    </div>
{/if}
