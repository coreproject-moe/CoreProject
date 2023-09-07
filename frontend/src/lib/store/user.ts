import type { Writable } from "svelte/store";
import { writable } from "svelte/store";

export const is_authenticated: Writable<boolean> = writable(true);
