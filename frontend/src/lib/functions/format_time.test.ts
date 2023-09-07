import { FormatTime } from "$functions/format_time";
import { expect, test } from "vitest";

test("format date function", () => {
    const formated_time = new FormatTime(1600);
    expect(formated_time.format_seconds_to_minutes).toBe("26");
    expect(formated_time.format_seconds_to_time_stamp_duration).toBe("26:40");
});
