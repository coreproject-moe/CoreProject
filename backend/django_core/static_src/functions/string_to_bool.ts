import { isBoolean } from "lodash";

export function string_to_boolean(variable: string | boolean): boolean {
    if (isBoolean(variable)) {
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
