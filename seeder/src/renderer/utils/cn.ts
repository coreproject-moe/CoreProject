import { twMerge } from "tailwind-merge";

type ClassValue =
	| ClassValue[]
	| Record<string, string | number | null | boolean | undefined>
	| string
	| number
	| null
	| boolean
	| undefined;

const clsx = (...args: ClassValue[]) =>
	args.filter((arg) => arg && typeof arg === "string").join(" ");
const cn = (...classes: ClassValue[]) => twMerge(clsx(...classes));

export { cn };
