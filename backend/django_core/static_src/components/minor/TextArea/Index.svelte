<script lang="ts">
    import * as _ from "lodash-es";
    import emojis from "../../../data/emoji.json";
    import { cn } from "$functions/classname";
    import { is_valid_url } from "$functions/is_valid_url";
    import { offset } from "caret-pos";
    import type { SvelteComponent } from "svelte";
    import Markdown from "$components/minor/Markdown/Index.svelte";
    // Icons import
    import Bold from "$icons/Bold/Index.svelte";
    import Italic from "$icons/Italic/Index.svelte";
    import Underline from "$icons/Underline/Index.svelte";
    import Strike from "$icons/Strike/Index.svelte";
    import Code from "$icons/Code/Index.svelte";
    import Hyperlink from "$icons/Hyperlink/Index.svelte";
    import { goto } from "$functions/urls";
    import { IS_CHROMIUM } from "$constants/browser";

    let caret_offset_top: string | null = null,
        caret_offset_left: string | null = null;

    // External Bindings
    export let textarea_value = "";

    // Textarea Bindings
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
                class: "w-5 md:w-[1.5vw]  text-surface-200"
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
                class: "w-5 md:w-[1.25vw] text-surface-200"
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

            for (const item of Object.entries(emojis).toSorted()) {
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
            if (_.isNull(caret_offset_left) && _.isNull(caret_offset_top)) {
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
                    active_emoji_index = (active_emoji_index - 1 + emoji_matches.length) % emoji_matches.length;
                    break;
                }
                case "arrowdown": {
                    event.preventDefault();
                    active_emoji_index = (active_emoji_index + 1) % emoji_matches.length;
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
        if (
            element.value.substring(selection_start - starting_operator.length, selection_start) == starting_operator &&
            element.value.substring(selection_end, selection_end + ending_operator.length) == ending_operator
        ) {
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
        } else if (
            element.value.substring(selection_start, selection_start + starting_operator.length) == starting_operator &&
            element.value.substring(selection_end - ending_operator.length, selection_end) == ending_operator
        ) {
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
        active_tab = tab_name as typeof active_tab;
    }
</script>

<div
    role="navigation"
    class="flex items-center justify-between rounded-t-lg md:rounded-t-[0.75vw]"
>
    <div class="md:p-[0.25vw] md:pl-[0.3vw]">
        {#each ["edit", "preview"] as tab}
            {@const active = tab === active_tab}
            <button
                type="button"
                class={cn("btn min-h-full capitalize md:h-[2.25vw] md:text-[1vw]", active ? "btn-neutral" : "bg-secondary")}
                on:click={() => handle_tab_click(tab)}
            >
                {tab}
            </button>
        {/each}
    </div>
    <div class="flex h-max items-center gap-2 pr-4 md:gap-[0.75vw] md:pr-[1vw]">
        {#each Object.entries(icon_and_function_mapping) as item}
            {@const item_label = item[0]}

            {@const icon = item[1].icon.component}
            {@const icon_class = item[1].icon.class}
            {@const button_function = item[1].function}
            {@const description = item[1].description}

            <button
                class={cn(icon_class, "btn h-max min-h-max border-none !bg-transparent p-0", "tooltip tooltip-top")}
                type="button"
                data-tip={description}
                aria-label={item_label}
                on:mouseenter={() => {}}
                on:click={() => button_function(textarea_element)}
            >
                <svelte:component this={icon} />
            </button>
        {/each}
    </div>
</div>
{#if active_tab === "edit"}
    <textarea
        on:paste|preventDefault={(event) => paste_text(event)}
        on:input={handle_input}
        on:keydown={handle_keydown}
        on:blur={handle_blur}
        bind:value={textarea_value}
        bind:this={textarea_element}
        spellcheck="true"
        placeholder="Leave a comment"
        class:scrollbar-none={IS_CHROMIUM}
        class="h-28 w-full resize-none overflow-y-scroll border-none bg-secondary px-3 text-sm leading-tight outline-none focus:ring-0 md:h-[8vw] md:px-[1vw] md:py-[0.5vw] md:text-[1vw] md:leading-[1.5vw]"
    ></textarea>
{:else if active_tab === "preview"}
    <div class="h-28 w-full overflow-y-scroll px-3 text-sm leading-tight md:h-[8vw] md:px-[1vw] md:py-[0.5vw] md:text-[1vw] md:leading-[1.5vw] [&_img]:inline-flex [&_img]:w-[1.25vw]">
        {#if textarea_value}
            <Markdown markdown={textarea_value} />
        {:else}
            Nothing to preview!
        {/if}
    </div>
{/if}

<div
    class="flex items-center gap-[0.25vw] px-4 py-2 text-[0.65rem] font-thin leading-[1.5vw] text-accent md:px-[1vw] md:py-[0.1vw] md:text-[0.75vw]"
    style="align-self: flex-end;"
>
    Learn more about
    <button class="underline">core editor</button>
</div>
{#if show_emoji_picker && !_.isEmpty(emoji_matches)}
    <div
        class="absolute flex min-w-[12vw] flex-col divide-y divide-accent/10 overflow-hidden rounded-[0.5vw] bg-neutral text-[1vw] text-accent"
        style:top={caret_offset_top}
        style:left={caret_offset_left}
    >
        {#each emoji_matches.slice(0, SHOWN_EMOJI_LIMIT) as item, index}
            {@const emoji = item?.["emoji"] ?? ""}
            {@const keyword = item?.["keyword"] ?? ""}

            <div
                role="button"
                tabindex="0"
                class="flex cursor-pointer items-center gap-[0.5vw] px-[0.75vw] py-[0.25vw] leading-[1.75vw] hover:bg-primary hover:text-accent"
                class:bg-primary={active_emoji_index === index}
                class:text-accent={active_emoji_index === index}
                on:mouseenter={() => (active_emoji_index = index)}
                on:mousedown={async () => {
                    await select_emoji({
                        emoji_index: index,
                        element: textarea_element
                    });
                }}
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
        {/each}
    </div>
{/if}
