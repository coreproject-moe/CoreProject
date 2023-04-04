<script lang="ts">
    import Cookies from "js-cookie";
    import { get } from "svelte/store";

    import { user_is_logged_in } from "$store/User";

    if (get(user_is_logged_in)) {
        Cookies.remove("token");
        user_is_logged_in.set(false);
    }
</script>

{#if $user_is_logged_in}
    <div class="text-center text-2xl text-white">You have successfully logged out</div>
{:else}
    <div class="text-center text-2xl text-white">
        Did you mean to <a
            class="link"
            href="./login"
        >
            log in
        </a>
        ?
    </div>
{/if}
