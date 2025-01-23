declare global {
    interface Window {
        pyloid: {
            JSApi: {
                get_server_port: () => Promise<{ host: string; port: number }>;
                start_websocket_server: () => Promise<void>;
            };
        };
    }
}

export {};
