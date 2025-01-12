import { writable } from "svelte/store";
import { Comment } from "$types/comment";

export const comment_needs_update = writable(false);

export const tree_branch = writable<Array<Comment>>(new Array<Comment>());
