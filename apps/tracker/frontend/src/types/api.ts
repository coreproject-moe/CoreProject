export interface BackendData {
  quart_version: string;
  redis_version: {
    client: string;
    server: string;
  };
  python_version: string;
  redis_data: {
    [infoHash: string]: {
      [peerAddress: string]: string;
    };
  };
}

export interface RedisData {
  info_hash: string;
  type: "http" | "udp";
  peer_id: string;
  peer_ip: string;
  port: number;
  left: number | null;
}
