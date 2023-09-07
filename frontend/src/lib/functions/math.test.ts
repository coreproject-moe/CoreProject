import { round_to_nearest_zero_point_five } from "$functions/math";
import { expect, test } from "vitest";

test("format date function", () => {
    expect(round_to_nearest_zero_point_five(3.85)).toBe(4);
    expect(round_to_nearest_zero_point_five(3.25)).toBe(3.5);
    expect(round_to_nearest_zero_point_five(3.1)).toBe(3);
});
