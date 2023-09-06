import { cn } from "$functions/classnames";
import { test, expect } from "vitest";

test("check classnames", () => {
    expect(cn("w-full", "h-full")).toBe("w-full h-full");
    expect(cn("md:max-h-[1vw]", "md:hover:max-h-[10vw]")).toBe("md:max-h-[1vw] md:hover:max-h-[10vw]");
    expect(cn("px-2 py-1 bg-red hover:bg-dark-red", "p-3 bg-[#B91C1C]")).toBe("hover:bg-dark-red p-3 bg-[#B91C1C]");
});
