function require_pyloid() {
    return function (target: any, context: ClassMethodDecoratorContext) {
        return function (this: any, ...args: any[]) {
            try {
                if (window.pyloid != undefined) {
                    return target.apply(this, args);
                } else {
                    return null;
                }
            } catch (error) {
                return null;
            }
        };
    };
}

export class JSApi {
    @require_pyloid()
    async get_server_port() {
        return await window.pyloid.JSApi.get_server_port();
    }
}
