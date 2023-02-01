import { writable } from "svelte/store";

export const timer = writable<"start" | "pause" | "reset">("start");
