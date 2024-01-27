<script lang="ts">
    import { FormatDate } from "$functions/format_date";
    import Upload from "$icons/Upload/Index.svelte";
    import Search from "$icons/Search/Index.svelte";
    import Edit from "$icons/Edit/Index.svelte";
    import prettyBytes from "pretty-bytes";
    import Dropzone from "svelte-file-dropzone";
    import * as _ from "lodash-es";
    import { blur } from "svelte/transition";
    import Delete from "$icons/Delete/Index.svelte";
    import Chevron from "$icons/Chevron/Index.svelte";

    let upload_state: "null" | "selecting" | "uploading" = "null",
        show_dropzone = false,
        dropzone_active = false;

    let files: File[] = [],
        selected_files: File[] = [];

    // A key-value pair that includes mimetype and extension
    const file_whitelist = {
        "video/mp4": ".mp4",
        "video/x-matroska": ".mkv"
    };

    let main_checkbox: HTMLInputElement;
    let checkboxes = Array(files.length).fill(false);

    function handle_main_checkbox_change(event: Event) {
        const target = event.target as HTMLInputElement;

        if (target.checked) {
            checkboxes = Array(files.length).fill(true);
            selected_files = files;
        } else {
            checkboxes = Array(files.length).fill(false);
            selected_files = [];
        }
    }

    function handle_sub_checkbox_change(): void {
        const checks = checkboxes.filter((checked) => checked);

        if (checks.length === files.length) {
            main_checkbox.indeterminate = false;
            main_checkbox.checked = true;
        } else if (checks.length !== 0) {
            main_checkbox.indeterminate = true;
            main_checkbox.checked = false;
        } else {
            main_checkbox.indeterminate = false;
            main_checkbox.checked = false;
        }
    }

    function handle_select_files(e: CustomEvent) {
        const { acceptedFiles } = e.detail;
        if (!acceptedFiles) return;
        update_files(acceptedFiles);
        upload_state = "selecting";
    }

    function update_files(new_files: File[]) {
        files = _.uniqBy([...files, ...new_files], "name");
    }

    // file drag and drop
    function on_drop_handler(event: DragEvent): void {
        show_dropzone = false;
        dropzone_active = false;

        const event_files = event.dataTransfer?.items as unknown as DataTransferItemList;

        Array.from(event_files).forEach(async (item) => {
            const entry = item.webkitGetAsEntry();

            if (entry?.isDirectory) {
                scan_directory(entry as FileSystemDirectoryEntry);
            } else if (entry?.isFile) {
                const file_entry = entry as FileSystemFileEntry;
                file_entry.file((file) => {
                    if (Object.keys(file_whitelist).includes(file.type)) {
                        update_files([file]);
                    }
                });
            }
        });
    }

    async function scan_directory(item: FileSystemDirectoryEntry) {
        let directory_reader = item.createReader();

        directory_reader.readEntries((entries) => {
            entries.forEach(async (entry) => {
                if (entry.isFile) {
                    const item = entry as FileSystemFileEntry;
                    item.file(async (file) => {
                        const file_type = file.name.split(".")[1];
                        if (Object.values(file_whitelist).includes(`.${file_type}`)) {
                            if (Object.keys(file_whitelist).includes(file.type)) {
                                update_files([file]);
                            }
                        }
                    });
                } else if (entry.isDirectory) {
                    await scan_directory(entry as FileSystemDirectoryEntry);
                }
            });
        });
    }

    function handle_delete() {
        files = files.filter((file) => !selected_files.includes(file));
        // uncheck
        checkboxes = Array(files.length).fill(false);
        main_checkbox.indeterminate = false;
        main_checkbox.checked = false;
    }

    const table_head_mapping = [
        {
            name: "name",
            left_button_click: () => {
                console.log("Name sorting left clicked!")
            },
            right_button_click: () => {}
        },
        { name: "date modified", left_button_click: () => {}, right_button_click: () => {} },
        { name: "size", left_button_click: () => {}, right_button_click: () => {} }
    ];
</script>

<svelte:window
    on:dragover|preventDefault={() => (show_dropzone = true)}
    on:dragleave|preventDefault={() => (show_dropzone = false)}
    on:drop|preventDefault={() => (show_dropzone = false)}
/>

