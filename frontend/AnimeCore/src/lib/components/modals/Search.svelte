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

    import Search from "$icons/Search.svelte";
    import { responsiveMode } from "$store/Responsive";

    let mobile: boolean;
    $: mobile = $responsiveMode === "mobile";

    let dropDownElement: Partial<HTMLDivElement> | undefined = undefined;
    let data = [];

    const onFocus = () => {
        dropDownElement?.classList?.add("dropdown-open");
    };

    const onBlur = () => {
        dropDownElement?.classList?.remove("dropdown-open");
    };
</script>

<input
    bind:checked={value}
    type="checkbox"
    id={$modals.search}
    class="modal-toggle"
/>
<div class="modal flex flex-col gap-20">
    <div class="modal-box p-1">
        <div class="relative text-gray-600 focus-within:text-gray-400">
            <span class="absolute flex h-full w-16 items-center justify-center">
                <Search
                    color="white"
                    height={15}
                    width={15}
                />
            </span>
            <input
                on:focus={onFocus}
                on:blur={onBlur}
                type="Search"
                class="input w-full pl-16"
                placeholder="Search for anything"
                autocomplete="off"
            />
        </div>
    </div>
    <label
        for=""
        class="flex gap-20"
    >
        <div>
            <p class="pl-3 font-bold">Anime</p>
            <div class="modal-box relative w-72">pass</div>
        </div>
        <div class="modal-box w-72" />
        <div class="modal-box w-72" />
    </label>
</div>
