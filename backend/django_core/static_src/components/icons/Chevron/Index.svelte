<script lang="ts">
    let klass: string;
    export { klass as class };
    export let style: string;
</script>

<svg
    class={klass}
    {style}
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
>
    <path
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="3.5"
        d="M6 9L12 15L18 9"
    ></path>
</svg>
