import { twMerge } from "tailwind-merge";

type ClassValue =
	| ClassValue[]
	| Record<string, string | number | null | boolean | undefined>
	| string
	| number
	| null
	| boolean
	| undefined;

const clsx = (...args: ClassValue[]): string =>
	args.filter((arg) => arg && typeof arg === "string").join(" ");
export const cn = (...classes: ClassValue[]): string => twMerge(clsx(...classes));
