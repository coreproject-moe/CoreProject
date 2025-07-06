export const BACKEND_HOST =
  process.env.NEXT_PUBLIC_BACKEND_HOST || "localhost:5000";

export const HTTP_ENDPOINT = `http://${BACKEND_HOST}`;
export const WS_ENDPOINT = `ws://${BACKEND_HOST}/`;

// Websocket
export const WS_TRACKER_ENDPOINT = `${WS_ENDPOINT}/announce`;

// HTTP
export const HTTP_ANNOUNCE_ENDPOINT = `${HTTP_ENDPOINT}/announce`;
export const API_URL = `${HTTP_ENDPOINT}/api`;
export const HTTP_TRACKER_ENDPOINT = `${HTTP_ENDPOINT}/http`;
