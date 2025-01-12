<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import prettyBytes from "pretty-bytes";

    export let file: File;
    export let checked: boolean;
</script>

<tr class="relative md:text-[1vw]">
    <td>
        <input
            on:change
            {checked}
            type="checkbox"
            class="cursor-pointer rounded border-2 bg-transparent focus:ring-0 focus:ring-offset-0 md:h-[1.25vw] md:w-[1.25vw] md:border-[0.2vw]"
        />
    </td>
    <td class="line-clamp-1">{file.name}</td>
    <td class="whitespace-nowrap">{new FormatDate(new Date(file.lastModified).toISOString()).format_to_human_readable_form}</td>
    <td class="whitespace-nowrap">{prettyBytes(file.size)}</td>
    <td class="pointer-events-none absolute inset-0 md:static">
        <progress class="progress progress-primary h-full w-full rounded-sm opacity-25 md:h-[0.5vw] md:rounded-[0.25vw] md:opacity-100" />
    </td>
</tr>
