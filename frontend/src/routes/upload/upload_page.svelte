<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import Chevron from "$icons/chevron.svelte";
    import Cross from "$icons/cross.svelte";
    import Delete from "$icons/delete.svelte";
    import Edit from "$icons/edit.svelte";
    import EmptyUpload from "$icons/empty_upload.svelte";
    import Search from "$icons/search.svelte";
    import Star from "$icons/star.svelte";
    import Upload from "$icons/upload.svelte";
    import { FileDropzone } from "@skeletonlabs/skeleton";
    import { ProgressBar } from "@skeletonlabs/skeleton";
    import dayjs from "dayjs";
    import prettyBytes from "pretty-bytes";
    import { blur } from "svelte/transition";

    let main_checkbox: HTMLInputElement;

    let checkbox_elements: Array<HTMLInputElement> = new Array<HTMLInputElement>();
    let data_list: Array<{ file: File }> = new Array<{ file: File }>();
    let show_dropzone = false;
    let dropzone_active = false;

    function handle_main_checkbox_change(event: Event) {
        const target = event.target as HTMLInputElement;

        if (target.checked) {
            checkbox_elements.forEach((element) => {
                element.checked = true;
            });
        } else {
            checkbox_elements.forEach((element) => {
                element.checked = false;
            });
        }
    }

    // A key-value pair that includes mimetype and extension
    const file_whitelist = {
        "video/mp4": ".mp4",
        "video/mkv": ".mkv"
    };
    function handle_sub_checkbox_change(): void {
        const truthy_checkbox_array = checkbox_elements.filter((item) => item.checked);

        if (truthy_checkbox_array.length === data_list.length) {
            main_checkbox.indeterminate = false;
            main_checkbox.checked = true;
        } else if (truthy_checkbox_array.length !== 0) {
            main_checkbox.indeterminate = true;
            main_checkbox.checked = false;
        } else {
            main_checkbox.indeterminate = false;
            main_checkbox.checked = false;
        }
    }

    // handle the file_size
    function handle_file_change(e: Event): void {
        const files = (e.target as HTMLInputElement).files as FileList;
        const file_list_names = data_list.map((data) => {
            return data.file.name;
        });

        Array.from(files).forEach((file) => {
            if (Object.keys(file_whitelist).includes(file.type)) {
                if (!file_list_names.includes(file.name)) {
                    data_list = data_list.concat({ file: file });
                }
            }
        });
    }

    // file drag and drop
    function on_drop_handler(event: DragEvent): void {
        show_dropzone = false;
        dropzone_active = false;

        const files = event.dataTransfer?.items as unknown as DataTransferItemList;
        const file_list_names = data_list.map((data) => {
            return data.file.name;
        });

        Array.from(files).forEach(async (item) => {
            const entry = item.webkitGetAsEntry();

            if (entry?.isDirectory) {
                scan_directory(entry as FileSystemDirectoryEntry);
            } else if (entry?.isFile) {
                const file_entry = entry as FileSystemFileEntry;
                file_entry.file((file) => {
                    if (Object.keys(file_whitelist).includes(file.type)) {
                        if (!file_list_names.includes(file.name)) {
                            data_list = data_list.concat({ file: file });
                        }
                    }
                });
            }
        });
    }

    async function scan_directory(item: FileSystemDirectoryEntry) {
        let directory_reader = item.createReader();
        const file_list_names = data_list.map((data) => {
            return data.file.name;
        });

        directory_reader.readEntries((entries) => {
            entries.forEach(async (entry) => {
                if (entry.isFile) {
                    const item = entry as FileSystemFileEntry;
                    item.file(async (file) => {
                        const file_type = file.name.split(".")[1];

                        if (Object.values(file_whitelist).includes(`.${file_type}`)) {
                            if (!file_list_names.includes(file.name)) {
                                data_list = data_list.concat({ file: file });
                            }
                        }
                    });
                } else if (entry.isDirectory) {
                    await scan_directory(entry as FileSystemDirectoryEntry);
                }
            });
        });
    }
</script>

<svelte:window
    on:dragover|preventDefault={() => (show_dropzone = true)}
    on:dragleave|preventDefault={() => (show_dropzone = false)}
    on:drop|preventDefault={() => (show_dropzone = false)}
/>

