"use client";

import useSWR from "swr";
import { URL } from "node:url";

const BACKEND_HOST =
  process.env.NEXT_PUBLIC_BACKEND_HOST || "http://localhost:5000";
const API_URL = `${BACKEND_HOST}/api`;

const fetcher = (url: URL) => fetch(url).then((res) => res.json());

export function useBackendData() {
  const { data, error, isLoading } = useSWR(API_URL, fetcher);

  return {
    data: data,
    isLoading,
    isError: error,
  };
}
