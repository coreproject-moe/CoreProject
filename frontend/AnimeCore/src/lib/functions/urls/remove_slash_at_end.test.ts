import { remove_slash_from_end } from "$functions/urls/remove_slash_at_end";
import { test, expect } from "vitest";

test("remove trailing slash", () => {
    expect(remove_slash_from_end("https://hello.world/remove_slash_from_end/")).toBe("https://hello.world/remove_slash_from_end");
});
