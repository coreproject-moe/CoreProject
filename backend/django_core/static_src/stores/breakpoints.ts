import tailwind from "$functions/tailwind";
import { createMediaStore } from "svelte-media-queries";

const breakpoints = tailwind.theme.screens;

type BreakpointKey = keyof typeof breakpoints;
type Breakpoints = Record<BreakpointKey, string>;

function transformBreakpointsToMediaQueries(): Breakpoints {
    const mediaQueries = {};

    const keys = Object.keys(breakpoints);
    const values = Object.values(breakpoints);

    for (let i = 0; i < keys.length; i++) {
        mediaQueries[keys[i]] = `(min-width: ${values[i]})`;
    }

    return mediaQueries as Breakpoints;
}

console.log(transformBreakpointsToMediaQueries());
export const breakpoint = createMediaStore<Breakpoints>(transformBreakpointsToMediaQueries());
