import { spawn } from "child_process";
import { IS_LINUX, IS_MAC, IS_WINDOWS } from "@constants/os";
import { join } from "path";

class Shiinobi {
	private get shiinobi() {
		if (IS_LINUX) {
			return join(__dirname, "../../resources/bin/", "linux/shiinobi");
		} else if (IS_WINDOWS) {
			return join(__dirname, "../../resources/bin/", "win32/shiinobi.exe");
		} else if (IS_MAC) {
			return join(__dirname, "../../resources/bin/", "darwin/shiinobi");
		} else {
			throw new Error("System architecture not supported for shiinobi");
		}
	}

	private spawn(args: string[]) {
		return new Promise((resolve, reject) => {
			const process = spawn(this.shiinobi, args);
			let output = "";

			process.stdout.on("data", (data: Buffer) => {
				output += data.toString();
			});

			process.stderr.on("data", (data: Buffer) => {
				console.error("Err: ", data.toString());
			});

			process.on("close", (code) => {
				if (code === 0) {
					try {
						const parsedJson = JSON.parse(output);
						resolve(parsedJson);
					} catch (err) {
						console.error("JSONError: ", err);
					}
				} else {
					console.error("Process exited with code: ", code);
					reject(new Error("Process exited with code: " + code));
				}
			});

			process.on("error", (err) => {
				console.log("Process err: ", err);
				reject(err);
			});
		});
	}

	public async get_staff_urls() {
		return await this.spawn(["get-staff-urls"]);
	}
}

export { Shiinobi };
