import { twMerge } from "tailwind-merge";

type ClassValue = ClassValue[] | Record<string, string | number | null | boolean | undefined> | string | number | null | boolean | undefined;

// Code modified from
// https://chat.openai.com/share/58feb08e-0905-4860-a309-6d75687c2e6e
const clsx = (...args: ClassValue[]) => args.filter((arg) => arg && typeof arg === "string").join(" ");
export const cn = (...classes: ClassValue[]) => twMerge(clsx(...classes));
