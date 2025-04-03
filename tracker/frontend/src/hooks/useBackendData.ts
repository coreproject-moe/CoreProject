"use client";

import useSWR from "swr";
import { API_URL } from "@/constants/url";
import { fetcher } from "@/functions/fetcher";

export function useBackendData() {
  const { data, error, isLoading } = useSWR(API_URL, fetcher);

  return {
    data: data,
    isLoading,
    isError: error,
  };
}
