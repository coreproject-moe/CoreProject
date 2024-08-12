import { spawn } from "node:child_process";
import { IS_LINUX, IS_MAC, IS_WINDOWS } from "$constants/os";
import { join } from "path";
import { isEmpty } from "lodash-es";

export const COMMANDS = [
	"get-myanimelist-anime-explicit-genres",
	"get-myanimelist-anime-genres",
	"get-myanimelist-anime-themes",
	"get-myanimelist-anime-urls",
	"get-myanimelist-character-urls",
	"get-myanimelist-demographics",
	"get-myanimelist-specific-anime-character-and-staff-list-information",
	"get-myanimelist-specific-anime-genre-information",
	"get-myanimelist-specific-anime-information",
	"get-myanimelist-specific-character-information",
	"get-myanimelist-specific-producer-information",
	"get-myanimelist-specific-staff-information",
	"get-myanimelist-staff-urls"
];

class Shiinobi {
	constructor() {
		COMMANDS.forEach((command) => {
			this[command.replaceAll("-", "_")] = async (...args: any[]) => {
				const id = args[0];
				return await this.#spawn({ command, id: id });
			};
		});
	}

	get #shiinobi() {
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

	#spawn({ command, id }: { command: (typeof COMMANDS)[0]; id?: number }) {
		const _command: string[] = [command];
		if (!isEmpty(id)) _command.push(String(id));

		return new Promise((resolve, reject) => {
			const process = spawn(this.#shiinobi, _command);
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
}

export { Shiinobi };
