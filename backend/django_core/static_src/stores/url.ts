import { writable } from "svelte/store";

export const url = writable(window.location.pathname);
export const previous_url = writable<string | undefined>(undefined);
