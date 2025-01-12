import solid from "eslint-plugin-solid";
import path from "node:path";
import { fileURLToPath } from "node:url";
import js from "@eslint/js";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
	baseDirectory: __dirname,
	recommendedConfig: js.configs.recommended,
	allConfig: js.configs.all
});

export default [
	{
		ignores: ["**/node_modules", "**/dist", "**/out", "**/.gitignore"]
	},
	...compat.extends(
		"eslint:recommended",
		"plugin:solid/typescript",
		"@electron-toolkit/eslint-config-ts/recommended",
		"@electron-toolkit/eslint-config-prettier"
	),
	{
		plugins: {
			solid
		},

		rules: {
			"@typescript-eslint/explicit-function-return-type": "off"
		}
	}
];
