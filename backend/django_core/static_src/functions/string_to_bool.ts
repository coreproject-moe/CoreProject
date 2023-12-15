export function string_to_boolean(string: string) {
    const _string = string.toLowerCase();

    if (_string === "true") return true;
    else if (_string === "false") return false;
    else throw Error("String is not convertable to boolean");
}
