<script lang="ts">
    import emojis from "./emoji.json";
    import { cn } from "../../functions/classname";
    import { vw } from "../../functions/vw";
    import { is_valid_url } from "../../functions/is_valid_url";
    import { offset } from "caret-pos";
    import { encode } from "html-entities";
    import type { SvelteComponent } from "svelte";
    import tippy from "tippy.js";
    import { reverse } from "../../functions/urls";

    // Icons import
    import Bold from "../icons/bold.svelte";
    import Italic from "../icons/italic.svelte";
    import Underline from "../icons/underline.svelte";
    import Strike from "../icons/strike.svelte";
    import Code from "../icons/code.svelte";
    import Hyperlink from "../icons/hyperlink.svelte";

    let caret_offset_top: string | null = null,
        caret_offset_left: string | null = null;

    // Textarea Bindings
    let textarea_element: HTMLTextAreaElement,
        textarea_value = "";

    let preview_element_innerHTML = "";

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
                    await select_emoji({
                        element: event.currentTarget as HTMLTextAreaElement,
                        emoji_index: active_emoji_index
                    });
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
        await operate_on_selected_text({
            element: element,
            starting_operator: "**",
            ending_operator: "**"
        });
    }
    async function italic_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({
            element: element,
            starting_operator: "_",
            ending_operator: "_"
        });
    }
    async function code_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({
            element: element,
            starting_operator: "`",
            ending_operator: "`"
        });
    }
    async function underline_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({
            element: element,
            starting_operator: "<u>",
            ending_operator: "</u>"
        });
    }
    async function strike_text(element: HTMLTextAreaElement) {
        await operate_on_selected_text({
            element: element,
            starting_operator: "~~",
            ending_operator: "~~"
        });
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
            await insert_text({
                target: element,
                text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
            });
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
            await insert_text({
                target: element,
                text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
            });
            element.setSelectionRange(selection_start + replacement_text.length, selection_start + replacement_text.length);
        } else {
            const replacement_text = clipboard_data;
            await insert_text({
                target: element,
                text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
            });
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
                await insert_text({
                    target: element,
                    text: element.value.substring(0, selection_start - starting_operator.length) + replacement_text + element.value.substring(selection_end + ending_operator.length)
                });

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
            await insert_text({
                target: element,
                text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
            });

            element.setSelectionRange(selection_start, selection_end - (starting_operator.length + ending_operator.length));
        } else {
            /**
             * `|hello|` -> `<operator>|hello|<operator>`
             * `|hello|` -> `_|hello|_`
             */
            const replacement_text = starting_operator + selection_text + ending_operator;
            await insert_text({
                target: element,
                text: element.value.substring(0, selection_start) + replacement_text + element.value.substring(selection_end)
            });
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
        await insert_text({
            target: textarea_element,
            text: `${updated_text_before_selection} ${text_after_selection}`
        });

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

    let active_tab: "edit" | "preview" = "edit";
    async function handle_tab_click(tab_name: string) {
        if (tab_name === "preview") {
            const res = await fetch(reverse("partial_markdown_endpoint"), {
                method: "POST",
                credentials: "same-origin",
                body: textarea_value,
                headers: { "X-CSRFToken": window.csrfmiddlewaretoken }
            });
            // guard clause
            if (!res.ok) return;
            const markdown_html = await res.text();
            if (textarea_value) {
                preview_element_innerHTML = markdown_html;
            } else {
                preview_element_innerHTML = "Nothing to preview!";
            }
        }
        active_tab = tab_name as typeof active_tab;
    }
</script>

<textarea-navbar class="flex items-center justify-between rounded-t-lg md:rounded-t-[0.75vw]">
    <div class="md:p-[0.25vw] md:pl-[0.3vw]">
        {#each ["edit", "preview"] as tab}
            {@const active = tab === active_tab}
            <button
                type="button"
                class={cn("btn min-h-full capitalize md:h-[2.5vw] md:text-[1vw]", active ? "btn-neutral" : "bg-secondary")}
                on:click={() => handle_tab_click(tab)}
            >
                {tab}
            </button>
        {/each}
    </div>
    <div class="flex items-center gap-2 pr-4 md:gap-[0.75vw] md:pr-[1vw]">
        {#each Object.entries(icon_and_function_mapping) as item}
            {@const item_label = item[0]}

            {@const icon = item[1].icon.component}
            {@const icon_class = item[1].icon.class}
            {@const button_function = item[1].function}
            {@const description = item[1].description}
            <div
                class="before:px-[0.5vw] before:py-[0.25vw] before:md:text-[0.9vw]"
                use:tippy={{
                    content: `<div class='leading-2 w-max whitespace-nowrap rounded-lg bg-surface-400 px-2 py-1 text-[0.65rem] text-surface-50 md:px-[0.75vw] md:py-[0.3vw] md:text-[1vw]'>${encode(description)}</div>`,
                    allowHTML: true,
                    arrow: false,
                    appendTo: document.body,
                    animation: "shift-away",
                    theme: "elaine",
                    onTrigger(instance) {
                        instance.props.offset = [0, vw(1)];
                    }
                }}
            >
                <button
                    class={cn(icon_class, "btn min-h-full border-none !bg-transparent p-0")}
                    type="button"
                    aria-label={item_label}
                    on:click={() => button_function(textarea_element)}
                >
                    <svelte:component this={icon} />
                </button>
            </div>
        {/each}
    </div>
</textarea-navbar>
{#if active_tab === "edit"}
    <textarea
        on:paste={(event) => paste_text(event)}
        on:input={handle_input}
        on:keydown={handle_keydown}
        on:blur={handle_blur}
        bind:value={textarea_value}
        bind:this={textarea_element}
        spellcheck="true"
        placeholder="Leave a comment"
        class="h-28 w-full resize-none overflow-y-scroll border-none bg-secondary px-3 text-sm leading-tight outline-none focus:ring-0 md:h-[8vw] md:px-[1vw] md:py-[0.5vw] md:text-[1vw] md:leading-[1.5vw]"
    ></textarea>
{:else if active_tab === "preview"}
    <div
        class="h-28 w-full overflow-y-scroll px-3 text-sm leading-tight md:h-[8vw] md:px-[1vw] md:py-[0.5vw] md:text-[1vw] md:leading-[1.5vw]"
        contenteditable="false"
        bind:innerHTML={preview_element_innerHTML}
    ></div>
{/if}

<textarea-footer
    class="flex items-center gap-[0.25vw] px-4 py-2 text-[0.65rem] font-thin leading-[1.5vw] text-accent md:px-[1vw] md:py-[0.1vw] md:text-[0.75vw]"
    style="align-self: flex-end;"
>
    Learn more about <a
        class="underline"
        href="/"
    >
        core editor
    </a>
</textarea-footer>
{#if show_emoji_picker && emoji_matches.length > 0}
    <emoji-popover
        class="divide-surface-50/10 bg-surface-400 text-surface-50 absolute flex min-w-[12vw] flex-col divide-y overflow-hidden rounded-[0.5vw] text-[1vw]"
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
                    class="hover:bg-primary-500 flex cursor-pointer items-center gap-[0.5vw] px-[0.75vw] py-[0.25vw] leading-[1.75vw] hover:text-white"
                    class:bg-primary-500={active_emoji_index === index}
                    class:text-white={active_emoji_index === index}
                    on:mousedown={async (event) =>
                        await select_emoji({
                            emoji_index: index,
                            element: event.currentTarget
                        })}
                >
                    <div class="h-[0.9vw] w-[0.9vw]">
                        <img
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
