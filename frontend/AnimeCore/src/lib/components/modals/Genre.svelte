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
    id={$modals.genre}
    class="modal-toggle"
/>
<label
    class="modal modal-bottom"
    for={$modals.genre}
>
    <div class="modal-box">
        <h3 class="font-bold text-lg">Congratulations random Internet user!</h3>
        <p class="py-4">
            You've been selected for a chance to get one year of subscription to use Wikipedia for
            free!
        </p>
        <div class="modal-action">
            <label
                for={$modals.genre}
                class="btn"
            >
                Yay!
            </label>
        </div>
    </div>
</label>
