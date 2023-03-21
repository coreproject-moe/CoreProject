<script lang="ts">
    import Cookies from "js-cookie";
    import { user_is_logged_in } from "$store/User";

    if ($user_is_logged_in) {
        Cookies.remove("token");
        user_is_logged_in.set(false);
    }
</script>

<div class="text-center text-2xl text-white">You are successfully logged out</div>
