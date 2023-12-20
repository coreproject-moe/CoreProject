<script lang="ts">
    let klass = "";
    export { klass as class };
    export let style = "";
</script>

<svg
    class={klass}
    {style}
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <rect
        width="8"
        height="8"
        rx="2"
        fill="currentColor"
    />
    <rect
        x="12"
        width="8"
        height="8"
        rx="2"
        fill="currentColor"
    />
    <rect
        x="12"
        y="12"
        width="8"
        height="8"
        rx="2"
        fill="currentColor"
    />
    <rect
        y="12"
        width="8"
        height="8"
        rx="2"
        fill="currentColor"
    />
</svg>