{#if show_dropzone}
    <div
        transition:blur|local={{ duration: 200 }}
        class="absolute inset-0 z-50 flex items-center justify-center bg-secondary/80"
    >
        <div class="rounded-[1vw] bg-neutral p-[1.25vw]">
            <div
                role="button"
                tabindex="0"
                on:dragover|preventDefault={() => (dropzone_active = true)}
                on:drop|preventDefault={on_drop_handler}
                on:dragleave|preventDefault={() => (dropzone_active = false)}
                class="flex w-[50vw] flex-col place-items-center gap-[0.75vw] rounded-[1vw] border-[0.2vw] border-dashed border-white/50 bg-neutral py-[4vw] transition duration-300 ease-in-out"
                class:bg-base-200={dropzone_active}
            >
                <Upload class="mb-[1.5vw] w-[5vw]" />
                <span class="text-[1.25vw] font-semibold leading-none">Drop your files here to upload</span>
                <span class="text-surface-50 text-[1vw] leading-none">Allowed formats: {Object.values(file_whitelist)}</span>
            </div>
        </div>
    </div>
{/if}

<div class="flex min-h-dvh flex-col bg-secondary p-5 md:gap-[2vw] md:px-[5vw] md:py-[3vw]">
    <div class="grid grid-cols-12 gap-7 md:gap-[5vw] md:px-[10vw]">
        <div class="col-span-12 mt-20 flex items-end md:col-span-7 md:pb-[1.5vw]">
            <div class="w-full text-center md:text-left">
                {#if upload_state === "selecting"}
                    <progress class="progress progress-primary w-full md:h-[1vw] md:rounded-[0.25vw]" />
                {:else if upload_state === "null"}
                    <progress
                        class="progress progress-primary w-full md:h-[1vw] md:rounded-[0.25vw]"
                        value="0"
                    />
                {:else if upload_state === "uploading"}
                    <progress
                        class="progress progress-primary w-full md:h-[1vw] md:rounded-[0.25vw]"
                        value="0"
                        max="100"
                    />
                {/if}
                <div class="mt-2 flex justify-center gap-3 leading-none md:mt-[1.5vw] md:flex-col md:gap-[0.5vw]">
                    <span class="font-semibold md:text-[1vw]">
                        {prettyBytes(files?.reduce((total, current) => total + current.size, 0))}
                    </span>
                    <span class="text-surface-50 md:text-[1vw]">{files.length} files</span>
                </div>
            </div>
        </div>

        <!-- add more props: https://github.com/thecodejack/svelte-file-dropzone#props -->
        <Dropzone
            containerClasses="relative col-span-12 flex gap-10 md:gap-0 cursor-pointer md:flex-col items-center justify-center bg-neutral md:col-span-5 h-40 md:h-[12vw] md:gap-[0.25vw] rounded-xl md:rounded-[0.75vw]"
            disableDefaultStyles={true}
            accept=".mp4,.mkv"
            on:drop={handle_select_files}
        >
            <Upload class="w-20 text-white/75 md:w-[2vw] md:text-white" />
            <div class="flex select-none flex-col items-center gap-1 leading-none md:w-full md:gap-[0.35vw]">
                <span class="text-lg font-semibold md:mt-[1vw] md:text-[1.1vw]">Drag and Drop files</span>
                <div class="divider m-0 text-sm before:bg-accent/25 after:bg-accent/25 md:px-[10vw] md:text-[0.9vw] md:before:h-[0.15vw] md:after:h-[0.15vw]">Or</div>
                <span class="font-semibold md:text-[1.1vw]">Browse</span>
            </div>
        </Dropzone>
    </div>
    <div class="divider md:m-0 md:before:h-[0.2vw] md:after:h-[0.2vw]"></div>
    <div class="flex flex-col md:gap-[1vw]">
        <div class="flex flex-col justify-between md:flex-row">
            <div class="flex items-center justify-between gap-3 md:justify-start md:gap-[1vw]">
                <form class="relative flex items-center">
                    <button
                        class="absolute left-2 p-0 md:left-[1vw]"
                        aria-label="Search"
                    >
                        <Search class="w-4 opacity-75 md:w-[1.25vw]" />
                    </button>
                    <input
                        type="text"
                        placeholder="Search"
                        class="placeholder:text-surface-50 h-full w-full rounded-lg border-none bg-neutral pl-9 text-base leading-none text-white shadow-lg !ring-0 placeholder:font-medium md:w-full md:rounded-[0.5vw] md:py-[0.75vw] md:pl-[3vw] md:text-[1.1vw]"
                    />
                </form>
                <div class="relative flex items-center">
                    <button
                        class="absolute left-2 p-0 md:left-[1vw]"
                        aria-label="Search"
                    >
                        <Search class="w-4 opacity-75 md:w-[1.25vw]" />
                    </button>
                    <input
                        type="text"
                        placeholder="Folder Name"
                        class="placeholder:text-surface-50 h-full w-full rounded-lg border-none bg-neutral/50 pl-9 text-base leading-none text-white shadow-lg !ring-0 placeholder:font-medium md:w-full md:rounded-[0.5vw] md:py-[0.75vw] md:pl-[3vw] md:text-[1.1vw]"
                    />
                </div>
            </div>

            <div class="mt-5 flex justify-between md:mt-0 md:justify-start md:gap-[3vw]">
                <button
                    disabled={_.isEmpty(files)}
                    class="text-surface-50 btn flex min-h-full gap-3 !bg-transparent p-0 text-base font-semibold capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]"
                >
                    <Edit class="w-4 md:w-[1vw]" />

                    <span>Rename</span>
                </button>
                <button
                    disabled={_.isEmpty(files)}
                    class="text-surface-50 btn flex min-h-full gap-3 !bg-transparent p-0 text-base font-semibold capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]"
                >
                    <Edit class="w-4 md:w-[1vw]"></Edit>
                    <span>Edit Details</span>
                </button>
                <button
                    disabled={_.isEmpty(files)}
                    on:click|preventDefault={handle_delete}
                    class="text-surface-50 btn flex min-h-full gap-3 !bg-transparent p-0 text-base font-semibold capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]"
                >
                    <Delete class="w-4 md:w-[1vw]" />
                    <span>Delete</span>
                </button>
                <button
                    disabled={_.isEmpty(files)}
                    class="btn btn-primary min-h-max md:h-max md:rounded-[0.5vw] md:p-[1vw] md:text-[1vw]"
                >
                    <Upload class="w-4 md:w-[1.25vw]" />
                    Upload
                </button>
            </div>
        </div>

        <table class="table-auto border-separate border-spacing-2 break-all leading-none md:border-spacing-y-[0.75vw]">
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
                    {#each table_head_mapping as item}
                        <th>
                            <div class="flex items-center md:gap-[0.5vw]">
                                <span class="whitespace-nowrap capitalize">{item.name}</span>
                                <button
                                    on:click|preventDefault={item.left_button_click}
                                    class="btn min-h-full !bg-transparent p-0"
                                >
                                    <Chevron class="w-4 md:w-[1vw]"></Chevron>
                                </button>
                                <button
                                    on:click|preventDefault={item.right_button_click}
                                    class="btn min-h-full !bg-transparent p-0"
                                >
                                    <Chevron class="w-4 rotate-180 opacity-50 md:w-[1vw]"></Chevron>
                                </button>
                            </div>
                        </th>
                    {/each}
                </tr>
            </thead>
            <tbody>
                {#each files as file, index}
                    <tr class="md:text-[1vw]">
                        <td>
                            <input
                                bind:checked={checkboxes[index]}
                                bind:group={selected_files}
                                value={file}
                                on:change={handle_sub_checkbox_change}
                                type="checkbox"
                                class="cursor-pointer rounded border-2 bg-transparent focus:ring-0 focus:ring-offset-0 md:h-[1.25vw] md:w-[1.25vw] md:border-[0.2vw]"
                            />
                        </td>
                        <td class="line-clamp-1">{file.name}</td>
                        <td class="whitespace-nowrap">{new FormatDate(new Date(file.lastModified).toISOString()).format_to_human_readable_form}</td>
                        <td class="whitespace-nowrap">{prettyBytes(file.size)}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
        {#if files.length === 0}
            <div class="flex w-full flex-col items-center justify-center md:flex-row md:gap-[2vw]">
                <coreproject-icon-empty class="w-32 stroke-accent stroke-[0.15vw] md:w-[10vw] md:stroke-accent/50"></coreproject-icon-empty>
                <div class="flex flex-col items-center gap-2 md:items-start md:gap-[0.75vw]">
                    <span class="text-base font-semibold leading-none text-accent md:text-[1.4vw]">Empty!</span>
                    <span class="text-sm leading-none text-accent/50 md:text-[1.1vw]">Upload something to make kokoro-chan happy</span>
                </div>
            </div>
        {/if}
    </div>
</div>