{#if show_dropzone}
    <dropzone-background
        transition:blur|local={{ duration: 200 }}
        class="absolute inset-0 z-50 flex items-center justify-center bg-surface-900/80"
    >
        <dropzone-outer class="rounded-[1vw] bg-surface-400 p-[1.25vw]">
            <dropzone
                role="button"
                tabindex="0"
                on:dragover|preventDefault={() => (dropzone_active = true)}
                on:drop|preventDefault={on_drop_handler}
                on:dragleave|preventDefault={() => (dropzone_active = false)}
                class="flex w-[50vw] flex-col place-items-center gap-[0.75vw] rounded-[1vw] border-[0.2vw] border-dashed border-surface-50 bg-surface-400 py-[4vw] transition duration-300 ease-in-out"
                class:bg-surface-500={dropzone_active}
            >
                <Upload class="mb-[1.5vw] w-[5vw]" />
                <span class="text-[1.25vw] font-semibold leading-none">Drop your files here to upload</span>
                <span class="text-[1vw] leading-none text-surface-50">Allowed formats: mp4, mkv</span>
            </dropzone>
        </dropzone-outer>
    </dropzone-background>
{/if}

<container class="block p-5 md:py-[2vw] md:pl-[5vw] md:pr-[3.75vw]">
    <upload-area class="grid grid-cols-12 gap-7 md:gap-[5vw] md:px-[10vw]">
        <upload-progress class="col-span-12 mt-20 flex items-end md:col-span-7 md:pb-[1.5vw]">
            <div class="w-full text-center md:text-left">
                <ProgressBar
                    label="Progress Bar"
                    value={Array.isArray(data_list) && data_list.length === 0 ? 0 : undefined}
                    max={100}
                    height="h-3 md:h-[0.9vw]"
                    rounded="rounded md:rounded-[0.25vw]"
                    track="bg-surface-400"
                    meter="bg-primary-500"
                />
                <progress-info class="mt-5 flex flex-col gap-3 leading-none md:mt-[1.5vw] md:gap-[0.5vw]">
                    <span class="font-semibold md:text-[1vw]">
                        {prettyBytes(data_list.reduce((a, b) => Number(a + b.file.size), 0))}
                    </span>
                    <span class="text-surface-50 md:text-[1vw]">{data_list.length} files</span>
                </progress-info>
            </div>
        </upload-progress>
        <upload-input class="col-span-12 md:col-span-5">
            <FileDropzone
                on:change={handle_file_change}
                accept={Object.values(file_whitelist).join(",")}
                multiple={true}
                name="files"
                padding="md:p-[2vw] !bg-surface-400 h-48 md:h-full"
                border="border-none"
                rounded="rounded-2xl md:rounded-[1vw]"
                regionInterfaceText="flex flex-col place-items-center gap-2 md:gap-[1vw]"
                slotLead="leading-none"
                slotMessage="leading-none"
                slotMeta="leading-none flex flex-col md:gap-[0.25vw]"
            >
                <svelte:fragment slot="lead">
                    <Upload class="w-9 md:w-[2vw]" />
                </svelte:fragment>
                <svelte:fragment slot="message">
                    <span class="text-base font-semibold text-surface-50 md:text-[1.1vw]">Drag and Drop files</span>
                </svelte:fragment>
                <svelte:fragment slot="meta">
                    <divider class="flex items-center justify-center gap-2 md:gap-[0.5vw]">
                        <left-border class="w-5 border-t-2 border-surface-300 md:w-[2vw] md:border-t-[0.1vw]" />
                        <span class="text-xs font-semibold text-surface-300 md:text-[0.9vw]">Or</span>
                        <right-border class="w-5 border-t-2 border-surface-300 md:w-[2vw] md:border-t-[0.1vw]" />
                    </divider>
                    <span class="text-sm text-surface-50 md:text-[1.1vw]">Browse</span>
                </svelte:fragment>
            </FileDropzone>
        </upload-input>
    </upload-area>

    <hr class="!md:border-t-[0.2vw] mb-5 mt-10 !border-t-2 !border-primary-200/25 opacity-0 md:mb-[1vw] md:mt-[3vw] md:opacity-100" />

    <uploads>
        <uploads-options class="flex flex-col justify-between md:flex-row">
            <div class="flex items-center justify-between md:justify-start md:gap-[3vw]">
                <form class="relative flex items-center">
                    <button
                        class="btn absolute left-2 p-0 md:left-[1vw]"
                        aria-label="Search"
                    >
                        <Search
                            class="hidden md:flex"
                            style="width: 1vw; opacity: 0.75;"
                        />
                        <Search
                            class="flex md:hidden"
                            style="width: 1rem; opacity: 0.75;"
                        />
                    </button>
                    <input
                        type="text"
                        placeholder="Search"
                        class="h-full w-56 rounded-lg border-none bg-surface-400 pl-12 text-base leading-none text-white shadow-lg !ring-0 placeholder:font-medium placeholder:text-surface-50 md:w-full md:rounded-[0.5vw] md:py-[0.5vw] md:pl-[3vw] md:text-[1vw]"
                    />
                </form>
                <button class="btn flex gap-2 p-0 leading-none text-surface-50 md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                    <Cross class="w-4 rotate-45 md:w-[1vw]" />
                    New folder
                </button>
            </div>

            <div class="mt-5 flex justify-between md:mt-0 md:justify-start md:gap-[3vw]">
                <button class="btn flex gap-3 p-0 text-base font-semibold leading-none text-surface-50 md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                    <Edit
                        variant="without_underline_around_pencil"
                        class="w-4 md:w-[1vw]"
                    />
                    Rename
                </button>
                <button class="btn flex gap-3 p-0 text-base font-semibold leading-none text-surface-50 md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                    <Edit
                        variant="with_underline_around_pencil"
                        class="w-4 md:w-[1vw]"
                    />
                    Edit Details
                </button>
                <button class="btn flex gap-3 p-0 text-base font-semibold leading-none text-surface-50 md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                    <Delete class="w-4 md:w-[1vw]" />
                    Delete
                </button>
            </div>
        </uploads-options>

        {#if data_list.length > 0}
            <uploads-table class="mt-10 block md:mt-[3vw]">
                <table class="w-full border-separate border-spacing-y-2 leading-none text-surface-50 md:border-spacing-y-[0.25vw]">
                    <thead>
                        <tr class="text-left md:text-[1vw]">
                            <th>
                                <input
                                    bind:this={main_checkbox}
                                    on:change={handle_main_checkbox_change}
                                    type="checkbox"
                                    class="cursor-pointer rounded border-2 bg-transparent focus:ring-0 focus:ring-offset-0 md:h-[1.25vw] md:w-[1.25vw] md:border-[0.2vw]"
                                />
                            </th>
                            {#each ["name", "type", "date modified", "size"] as table_heading_item}
                                <th>
                                    <div class="flex items-center md:gap-[0.5vw]">
                                        <span class="capitalize">{table_heading_item}</span>
                                        <button class="btn p-0"><Chevron class="md:w-[1vw]" /></button>
                                        <button class="btn p-0"><Chevron class="rotate-180 opacity-50 md:w-[1vw]" /></button>
                                    </div>
                                </th>
                            {/each}
                        </tr>
                    </thead>
                    <!-- spacing -->
                    <tbody>
                        <tr>
                            <td class="h-5 md:h-[1vw]" />
                        </tr>
                    </tbody>
                    <!-- spacing -->
                    <tbody>
                        {#each data_list.sort() as data, index}
                            {@const file = data.file}
                            {@const name = file.name}
                            {@const last_modified = new FormatDate(
                                /* 
                                    Somehow things got fked up.
                                    dayjs expects `time` to be in seconds and we have the file.lastModified as milliseconds.
                                    So here we go with our logic. 
                                */
                                dayjs.unix(file.lastModified / 1000).toString()
                            ).format_to_human_readable_form}
                            {@const type = "[DIRECTORY]"}
                            {@const size = prettyBytes(file.size)}

                            <tr>
                                <td class="flex items-center md:gap-[1vw]">
                                    <input
                                        bind:this={checkbox_elements[index]}
                                        on:change={handle_sub_checkbox_change}
                                        type="checkbox"
                                        class="cursor-pointer rounded border-2 bg-transparent focus:ring-0 focus:ring-offset-0 md:h-[1.25vw] md:w-[1.25vw] md:border-[0.2vw]"
                                    />
                                    <button class="btn hidden p-0 md:flex">
                                        <Star
                                            variant="empty"
                                            class="text-surface-50/50 md:w-[1.5vw]"
                                            fill_color="none"
                                        />
                                    </button>
                                </td>
                                {#each [name, type, last_modified, size] as table_item}
                                    <td>
                                        <span class="md:text-[1vw]">{table_item}</span>
                                    </td>
                                {/each}
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </uploads-table>
        {:else}
            <empty-ui class="mt-10 flex w-full flex-col items-center justify-center md:mt-[5vw] md:flex-row md:gap-[2vw]">
                <EmptyUpload class="w-32 stroke-surface-50 stroke-[0.15vw] md:w-[10vw] md:stroke-surface-300" />
                <div class="flex flex-col items-center gap-2 md:items-start md:gap-[0.75vw]">
                    <span class="text-base font-semibold leading-none text-surface-50 md:text-[1.4vw]">Empty!</span>
                    <span class="text-sm leading-none text-surface-300 md:text-[1.1vw]">Upload something to make kokoro-chan happy</span>
                </div>
            </empty-ui>
        {/if}
    </uploads>
</container>
