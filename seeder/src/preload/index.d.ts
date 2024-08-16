import { ElectronAPI } from "@electron-toolkit/preload";
import { COMMANDS as SHIINOBI_COMMANDS } from "$interfaces/shiinobi";

declare global {
	interface Window {
		electron: ElectronAPI;
		api: {
			get_app_version: () => Promise<string>;
			get_express_urls: () => Promise<{
				shiinobi_healthcheck: string;
				staff: string;
			}>;
			// Shiinobi
			[key in typeof SHIINOBI_COMMANDS[number]]: (...args: any[]) => Promise<object>;
		};
	}
}
