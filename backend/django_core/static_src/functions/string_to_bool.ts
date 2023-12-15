export function string_to_boolean(string: string) {
    switch (string.toLowerCase()) {
        case "true": {
            return true;
        }
        case "false": {
            return false;
        }
        default: {
            throw new Error("String is not convertable to boolean");
        }
    }
}
