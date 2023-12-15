export function string_to_boolean(string: string) {
    const _string = string.toLowerCase();
    switch (_string) {
        case "true": {
            return true;
        }
        case "false": {
            return false;
        }
        default: {
            throw Error("String is not convertable to boolean");
        }
    }
}
