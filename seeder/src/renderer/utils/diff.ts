import { Change } from "diff";

export const hasDiff = (diff: { [key: string]: Change[] }) =>
	Object.values(diff).some((field) => field.some((part) => part.added || part.removed));
