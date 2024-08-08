import { ElectronAPI } from "@electron-toolkit/preload";

declare global {
	interface Window {
		electron: ElectronAPI;
		api: {
			get_app_version: () => Promise<string>;
			// Shiinobi
			get_staff_urls: () => Promise<object>;
		};
	}
}
