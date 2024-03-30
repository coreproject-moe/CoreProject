import tailwind from "$functions/tailwind";
import { createMediaStore } from "svelte-media-queries";

const breakpoints = tailwind.theme.screens;

type BreakpointKey = keyof typeof breakpoints;
type Breakpoints = Record<BreakpointKey, string>;

function transformBreakpointsToMediaQueries(): Breakpoints {
    const mediaQueries: Record<string, string> = {};

    // Get the keys of the breakpoints
    const breakpointKeys = Object.keys(breakpoints);

    // Loop through the breakpoints to create media queries
    for (let i = 0; i < breakpointKeys.length; i++) {
        const currentKey = breakpointKeys[i] as BreakpointKey;

        const prevKey = breakpointKeys[i - 1] as BreakpointKey;
        const nextKey = breakpointKeys[i + 1] as BreakpointKey;

        if (i == 0) {
            mediaQueries[currentKey] = `(max-width: ${breakpoints[currentKey]})`;
        } else {
            if (nextKey) {
                // For intermediate breakpoints
                mediaQueries[currentKey] = `(min-width: ${breakpoints[prevKey]}) and (max-width: ${parseInt(breakpoints[currentKey])}px)`;
            } else {
                // For the last breakpoint
                mediaQueries[currentKey] = `(min-width: ${breakpoints[currentKey]})`;
            }
        }
    }

    return mediaQueries as Breakpoints;
}

export const breakpoint = createMediaStore<Breakpoints>(transformBreakpointsToMediaQueries());
