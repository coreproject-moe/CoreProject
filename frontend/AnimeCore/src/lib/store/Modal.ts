import { readable } from "svelte/store";
import { v4 as uuidv4 } from "uuid";

export const modals = readable<{ navbar: string; genre: string }>({
    navbar: uuidv4(),
    genre: uuidv4()
});
