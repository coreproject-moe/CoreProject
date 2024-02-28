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
        const currentValue = breakpoints[currentKey];
        const nextKey = breakpointKeys[i + 1] as BreakpointKey;

        if (nextKey) {
            // For intermediate breakpoints
            mediaQueries[currentKey] = `(min-width: ${currentValue}) and (max-width: ${breakpoints[nextKey]})`;
        } else {
            // For the last breakpoint
            mediaQueries[currentKey] = `(max-width: ${currentValue})`;
        }
    }

    return mediaQueries as Breakpoints;
}
console.log(transformBreakpointsToMediaQueries());

export const breakpoint = createMediaStore<Breakpoints>(transformBreakpointsToMediaQueries());
