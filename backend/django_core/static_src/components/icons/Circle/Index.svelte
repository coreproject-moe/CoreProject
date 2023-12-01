<script lang="ts">
    let klass: string;
    export { klass as class };
    export let style: string;
</script>

<svg
    class={klass}
    {style}
    viewBox="0 0 10 10"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <circle
        cx="5"
        cy="5"
        r="5"
        fill="currentColor"
    ></circle>
</svg>
