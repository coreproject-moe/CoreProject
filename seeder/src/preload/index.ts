import { contextBridge, ipcRenderer } from "electron";
import { electronAPI } from "@electron-toolkit/preload";
import { COMMANDS as SHIINOBI_COMMANDS } from "$interfaces/shiinobi";

// Custom APIs for renderer
const api = {
	get_app_version: () => ipcRenderer.invoke("get-app-version")
};

SHIINOBI_COMMANDS.forEach((item) => {
	const function_name = item.replaceAll("-", "_");
	api[function_name] = () => ipcRenderer.invoke(function_name);
});

// Use `contextBridge` APIs to expose Electron APIs to
// renderer only if context isolation is enabled, otherwise
// just add to the DOM global.
if (process.contextIsolated) {
	try {
		contextBridge.exposeInMainWorld("electron", electronAPI);
		contextBridge.exposeInMainWorld("api", api);
	} catch (error) {
		console.error(error);
	}
} else {
	// @ts-ignore (define in dts)
	window.electron = electronAPI;
	// @ts-ignore (define in dts)
	window.api = api;
}
