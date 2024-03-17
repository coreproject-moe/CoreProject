import * as _ from "lodash-es";

export function string_to_number(variable: string | null): number {
    let number = Number(variable);
    if (_.isNaN(number)) {
        throw new Error(`${`variable`} is not convertable to number`);
    }
    return number;
}
