<script lang="ts">
    // Your custom Skeleton theme:
    import "../theme.scss";

    // This contains the bulk of Skeletons required styles:
    import "@skeletonlabs/skeleton/styles/all.css";
    // Most of your app wide CSS should be put in this file
    import "../app.scss";
    import { AppShell, Avatar } from "@skeletonlabs/skeleton";

    import AnimeCore from "$icons/AnimeCore.svelte";
    import Logo from "$icons/Logo.svelte";
    import Search from "$icons/Search.svelte";
</script>

<div class="h-screen overflow-hidden">
    <AppShell>
        <svelte:fragment slot="header">
            <div class="h-24 flex justify-between">
                <Logo
                    height="48"
                    width="33.6"
                    class="mt-12 mx-12"
                />

                <AnimeCore
                    width="168"
                    height="33.6"
                    class="self-center"
                />

                <div class="h-16 w-16 mr-16 self-center">
                    <Avatar
                        rounded="rounded-md"
                        src="https://i.pravatar.cc/?img=48"
                        initials="JD"
                    />
                </div>
            </div>
        </svelte:fragment>
        <svelte:fragment slot="sidebarLeft">
            <div class="w-32 flex justify-center mt-14 flex-col items-center">
                <button
                    type="button"
                    class="btn-icon bg-warning-400 rounded-lg p-0"
                >
                    <Search
                        color="black"
                        width="20"
                        height="20"
                    />
                </button>

                <button
                    type="button"
                    class="btn-icon bg-initial rounded-lg p-0 mt-14"
                >
                    Home
                </button>
            </div>
        </svelte:fragment>

        <!-- Page contents go here  -->
        <slot />
    </AppShell>
</div>
