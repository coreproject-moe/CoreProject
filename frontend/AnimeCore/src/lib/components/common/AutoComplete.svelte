<script lang="ts">
    const onFocus = () => {
        console.log(1);
    };
</script>

<div class="dropdown dropdown-open">
    <div tabindex="0" class="m-1">
        <div class="relative text-gray-600 focus-within:text-gray-400">
            <span class="absolute inset-y-0 left-0 flex items-center pl-2">
                <button type="submit" class="p-1 focus:outline-none focus:shadow-outline">
                    <svg
                        fill="none"
                        stroke="currentColor"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        viewBox="0 0 24 24"
                        class="w-6 h-6"
                    >
                        <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                </button>
            </span>
            <input
                type="search"
                class="py-2 text-sm text-white bg-gray-900 rounded-md pl-10"
                placeholder="Search..."
                autocomplete="off"
            />
        </div>
    </div>
    <ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
        <li><a>Item 1</a></li>
        <li><a>Item 2</a></li>
    </ul>
</div>

<style global>
</style>
