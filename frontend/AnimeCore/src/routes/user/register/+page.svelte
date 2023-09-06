<script lang="ts">
    import { page as svelte_store_page } from "$app/stores";
    import { OpengraphGenerator } from "$functions/opengraph";
    import RegisterFormSkeleton from "$skeletons/register_page.svelte";
    import type { ComponentType } from "svelte";

    const opengraph_html = new OpengraphGenerator({
        title: "Register Page",
        site_name: "CoreProject",
        url: $svelte_store_page.url.href,

        image_url: "", // Use Opengraph later
        locale: "en_US",
        description: "A page where you can register your core account"
    }).generate_opengraph();

    // We import our page components (similar to the one above).
    let one = import("./1.svelte");
    let two = import("./2.svelte");
    let three = import("./3.svelte");

    const pages = [one, two, three];

    // The current page of our form.
    let page = 0;

    // The state of all of our pages
    let pages_state: { [key: number]: Record<string, string | number> } = [];

    // Our handlers
    function onSubmit(values: CustomEvent) {
        if (page === pages.length - 1) {
            // end of the page. do something.. Maybe seek for anime girls with stockings and leggings
            // XD
            console.log("ho ho ho, Wheres my anime girl?");
        } else {
            // If we're not on the last page, store our data and increase a step
            pages_state[page] = values.detail;
            page += 1;
        }
    }

    // Do some wizardy here later
    // https://github.com/sveltejs/language-tools/issues/486#issuecomment-1372330560
    let current_page: Promise<{ default: ComponentType }>;

    $: current_page = pages[page];
</script>

<svelte:head>
    <title>Register | CoreProject</title>
    {@html opengraph_html}
</svelte:head>

<!-- We display the current step here -->
{#await current_page}
    <RegisterFormSkeleton />
{:then Module}
    <svelte:component
        this={Module.default}
        on:submit={onSubmit}
        {pages_state}
    />
{/await}
