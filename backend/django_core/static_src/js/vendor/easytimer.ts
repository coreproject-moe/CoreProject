import { Timer as EasyTimer } from "easytimer.js";

const slider_delay = 10; // Modify this if needed

window.timer = new EasyTimer({
    target: {
        seconds: slider_delay
    },
    precision: "secondTenths"
});

window.timer.on("secondTenthsUpdated", () => {
    const time = window.timer.getTotalTimeValues().secondTenths,
        value = (100 / slider_delay) * (time / 10);

    const event = new CustomEvent("hyperscript:timer_updated", {
        detail: { value: value }
    });
    document?.querySelector("progress-bar")?.dispatchEvent(event);
});

window.timer.on("targetAchieved", () => {
    document?.querySelector("slider")?.dispatchEvent(new CustomEvent("hyperscript:slide_next"));
    window.timer.reset();
});
