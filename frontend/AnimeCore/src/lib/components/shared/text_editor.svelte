<script lang="ts">
    import ImageLoader from "$components/shared/image/image_loader.svelte";
    import { emojis } from "$data/emojis";
    import { is_valid_url } from "$functions/is_valid_url";
    import Bold from "$icons/bold.svelte";
    import Code from "$icons/code.svelte";
    import Hyperlink from "$icons/hyperlink.svelte";
    import Italic from "$icons/italic.svelte";
    import Strike from "$icons/strike.svelte";
    import Underline from "$icons/underline.svelte";
    import Markdown from "./markdown.svelte";
    import { offset } from "caret-pos";
    import { encode } from "html-entities";
    import type { SvelteComponent } from "svelte";
    import tippy from "tippy.js";

    export let textarea_value = "";

    let caret_offset_top: string | null = null,
        caret_offset_left: string | null = null;

    // Bindings
    let textarea_element: HTMLTextAreaElement;

    let emoji_matches: Array<{
            emoji: string;
            keyword: string;
        }>,
        show_emoji_picker = false,
        active_emoji_index: number,
        SHOWN_EMOJI_LIMIT = 5;

    // Icon Mapping
    const icon_and_function_mapping: {
        [key: string]: {
            function: (elemnt: HTMLElement) => void;
            icon: {
                component: typeof SvelteComponent<{}>;
                class: string;
            };
            description: string;
        };
    } = {
        bold: {
            function: (element) => bold_text(element as HTMLTextAreaElement),
            icon: {
                component: Bold,
                class: "w-5 md:w-[1.4vw]  text-surface-200"
            },
            description: "Add bold text, <Ctrl + b>"
        },
        italic: {
            function: (element) => italic_text(element as HTMLTextAreaElement),
            icon: {
                component: Italic,
                class: "w-5 md:w-[1.5vw] text-surface-200"
            },
            description: "Add italic text, <Ctrl + i>"
        },
        underline: {
            function: (element) => underline_text(element as HTMLTextAreaElement),
            icon: {
                component: Underline,
                class: "w-5 md:w-[1.35vw] text-surface-200"
            },
            description: "Add underline text, <Ctrl + u>"
        },
        strike: {
            function: (element) => strike_text(element as HTMLTextAreaElement),
            icon: {
                component: Strike,
                class: "w-5 md:w-[1.5vw] text-surface-200"
            },
            description: "Add strikethrough text, <Ctrl + Shift + x>"
        },
        code: {
            function: (element) => code_text(element as HTMLTextAreaElement),
            icon: {
                component: Code,
                class: "w-5 md:w-[1.5vw] text-surface-200"
            },
            description: "Add code text, <Ctrl + e>"
        },
        hyperlink: {
            function: (element) => hyperlink_text(element as HTMLTextAreaElement),
            icon: {
                component: Hyperlink,
                class: "w-4 md:w-[1.25vw] text-surface-200 ml-3 md:ml-[1vw]"
            },
            description: "Add hyperlinked text, <Ctrl + k>"
        }
    };

    // Hanlders
    async function handle_blur() {
        emoji_matches = [];
        show_emoji_picker = false;

        caret_offset_top = null;
        caret_offset_left = null;
    }

    async function handle_input(event: Event) {
        const element = event.target as HTMLTextAreaElement;
        const input_text = element.value;
        let last_typed_word: string;

        // to get last typed word even its in middle
        const selection_start = element.selectionStart;
        if (typeof selection_start !== "number") return;

        const words_before_caret = input_text.substring(0, selection_start);
        const words_list = words_before_caret.split(/[\s\n]/);
        last_typed_word = words_list.at(-1) ?? "";

        // check if last_typed_word starts with ":" that may or may not have subsequent word characters
        const emoji_code = last_typed_word?.match(/^:(\S*)$/);
        if (!emoji_code) {
            emoji_matches = [];
            show_emoji_picker = false;

            // Caret
            caret_offset_top = null;
            caret_offset_left = null;
        } else {
            // Set first item active
            active_emoji_index = 0;

            show_emoji_picker = true;
            emoji_matches = [];

            for (const item of Object.entries(emojis).sort()) {
                const keyword = item[0];
                const emoji = item[1];
                if (keyword.includes(emoji_code[1])) {
                    emoji_matches.push({
                        emoji: emoji,
                        keyword: keyword
                    });
                }
            }

            // Popover settings
            if (caret_offset_left === null && caret_offset_top == null) {
                const textarea_position = element.getBoundingClientRect();

                // CSS
                const line_height = getComputedStyle(element).getPropertyValue("line-height");

                const caret_position = offset(element);

                // We need 2 times the line height to be actually effective.
                caret_offset_top = `calc(${caret_position.top - textarea_position.top + caret_position.height}px + (2 * ${line_height}))`;
                caret_offset_left = `calc(${caret_position.left - textarea_position.left}px)`;
            }
        }
    }

    async function handle_keydown(event: KeyboardEvent) {
        /**Emoji specific codes*/
        if (show_emoji_picker) {
            switch (event.key.toLowerCase()) {
                case "arrowup": {
                    event.preventDefault();
                    active_emoji_index = (active_emoji_index - 1 + SHOWN_EMOJI_LIMIT) % SHOWN_EMOJI_LIMIT;
                    break;
                }
                case "arrowdown": {
                    event.preventDefault();
                    active_emoji_index = (active_emoji_index + 1) % SHOWN_EMOJI_LIMIT;
                    break;
                }
                case "enter": {
                    event.preventDefault();
                    await select_emoji({ element: event.currentTarget as HTMLTextAreaElement, emoji_index: active_emoji_index });
                    break;
                }
            }
        }

        /**
         * Editor specific funtions
         * Triggered by `ctrlKey`
         */
        if (event.ctrlKey) {
            switch (event.key.toLowerCase()) {
                case "b": {
                    /** Bold Functionality */
                    event.preventDefault();
                    await bold_text(event.target as HTMLTextAreaElement);
                    break;
                }
                case "i": {
                    /** Italic functionality */
                    event.preventDefault();
                    await italic_text(event.target as HTMLTextAreaElement);
                    break;
                }
                case "e": {
                    /** Code functionality */
                    event.preventDefault();
                    await code_text(event.target as HTMLTextAreaElement);
                    break;
                }
                case "u": {
                    /** Underline functionality */
                    event.preventDefault();
                    await underline_text(event.target as HTMLTextAreaElement);
                    break;
                }
                case "k": {
                    /** Hyperlink functionality */
                    event.preventDefault();
                    await hyperlink_text(event.target as HTMLTextAreaElement);
                    break;
                }
            }
        }

        if (event.ctrlKey && event.shiftKey) {
            switch (event.key.toLowerCase()) {
                case "x":
                    event.preventDefault();
                    await strike_text(event.target as HTMLTextAreaElement);
                    break;
            }
        }
    }
    // Editor specific functions
    async function bold_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({ element: element, starting_operator: "**", ending_operator: "**" });
    }
    async function italic_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({ element: element, starting_operator: "_", ending_operator: "_" });
    }
    async function code_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({ element: element, starting_operator: "`", ending_operator: "`" });
    }
    async function underline_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({ element: element, starting_operator: "<u>", ending_operator: "</u>" });
    }
    async function strike_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({ element: element, starting_operator: "~~", ending_operator: "~~" });
    }
    async function hyperlink_text(element: HTMLTextAreaElement) {
        const selection_start = element.selectionStart,
            selection_end = element.selectionEnd,
            selection_text = element.value.substring(selection_start, selection_end);

        // Handle use cases
        if (element.value.substring(selection_start - 3, selection_start) == "[](" && element.value.substring(selection_end, selection_end + 1) == ")") {
            /**
             * [](||) -> ||
             */
            element.focus();
            element.setSelectionRange(selection_start - 3, selection_end + 1);
            document.execCommand("delete");
        } else {
            const replacement_text = `[${selection_text}]()`;
            await insert_text({ target: element, text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end) });
            element.setSelectionRange(selection_start + selection_text.length + 3, selection_start + selection_text.length + 3);
        }
    }
    async function paste_text(event: ClipboardEvent & { currentTarget: HTMLTextAreaElement }) {
        event.preventDefault();
        const element = event.currentTarget;

        const selection_start = element.selectionStart,
            selection_end = element.selectionEnd,
            selection_text = element.value.substring(selection_start, selection_end);

        const clipboard_data = event.clipboardData?.getData("text") ?? "",
            clipboard_data_contains_url = is_valid_url(clipboard_data);

        if (selection_text && clipboard_data_contains_url) {
            const replacement_text = `[${selection_text}](${clipboard_data})`;
            await insert_text({ target: element, text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end) });
            element.setSelectionRange(selection_start + replacement_text.length, selection_start + replacement_text.length);
        } else {
            const replacement_text = clipboard_data;
            await insert_text({ target: element, text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end) });
        }
    }

    // Functions
    async function insert_text({ target, text }: { target: HTMLTextAreaElement; text: string }): Promise<void> {
        /**
         * Thanks stackoverflow guy and mozilla dev ( Michal Čaplygin |myf| )
         * Stackoverflow : https://stackoverflow.com/a/56509046
         * Mozilla : https://bugzilla.mozilla.org/show_bug.cgi?id=1523270
         */
        target.select();
        document.execCommand("insertText", false, text);
    }

    async function operate_on_selected_text({ element, starting_operator, ending_operator }: { element: HTMLTextAreaElement; starting_operator: string; ending_operator: string }): Promise<void> {
        element.focus();

        const selection_start = element.selectionStart,
            selection_end = element.selectionEnd,
            selection_text = element.value.substring(selection_start, selection_end);

        const regex_pattern_for_operator = new RegExp("^" + starting_operator.replace(/[|\\{}()[\]^$+*?.]/g, "\\$&") + "|" + ending_operator.replace(/[|\\{}()[\]^$+*?.]/g, "\\$&") + "$", "g");

        // Handle use cases
        if (element.value.substring(selection_start - starting_operator.length, selection_start) == starting_operator && element.value.substring(selection_end, selection_end + ending_operator.length) == ending_operator) {
            if (selection_text) {
                /**
                 * `<starting_operator>|hello|<ending_operator>` -> `|hello|`
                 * `_|hello|_` -> `|hello|`
                 */
                const replacement_text = element.value.substring(selection_start - starting_operator.length, selection_end + ending_operator.length).replace(regex_pattern_for_operator, "");
                await insert_text({ target: element, text: element.value.substring(0, selection_start - starting_operator.length) + replacement_text + element.value.substring(selection_end + ending_operator.length) });

                element.setSelectionRange(selection_start - starting_operator.length, selection_end - starting_operator.length);
            } else {
                /**
                 * `<starting_operator>||<ending_operator>` -> `||`
                 * `_||_` -> `||`
                 */
                element.focus();
                element.setSelectionRange(selection_start - starting_operator.length, selection_end + ending_operator.length);
                document.execCommand("delete", false);
            }
        } else if (element.value.substring(selection_start, selection_start + starting_operator.length) == starting_operator && element.value.substring(selection_end - ending_operator.length, selection_end) == ending_operator) {
            /**
             * `|<starting_opeator>hello<ending_operator>|` -> `|hello|`
             * `|_hello_|` -> `|hello|`
             */

            const replacement_text = element.value.substring(selection_start - starting_operator.length, selection_end + ending_operator.length).replace(regex_pattern_for_operator, "");
            await insert_text({ target: element, text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end) });

            element.setSelectionRange(selection_start, selection_end - (starting_operator.length + ending_operator.length));
        } else {
            /**
             * `|hello|` -> `<operator>|hello|<operator>`
             * `|hello|` -> `_|hello|_`
             */
            const replacement_text = starting_operator + selection_text + ending_operator;
            await insert_text({ target: element, text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end) });
            element.setSelectionRange(selection_start + starting_operator.length, selection_end + starting_operator.length);
        }
    }

    async function select_emoji({ emoji_index, element }: { emoji_index: number; element: HTMLElement }): Promise<void> {
        const textarea_element = element as HTMLTextAreaElement;

        const emoji_keyword = emoji_matches[emoji_index]?.keyword,
            emoji_code = `:${emoji_keyword}:`;

        const selection_start = textarea_element.selectionStart,
            selection_end = textarea_element.selectionEnd;

        const text_before_selection = textarea_value.substring(0, selection_start),
            text_after_selection = textarea_value.substring(selection_end);

        // replace last word before text selection with emoji code
        const updated_text_before_selection = text_before_selection.replace(/\S+$/, emoji_code);
        await insert_text({ target: textarea_element, text: `${updated_text_before_selection} ${text_after_selection}` });

        // set caret at the end of inserted emoji_code
        const caret_position = updated_text_before_selection.length + 1;
        textarea_element.setSelectionRange(caret_position, caret_position);

        // close emoji picker
        show_emoji_picker = false;
        emoji_matches = [];

        // Caret controls
        caret_offset_left = null;
        caret_offset_top = null;
    }

    let tab_type: "edit" | "preview" = "edit";

    async function handle_edit_preview_button_click(item: string): Promise<void> {
        tab_type = item as typeof tab_type;
    }
