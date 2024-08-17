import { parentPort, workerData } from "node:worker_threads";
import { Shiinobi as _Shiinobi } from "$interfaces/shiinobi";

const port = parentPort;
if (!port) throw new Error("IllegalState");

const shiinobi = new _Shiinobi();

port.on("message", async () => {
  const _port = workerData.port;
  try {
    port.postMessage(`Listening on http://localhost:${_port}/`);
    const cmd = await shiinobi.get_myanimelist_staff_urls();
    console.log(cmd)
  } catch (err) {
    port.postMessage(`Couldnot launch express.js, reason ${err}`);
  }
});
