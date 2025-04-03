export const BACKEND_HOST =
  process.env.NEXT_PUBLIC_BACKEND_HOST || "localhost:5000";

export const HTTP_ENDPOINT = `http://${BACKEND_HOST}`;
export const WS_ENDPOINT = `ws://${BACKEND_HOST}/`;

export const API_URL = `${BACKEND_HOST}/api`;
export const HTTP_TRACKER_ENDPOINT = `${BACKEND_HOST}/http`;
