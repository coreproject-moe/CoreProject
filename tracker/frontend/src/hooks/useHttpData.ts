"use client";

import useSWR from "swr";
import { BACKEND_HOST } from "@/constants/url";

// Fake url: http://localhost:5000/?info_hash=%234筗%E1%83{r%DD^%1a%0a%F2%03%D0%D9l%DBj&peer_id=-qB5040-6CdLzJpk(Zrn&port=52629&uploaded=0&downloaded=0&left=0&corrupt=0&key=A7E1171F&event=started&numwant=200&compact=1&no_peer_id=1&supportcrypto=1&redundant=0
export const fetcher = (url: URL) => fetch(url).then((res) => res.text());

const URL = `${BACKEND_HOST}/?info_hash=%234筗%E1%83{r%DD^%1a%0a%F2%03%D0%D9l%DBj&peer_id=-qB5040-6CdLzJpk(Zrn&port=52629&uploaded=0&downloaded=0&left=0&corrupt=0&key=A7E1171F&event=started&numwant=200&compact=1&no_peer_id=1&supportcrypto=1&redundant=0`;
export function useHttpData() {
  const { data, error, isLoading } = useSWR(URL, fetcher);

  return {
    data: data,
    isLoading: isLoading,
    isError: error,
  };
}
