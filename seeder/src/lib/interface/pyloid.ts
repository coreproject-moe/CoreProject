function require_pyloid() {
    return function (
        _: any,
        __: string,
        descriptor: TypedPropertyDescriptor<any>
    ): void | TypedPropertyDescriptor<any> {
        const originalMethod = descriptor.value;

        if (typeof originalMethod !== 'function') {
            throw new Error('Decorator can only be applied to methods.');
        }

        // Wrap the original method
        descriptor.value = function (...args: any[]) {
            try {
                if (window.pyloid !== undefined) {
                    return originalMethod.apply(this, args); // Call the original method
                } else {
                    console.warn('pyloid is undefined');
                    return null;
                }
            } catch (error) {
                console.error('Error in require_pyloid:', error);
                return null;
            }
        };

        return descriptor;
    };
}

export class JSApi {
    @require_pyloid()
    async get_server_port(): Promise<{ host: string; port: number } | null> {
        return await window.pyloid.JSApi.get_server_port();
    }

    @require_pyloid()
    async start_websocket_server(): Promise<boolean | null> {
        return await window.pyloid.JSApi.start_websocket_server();
    }
}
