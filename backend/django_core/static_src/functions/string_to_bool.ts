export function string_to_boolean(variable: string | boolean | null | undefined): boolean {
    if (variable === undefined) {
        return false;
    }

    if (typeof variable === "boolean") {
        return variable;
    }
    if (typeof variable === "undefined") {
        return false;
    }
    if (variable === null) {
        return false;
    }

    if (typeof variable === "string") {
        switch (variable.toLowerCase()) {
            case "true": {
                return true;
            }
            case "false": {
                return false;
            }
            default: {
                throw new Error(`${`variable`} is string but not convertable to boolean | The variable in question : ${variable}`);
            }
        }
    }
    throw new Error(`${`variable`} is neither string nor boolean and is not convertable to boolean | The variable : ${variable}`);
}
