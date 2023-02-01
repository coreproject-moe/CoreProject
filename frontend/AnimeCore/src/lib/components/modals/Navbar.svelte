<script lang="ts">
    import { modals } from "$store/Modal";
import { timer as timerStore } from "$store/Timer";
    let value: boolean;

    $: switch (value) {
        case true:
            $timerStore = "pause";
            break;
        case false:
            $timerStore = "start";
            break;
    }
</script>

<input
    bind:checked={value}
    type="checkbox"
    id={$modals.navbar}
    class="modal-toggle"
/>
<label
    for={$modals.navbar}
    class="modal cursor-pointer"
>
    <label
        class="modal-box relative"
        for=""
    >
        <h3 class="text-lg font-bold">Congratulations random Internet user!</h3>
        <p class="py-4">
            You've been selected for a chance to get one year of subscription to use Wikipedia for
            free!
        </p>
    </label>
</label>
