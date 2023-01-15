import { writable } from "svelte/store";

export const navbar_variant = writable<"black" | "white" | "">("");

navbar_variant.subscribe((value) => {
    console.log(value);
});
