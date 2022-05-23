import { writable } from "svelte/store";

export const activeModal = writable({
    option: false
});
