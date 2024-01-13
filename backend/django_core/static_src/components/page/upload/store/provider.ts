import { persist, createIndexedDBStorage } from "@macfja/svelte-persistent-store";
import { writable } from "svelte/store";

export let provider = persist(
    writable({
        doodstream: ""
    }),
    createIndexedDBStorage(),
    "provider"
);
