import * as _ from "lodash-es";
import { string_to_boolean } from "./string_to_bool";

export function get_csrf_token() {
    // Set by django
    let token: string | null = null;
    token = window.csrfmiddlewaretoken;

    if (_.isNull(token)) {
        throw new Error("There is no CSRF Token set by `django`");
    }

    return token;
}
