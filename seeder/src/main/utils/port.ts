import net from "net";
import { AddressInfo } from "net";

export function get_free_port() {
	return new Promise((resolve) => {
		const server = net.createServer();
		server.listen(0, () => {
			const port = (server.address() as AddressInfo)?.port; // Default to 0 if address is not AddressInfo
			server.close(() => resolve(port));
		});
	});
}
