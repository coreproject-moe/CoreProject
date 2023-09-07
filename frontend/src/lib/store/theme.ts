import { localStorageStore } from "@skeletonlabs/skeleton";
import type { Writable } from "svelte/store";

export const theme: Writable<"kokoro"> = localStorageStore("theme", "kokoro");
