import { writable } from "svelte/store";

export const url = writable(window.location.pathname);
