"use client";
import useSWR from "swr";
import { API_URL } from "@/constants/url";

export const fetcher = (url: URL) => fetch(url).then((res) => res.json());

export function useBackendData() {
  const { data, error, isLoading } = useSWR(API_URL, fetcher);

  return {
    data: data,
    isLoading,
    isError: error,
  };
}
