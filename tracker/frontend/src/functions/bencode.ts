import bencode from "bencode";

export function isDataBencoded(data: string) {
  try {
    bencode.decode(Buffer.from(data));
    return true;
  } catch {
    return false;
  }
}
