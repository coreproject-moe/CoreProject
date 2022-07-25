<script lang="ts">
    export let maxSlide: number;
    export let current: number;

    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
</script>

<div class="btn-group justify-center">
    <button class="btn">1</button>
    <button class="btn btn-disabled">...</button>

    <button class="btn">2</button>
    <button class="btn btn-active">3</button>
    <button class="btn">4</button>
    <button class="btn btn-disabled">...</button>

    <button class="btn">100</button>
</div>
