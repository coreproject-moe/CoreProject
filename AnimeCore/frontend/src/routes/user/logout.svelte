<script lang="ts">
    // This constant is very useful. PLease stay at top
    const homePage = "/anime";

    import { onMount } from "svelte";

    import { browser } from "$app/env";
    import { page } from "$app/stores";

    import { userToken } from "$store/users";
    import { tokenBlacklistUrl } from "$urls/restEndpoints";

    let errorMessage: string;
    let logoutState: boolean = false;
    let timeout: number;

    const loginpage = $page.url.searchParams.get("login_page") ?? false;
    const next = $page.url.searchParams.get("next") ?? homePage;

    onMount(async () => {
        timeout = 3000;
    });

    setInterval(async () => {
        timeout = timeout - 1000;
    }, 1000);

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

                // Control the timer. Control the Flow
                timeout = 3000;
                logoutState = true;
            })
            .catch((error) => {
                if (typeof error.json === "function") {
                    error.json().then((jsonError: unknown) => {
                        errorMessage = JSON.stringify(jsonError);
                    });
                }
            });
    }, 3000);

    // Goto Next page if it exists else redirect to home.
    $: {
        if (browser) {
            if (logoutState && timeout === 0) {
                window.location.href = loginpage ? `/user/login?next=${next}` : next;
            }
        }
    }
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
            If no option is picked we'll redirect to "{loginpage
                ? `/user/login?next=${next}`
                : next}" {timeout / 1000}s
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
