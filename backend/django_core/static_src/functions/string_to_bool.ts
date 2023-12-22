export function string_to_boolean(variable: string | boolean): boolean {
    if (typeof variable === "boolean") {
        return variable;
    }

    switch (variable.toLowerCase()) {
        case "true": {
            return true;
        }
        case "false": {
            return false;
        }
        default: {
            throw new Error("variable is not convertable to boolean");
        }
    }
}
