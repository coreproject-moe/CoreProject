import { readable } from "svelte/store";
import { v4 as uuidv4 } from "uuid";

export const modals = readable<{ genre: string; search: string }>({
    genre: uuidv4(),
    search: uuidv4()
});
