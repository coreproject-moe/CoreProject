export const BACKEND_HOST =
  process.env.NEXT_PUBLIC_BACKEND_HOST || "http://localhost:5000";
export const API_URL = `${BACKEND_HOST}/api`;

export const HTTP_ENDPOINT = `${BACKEND_HOST}/http`;
export const WS_ENDPOINT = `${BACKEND_HOST}/ws`;
