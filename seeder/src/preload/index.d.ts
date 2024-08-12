import { ElectronAPI } from "@electron-toolkit/preload";
import { COMMANDS as SHIINOBI_COMMANDS } from "$interfaces/shiinobi";

declare global {
	interface Window {
		electron: ElectronAPI;
		api: {
			get_app_version: () => Promise<string>;
			// Shiinobi
			[key in typeof SHIINOBI_COMMANDS[number]]: () => Promise<object>;
		};
	}
}
