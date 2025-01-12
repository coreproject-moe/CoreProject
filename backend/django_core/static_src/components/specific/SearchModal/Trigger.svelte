<script lang="ts">
    import { search_modal_state } from "./store";
    import Search from "$icons/Search/Index.svelte";
    let klass = "";
    export { klass as class };
    export let style = "";

    const handle_button_click = () => {
        search_modal_state.set(true);
    };
</script>

<button
    class={klass}
    {style}
    on:click|preventDefault={handle_button_click}
>
    <Search class="w-[1.25vw] text-black" />
</button>