</script>

<div class="relative rounded-lg ring-2 ring-surface-300/25 transition duration-300 focus-within:ring-primary-500 md:rounded-[0.75vw] md:ring-[0.15vw]">
    <textarea-navbar class="flex h-8 items-center justify-between overflow-hidden rounded-t-lg bg-surface-400/50 md:h-[2.5vw] md:rounded-t-[0.75vw]">
        <div>
            {#each ["edit", "preview"] as item}
                {@const active = tab_type.toLowerCase() == item}
                <button
                    type="button"
                    on:click={() => handle_edit_preview_button_click(item)}
                    class="{active ? 'bg-surface-900 text-surface-50' : 'text-surface-300'} h-8 px-5 text-xs capitalize leading-[1.5vw] transition-colors duration-100 md:h-[2.5vw] md:px-[1.5vw] md:text-[1vw]"
                >
                    {item}
                </button>
            {/each}
        </div>
        <div class="flex place-items-center gap-2 pr-4 md:gap-[0.75vw] md:pr-[1vw]">
            {#each Object.entries(icon_and_function_mapping) as item}
                {@const item_label = item[0]}

                {@const icon = item[1].icon.component}
                {@const icon_class = item[1].icon.class}
                {@const button_function = item[1].function}
                {@const description = item[1].description}

                <button
                    class="btn p-0 {icon_class}"
                    type="button"
                    aria-label={item_label}
                    use:tippy={{
                        content: `<div class='leading-2 w-max whitespace-nowrap rounded-lg bg-surface-400 px-2 py-1 text-[0.65rem] text-surface-50 md:px-[0.75vw] md:py-[0.3vw] md:text-[1vw]'>${encode(description)}</div>`,
                        allowHTML: true,
                        arrow: false,
                        offset: [0, 17],
                        appendTo: document.body,
                        animation: "shift-away",
                        theme: "elaine"
                    }}
                    on:click={() => button_function(textarea_element)}
                >
                    <svelte:component this={icon} />
                </button>
            {/each}
        </div>
    </textarea-navbar>
    <textarea-body class="block h-28 overflow-y-scroll md:h-[8vw]">
        {#if tab_type === "edit"}
            <textarea
                on:paste={(event) => paste_text(event)}
                on:input={handle_input}
                on:keydown={handle_keydown}
                on:blur={handle_blur}
                bind:value={textarea_value}
                bind:this={textarea_element}
                spellcheck="true"
                class="h-full w-full resize-none border-none bg-surface-900 p-3 text-sm leading-tight text-surface-50 outline-none duration-300 ease-in-out placeholder:text-surface-200 focus:ring-0 md:p-[1vw] md:text-[1vw] md:leading-[1.5vw]"
                placeholder="Leave a comment"
            />
        {:else if tab_type === "preview"}
            <div class="p-3 md:p-[1vw]">
                {#if textarea_value}
                    <Markdown
                        markdown={textarea_value}
                        class="h-full w-full border-none bg-surface-900 text-sm leading-tight text-surface-50 outline-none md:text-[1vw] md:leading-[1.5vw]"
                    />
                {:else}
                    <span class="text-sm leading-tight text-surface-50 md:text-[1vw] md:leading-[1.5vw]">Nothing to preview</span>
                {/if}
            </div>
        {/if}
    </textarea-body>
    <textarea-footer class="flex justify-between bg-surface-400/50 px-4 py-2 text-[0.65rem] font-thin leading-[1.5vw] text-surface-200 md:px-[1vw] md:py-[0.1vw] md:text-[0.75vw]">
        <div />
        <div>
            Learn more about
            <a
                class="underline"
                href="/"
            >
                core editor
            </a>
        </div>
    </textarea-footer>
    {#if show_emoji_picker && emoji_matches.length > 0}
        <emoji-popover
            class="emoji_picker absolute flex min-w-[12vw] flex-col divide-y divide-surface-50/10 overflow-hidden rounded-[0.5vw] bg-surface-400 text-[1vw] text-surface-50"
            style:top={caret_offset_top}
            style:left={caret_offset_left}
        >
            {#each emoji_matches as item, index}
                {#if index < SHOWN_EMOJI_LIMIT}
                    {@const emoji = item?.["emoji"] ?? ""}
                    {@const keyword = item?.["keyword"] ?? ""}

                    <div
                        role="button"
                        tabindex="0"
                        class="flex cursor-pointer items-center gap-[0.5vw] px-[0.75vw] py-[0.25vw] leading-[1.75vw] hover:bg-primary-500 hover:text-white"
                        class:bg-primary-500={active_emoji_index === index}
                        class:text-white={active_emoji_index === index}
                        on:mousedown={async (event) => await select_emoji({ emoji_index: index, element: event.currentTarget })}
                    >
                        <div class="h-[0.9vw] w-[0.9vw]">
                            <ImageLoader
                                src={emoji}
                                alt={keyword}
                                class="h-full w-full"
                            />
                        </div>
                        <span>{keyword}</span>
                    </div>
                {/if}
            {/each}
        </emoji-popover>
    {/if}
</div>
