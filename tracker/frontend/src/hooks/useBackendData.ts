"use client";
import useSWR from "swr";
import { API_URL } from "@/constants/url";
import { BackendData } from "@/types/api";

export const fetcher = (url: URL) => fetch(url).then((res) => res.json());

export function useBackendData() {
  const { data, error, isLoading } = useSWR<BackendData>(API_URL, fetcher);

  return {
    data: data ?? null,
    isLoading,
    isError: error,
  };
}
