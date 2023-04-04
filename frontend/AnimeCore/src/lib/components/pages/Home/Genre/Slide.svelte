<script lang="ts">
    import { responsiveMode } from "$store/Responsive";

    import AutoComplete from "./AutoComplete.svelte";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";
</script>

<div class="hero mt-10 min-h-[184px] bg-base-100 md:mt-0 md:min-h-screen">
    <div class="hero-content p-0 text-center">
        <div class="block flex-col">
            <AutoComplete />
        </div>
    </div>
</div>
