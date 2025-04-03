import { URL } from "node:url";

export const fetcher = (url: URL) => fetch(url).then((res) => res.json());
