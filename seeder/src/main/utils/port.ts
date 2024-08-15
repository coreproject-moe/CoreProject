import net, { AddressInfo } from "node:net";
import find from "local-devices";

// Range : 49152 – 65535
const PORT_START = 49152,
	PORT_END = 65535;

export function get_free_port() {
	return new Promise((resolve, reject) => {
		const server = net.createServer();
		let port = Math.floor(Math.random() * (PORT_END - PORT_START + 1)) + PORT_START;

		// Try to listen on a random port within the range
		server.listen(port, () => {
			port = (server.address() as AddressInfo)?.port;
			server.close(() => resolve(port));
		});

		// Handle errors (e.g., port already in use)
		server.on("error", () => {
			// Retry with another port if the current one is unavailable
			get_free_port().then(resolve).catch(reject);
		});
	});
}
export async function get_all_devices_running_shiinobi() {
	const friends = new Array<string>();
	const devices = await find();

	for (const device of devices) {
		for (let i = PORT_START; i < PORT_END; i++) {
			const URL = `https://${device.ip}/shiinobi-healthcheck`;
			const res = await fetch(URL);
			const text = await res.text();
			if (text === "We are friends") {
				friends.push(device.ip);
			}
		}
	}
}
