# create_torrent.py
import bencodepy
import hashlib
import os


def create_torrent(file_path, announce_url):
    with open(file_path, "rb") as f:
        file_data = f.read()

    pieces = []
    piece_length = 262144  # 256 KB per piece
    for i in range(0, len(file_data), piece_length):
        pieces.append(hashlib.sha1(file_data[i : i + piece_length]).digest())

    info = {
        "name": os.path.basename(file_path),
        "length": len(file_data),
        "piece length": piece_length,
        "pieces": b"".join(pieces),
    }

    torrent = {"announce": announce_url, "info": info}

    torrent_file = f"{file_path}.torrent"
    with open(torrent_file, "wb") as f:
        f.write(bencodepy.encode(torrent))
    print(f"info: {info}")
    return torrent_file


# Usage
announce_url = "http://127.0.0.1:9000/torrent/announce/"
file_path = "pyproject.toml"  # Replace with your file
torrent_file = create_torrent(file_path, announce_url)
print(f"Torrent file created: {torrent_file}")
