import { parentPort, workerData } from "node:worker_threads";
import { Shiinobi as _Shiinobi } from "$interfaces/shiinobi";

const port = parentPort;
if (!port) throw new Error("IllegalState");

const shiinobi = new _Shiinobi();

port.on("message", () => {
	const _port = workerData.port;
	try {
		// @ts-ignore
		const cmd = shiinobi.get_myanimelist_staff_urls();
	} catch (err) {
		port.postMessage(`Couldnot launch express.js, reason ${err}`);
	}
});
