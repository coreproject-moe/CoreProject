<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import prettyBytes from "pretty-bytes";

    export let checkboxes: any;
    export let index: number;
    export let file: File;
    export let selected_files: File[];
</script>

<tr class="md:text-[1vw]">
    <td>
        <input
            bind:checked={checkboxes[index]}
            bind:group={selected_files}
            value={file}
            on:change
            type="checkbox"
            class="cursor-pointer rounded border-2 bg-transparent focus:ring-0 focus:ring-offset-0 md:h-[1.25vw] md:w-[1.25vw] md:border-[0.2vw]"
        />
    </td>
    <td class="line-clamp-1">{file.name}</td>
    <td class="whitespace-nowrap">{new FormatDate(new Date(file.lastModified).toISOString()).format_to_human_readable_form}</td>
    <td class="whitespace-nowrap">{prettyBytes(file.size)}</td>
    <td>
        <progress
            class="progress progress-primary w-full md:h-[0.35vw] md:rounded-[0.25vw]"
            value="0"
        />
    </td>
</tr>