import { offset } from 'caret-pos';

import emojis from './emoji.json' assert { type: 'json' };

let textarea_value = '',
    caret_offset_top: string | null = null,
    caret_offset_left: string | null = null;

// Bindings
let textarea_element: HTMLTextAreaElement | null = document.querySelector('textarea');

let emoji_matches: { emoji: string; keyword: string }[],
    show_emoji_picker = false,
    active_emoji_index: number,
    SHOWN_EMOJI_LIMIT = 5;

// Hanlders
async function handle_blur() {
    emoji_matches = [];
    show_emoji_picker = false;

    caret_offset_top = null;
    caret_offset_left = null;
}

async function handle_input(event: Event) {
    const element = event.target as HTMLTextAreaElement;
    const input_text = element?.value;
    let last_typed_word;

    // to get last typed word even its in middle
    const selection_start = element.selectionStart;
    if (typeof selection_start !== 'number') return;

    const words_before_caret = input_text.substring(0, selection_start);
    const words_list = words_before_caret.split(/[\s\n]/);
    last_typed_word = words_list.at(-1) ?? '';

    // check if last_typed_word starts with ":" that may or may not have subsequent word characters
    const emoji_code = last_typed_word?.match(/^:(\S*)$/);
    if (!emoji_code) {
        emoji_matches = [];
        show_emoji_picker = false;

        // Caret
        caret_offset_top = null;
        caret_offset_left = null;

        // remove emoji popover element
        document.querySelector("custom-emoji-popover")?.remove();
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
                    keyword: keyword,
                });
            }
        }

        // Popover settings
        if (caret_offset_left === null && caret_offset_top == null) {
            const textarea_position = element.getBoundingClientRect();

            // CSS
            const line_height =
                getComputedStyle(element).getPropertyValue('line-height');

            const caret_position = offset(element);

            // We need 2 times the line height to be actually effective.
            caret_offset_top = `calc(${
                caret_position.top -
                textarea_position.top +
                caret_position.height
            }px + (2 * ${line_height}))`;
            caret_offset_left = `calc(${
                caret_position.left - textarea_position.left
            }px)`;
        }
        
        // show emoji popover
        emoji_popover();
    }
}

async function emoji_popover() {
    // emoji popover logics
    let custom_emoji_popover: HTMLElement | null = document.querySelector("custom-emoji-popover");

    if (!custom_emoji_popover) {
        custom_emoji_popover = document.createElement("custom-emoji-popover");
        textarea_element?.parentElement?.appendChild(custom_emoji_popover)
    }

    custom_emoji_popover.className = "absolute min-w-[12vw] flex-col divide-y divide-accent/10 overflow-hidden rounded-[0.5vw] bg-neutral text-[1vw]";
    custom_emoji_popover.style.position = "absolute"; // make sure its absolute
    custom_emoji_popover.style.top = caret_offset_top!;
    custom_emoji_popover.style.left = caret_offset_left!;

    // remove children for inserting new ones
    custom_emoji_popover.replaceChildren();

    emoji_matches.slice(0, 5).forEach((emoji, index) => {
        let child_el = document.createElement("div");
        child_el.className = 'flex cursor-pointer items-center gap-[0.5vw] px-[0.75vw] py-[0.25vw] leading-[1.75vw] hover:bg-primary-500 hover:text-white';
        child_el.innerHTML = `
            <img
                class='md:w-[1vw]'
                src=${emoji.emoji}
            >
            <span>${emoji.keyword}</span>
        `;

        // check active
        if (index === active_emoji_index) {
            child_el.classList.add("bg-primary", "text-white");
        };
        custom_emoji_popover?.appendChild(child_el);
    });
};

