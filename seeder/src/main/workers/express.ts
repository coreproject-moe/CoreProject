import { parentPort, workerData } from "node:worker_threads";
import { app } from "$backend/index";

const port = parentPort;
if (!port) throw new Error("IllegalState");

port.on("message", () => {
	const _port = workerData.port;
	try {
		app.listen(_port, () => {
			port.postMessage(`Listening on http://localhost:${_port}/`);
		});
	} catch (err) {
		port.postMessage(`Couldnot launch express.js, reason ${err}`);
	}
});
