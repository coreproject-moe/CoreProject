import tailwind from "$functions/tailwind";
import { createMediaStore } from "svelte-media-queries";

const breakpoints = tailwind.theme.screens;

type BreakpointKey = keyof typeof breakpoints;

export const breakpoint = createMediaStore({});

console.log(tailwind.theme.screens);
