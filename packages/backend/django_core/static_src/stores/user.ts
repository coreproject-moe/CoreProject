import { string_to_boolean } from "$functions/string_to_bool";
import { writable } from "svelte/store";

export const user_authenticated = writable<boolean>(string_to_boolean(window.request.user.is_authenticated));
