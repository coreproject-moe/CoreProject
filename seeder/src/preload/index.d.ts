import { ElectronAPI } from "@electron-toolkit/preload";

declare global {
	interface Window {
		electron: ElectronAPI;
		api: {
			get_staff_urls: () => Promise<any>;
		};
	}
}
