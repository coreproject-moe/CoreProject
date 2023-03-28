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
    type="checkbox"
    id={$modals.search}
    class="modal-toggle"
/>
<div class="modal">
    <div class="modal-box">
        <h3 class="text-lg font-bold">Congratulations random Internet user!</h3>
        <p class="py-4">
            You've been selected for a chance to get one year of subscription to use Wikipedia for
            free!
        </p>
        <div class="modal-action">
            <label
                for={$modals.search}
                class="btn"
            >
                Yay!
            </label>
        </div>
    </div>
</div>