async function handle_keydown(event: KeyboardEvent) {
    /** Emoji specific codes */
    if (show_emoji_picker) {
        switch (event.key.toLowerCase()) {
            case 'arrowup': {
                event.preventDefault();
                active_emoji_index =
                    (active_emoji_index - 1 + SHOWN_EMOJI_LIMIT) %
                    SHOWN_EMOJI_LIMIT;
                emoji_popover();
                break;
            }
            case 'arrowdown': {
                event.preventDefault();
                active_emoji_index =
                    (active_emoji_index + 1) % SHOWN_EMOJI_LIMIT;
                emoji_popover();
                break;
            }
            case 'enter': {
                event.preventDefault();
                await select_emoji({
                    element: event.currentTarget as HTMLTextAreaElement,
                    emoji_index: active_emoji_index,
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
            case 'b': {
                /** Bold Functionality */
                event.preventDefault();
                await bold_text(event.target as HTMLTextAreaElement);
                break;
            }
            case 'i': {
                /** Italic functionality */
                event.preventDefault();
                await italic_text(event.target as HTMLTextAreaElement);
                break;
            }
            case 'e': {
                /** Code functionality */
                event.preventDefault();
                await code_text(event.target as HTMLTextAreaElement);
                break;
            }
            case 'u': {
                /** Underline functionality */
                event.preventDefault();
                await underline_text(event.target as HTMLTextAreaElement);
                break;
            }
            case 'k': {
                /** Hyperlink functionality */
                event.preventDefault();
                await hyperlink_text(event.target as HTMLTextAreaElement);
                break;
            }
        }
    }

    if (event.ctrlKey && event.shiftKey) {
        switch (event.key.toLowerCase()) {
            case 'x':
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
        starting_operator: '**',
        ending_operator: '**',
    });
}

async function italic_text(element: HTMLTextAreaElement) {
    await operate_on_selected_text({
        element: element,
        starting_operator: '_',
        ending_operator: '_',
    });
}

async function code_text(element: HTMLTextAreaElement) {
    await operate_on_selected_text({
        element: element,
        starting_operator: '`',
        ending_operator: '`',
    });
}

async function underline_text(element: HTMLTextAreaElement) {
    await operate_on_selected_text({
        element: element,
        starting_operator: '<u>',
        ending_operator: '</u>',
    });
}

async function strike_text(element: HTMLTextAreaElement) {
    await operate_on_selected_text({
        element: element,
        starting_operator: '~~',
        ending_operator: '~~',
    });
}

async function hyperlink_text(element: HTMLTextAreaElement) {
    const selection_start = element.selectionStart,
        selection_end = element.selectionEnd,
        selection_text = element.value.substring(
            selection_start,
            selection_end
        );

    // Handle use cases
    if (
        element.value.substring(selection_start - 3, selection_start) ==
            '[](' &&
        element.value.substring(selection_end, selection_end + 1) == ')'
    ) {
        /**
         * [](||) -> ||
         */
        element.focus();
        element.setSelectionRange(selection_start - 3, selection_end + 1);
        document.execCommand('delete');
    } else {
        const replacement_text = `[${selection_text}]()`;
        await insert_text({
            target: element,
            text:
                element.value.substring(0, selection_start) +
                replacement_text +
                element.value.substring(selection_end),
        });
        element.setSelectionRange(
            selection_start + selection_text.length + 3,
            selection_start + selection_text.length + 3
        );
    }
}

async function paste_text(event: ClipboardEvent) {
    event.preventDefault();
    const element = event.currentTarget as HTMLTextAreaElement;

    const selection_start = element.selectionStart,
        selection_end = element.selectionEnd,
        selection_text = element.value.substring(
            selection_start,
            selection_end
        );

    const clipboard_data = event.clipboardData?.getData('text') ?? '',
        clipboard_data_contains_url = is_valid_url(clipboard_data);

    if (selection_text && clipboard_data_contains_url) {
        const replacement_text = `[${selection_text}](${clipboard_data})`;
        await insert_text({
            target: element,
            text:
                element.value.substring(0, selection_start) +
                replacement_text +
                element.value.substring(selection_end),
        });
        element.setSelectionRange(
            selection_start + replacement_text.length,
            selection_start + replacement_text.length
        );
    } else {
        const replacement_text = clipboard_data;
        await insert_text({
            target: element,
            text:
                element.value.substring(0, selection_start) +
                replacement_text +
                element.value.substring(selection_end),
        });
    }
}

// Functions
async function insert_text({
    target,
    text,
}: {
    target: HTMLTextAreaElement;
    text: string;
}) {
    /**
     * Thanks stackoverflow guy and mozilla dev ( Michal Čaplygin |myf| )
     * Stackoverflow : https://stackoverflow.com/a/56509046
     * Mozilla : https://bugzilla.mozilla.org/show_bug.cgi?id=1523270
     */
    target.select();
    document.execCommand('insertText', false, text);
}

async function operate_on_selected_text({
    element,
    starting_operator,
    ending_operator,
}: {
    element: HTMLTextAreaElement;
    starting_operator: string;
    ending_operator: string;
}) {
    element.focus();

    const selection_start = element.selectionStart,
        selection_end = element.selectionEnd,
        selection_text = element.value.substring(
            selection_start,
            selection_end
        );

    const regex_pattern_for_operator = new RegExp(
        '^' +
            starting_operator.replace(/[|\\{}()[\]^$+*?.]/g, '\\$&') +
            '|' +
            ending_operator.replace(/[|\\{}()[\]^$+*?.]/g, '\\$&') +
            '$',
        'g'
    );

    // Handle use cases
    if (
        element.value.substring(
            selection_start - starting_operator.length,
            selection_start
        ) == starting_operator &&
        element.value.substring(
            selection_end,
            selection_end + ending_operator.length
        ) == ending_operator
    ) {
        if (selection_text) {
            /**
             * `<starting_operator>|hello|<ending_operator>` -> `|hello|`
             * `_|hello|_` -> `|hello|`
             */
            const replacement_text = element.value
                .substring(
                    selection_start - starting_operator.length,
                    selection_end + ending_operator.length
                )
                .replace(regex_pattern_for_operator, '');
            await insert_text({
                target: element,
                text:
                    element.value.substring(
                        0,
                        selection_start - starting_operator.length
                    ) +
                    replacement_text +
                    element.value.substring(
                        selection_end + ending_operator.length
                    ),
            });

            element.setSelectionRange(
                selection_start - starting_operator.length,
                selection_end - starting_operator.length
            );
        } else {
            /**
             * `<starting_operator>||<ending_operator>` -> `||`
             * `_||_` -> `||`
             */
            element.focus();
            element.setSelectionRange(
                selection_start - starting_operator.length,
                selection_end + ending_operator.length
            );
            document.execCommand('delete', false);
        }
    } else if (
        element.value.substring(
            selection_start,
            selection_start + starting_operator.length
        ) == starting_operator &&
        element.value.substring(
            selection_end - ending_operator.length,
            selection_end
        ) == ending_operator
    ) {
        /**
         * `|<starting_opeator>hello<ending_operator>|` -> `|hello|`
         * `|_hello_|` -> `|hello|`
         */

        const replacement_text = element.value
            .substring(
                selection_start - starting_operator.length,
                selection_end + ending_operator.length
            )
            .replace(regex_pattern_for_operator, '');
        await insert_text({
            target: element,
            text:
                element.value.substring(0, selection_start) +
                replacement_text +
                element.value.substring(selection_end),
        });

        element.setSelectionRange(
            selection_start,
            selection_end - (starting_operator.length + ending_operator.length)
        );
    } else {
        /**
         * `|hello|` -> `<operator>|hello|<operator>`
         * `|hello|` -> `_|hello|_`
         */
        const replacement_text =
            starting_operator + selection_text + ending_operator;
        await insert_text({
            target: element,
            text:
                element.value.substring(0, selection_start) +
                replacement_text +
                element.value.substring(selection_end),
        });
        element.setSelectionRange(
            selection_start + starting_operator.length,
            selection_end + starting_operator.length
        );
    }
}

async function select_emoji({
    element,
    emoji_index,
}: {
    element: HTMLTextAreaElement;
    emoji_index: number;
}) {
    const emoji_keyword = emoji_matches[emoji_index]?.keyword,
        emoji_code = `:${emoji_keyword}:`;

    const selection_start = element.selectionStart,
        selection_end = element.selectionEnd;

    const text_before_selection = textarea_value.substring(0, selection_start),
        text_after_selection = textarea_value.substring(selection_end);

    // replace last word before text selection with emoji code
    const updated_text_before_selection = text_before_selection.replace(
        /\S+$/,
        emoji_code
    );
    await insert_text({
        target: element,
        text: `${updated_text_before_selection} ${text_after_selection}`,
    });

    // set caret at the end of inserted emoji_code
    const caret_position = updated_text_before_selection.length + 1;
    element.setSelectionRange(caret_position, caret_position);

    // close emoji picker
    show_emoji_picker = false;
    emoji_matches = [];

    // Caret controls
    caret_offset_left = null;
    caret_offset_top = null;
}

function is_valid_url(url_string: string): boolean {
    // Credit : https://stackoverflow.com/a/43467144
    try {
        const url = new URL(url_string);
        return url.protocol === 'http:' || url.protocol === 'https:';
    } catch (_) {
        return false;
    }
}

// Add events
if (textarea_element) {
    textarea_element.addEventListener('input', (event) => handle_input(event));
    textarea_element.addEventListener('paste', (event) => paste_text(event));
    textarea_element.addEventListener("keydown", (event) => handle_keydown(event));

    document
        .querySelector(`[data-action='bold']`)
        ?.addEventListener(
            'click',
            async () => await bold_text(textarea_element!)
        );
    document
        .querySelector(`[data-action='italic']`)
        ?.addEventListener(
            'click',
            async () => await italic_text(textarea_element!)
        );
    document
        .querySelector(`[data-action='underline']`)
        ?.addEventListener(
            'click',
            async () => await underline_text(textarea_element!)
        );
    document
        .querySelector(`[data-action='strike']`)
        ?.addEventListener(
            'click',
            async () => await strike_text(textarea_element!)
        );
    document
        .querySelector(`[data-action='code']`)
        ?.addEventListener(
            'click',
            async () => await code_text(textarea_element!)
        );
    document
        .querySelector(`[data-action='hyperlink']`)
        ?.addEventListener(
            'click',
            async () => await hyperlink_text(textarea_element!)
        );
}
