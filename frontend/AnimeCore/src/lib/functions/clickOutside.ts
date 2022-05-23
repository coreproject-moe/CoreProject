export function clickOutside(element: HTMLElement, callbackFunction: CallableFunction) {
    function onClick(event: Event) {
        if (!element?.contains(event?.target as HTMLElement)) {
            callbackFunction();
        }
    }

    document.body.addEventListener("click", onClick);

    return {
        update(newCallbackFunction: CallableFunction) {
            callbackFunction = newCallbackFunction;
        },
        destroy() {
            document.body.removeEventListener("click", onClick);
        }
    };
}
