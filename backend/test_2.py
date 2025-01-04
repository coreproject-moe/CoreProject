import bencodepy
import hashlib


def get_info_hash(torrent_file_path):
    # Load the .torrent file
    torrent_data = bencodepy.decode_from_file(torrent_file_path)

    # Extract the 'info' dictionary from the torrent metadata
    info_dict = torrent_data[b"info"]

    # Serialize the 'info' dictionary
    info_bytes = bencodepy.encode(info_dict)

    # Calculate the SHA1 hash of the serialized info dictionary
    info_hash = hashlib.sha1(info_bytes).hexdigest()

    return info_hash


# Example usage
torrent_file_path = "pyproject.toml.torrent"  # Replace with the path to your torrent file
info_hash = get_info_hash(torrent_file_path)
print(f"Info Hash: {info_hash}")
