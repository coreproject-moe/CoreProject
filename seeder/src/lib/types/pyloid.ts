import type { PromiseMethods } from '$lib/types/promise';

interface _PyloidJSApi {
    get_server_port: () => { host: string; port: number };
    start_websocket_server: () => boolean;
}

export type PyloidJSApi = PromiseMethods<_PyloidJSApi>;
