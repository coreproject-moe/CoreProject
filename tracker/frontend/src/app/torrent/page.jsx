"use client";
import { useState, useEffect, useRef } from "react";
// @ts-ignore
import WebTorrent from "webtorrent/dist/webtorrent.min.js";

const trackerURLs = ["ws://127.0.0.1:5000"];

export default function TorrentComponent() {
  const [status, setStatus] = useState("Ready");
  const [downloads, setDownloads] = useState(new Array());
  const clientRef = useRef(null);
  const [magnetUri, setMagnetUri] = useState("");

  // Initialize WebTorrent client
  useEffect(() => {
    if (typeof window !== "undefined") {
      clientRef.current = new WebTorrent();

      return () => {
        if (clientRef.current) {
          clientRef.current.destroy();
          clientRef.current = null;
        }
        // Cleanup Blob URLs
        downloads.forEach(({ url }) => URL.revokeObjectURL(url));
      };
    }
  }, []);

  const handleSeed = async () => {
    if (!clientRef.current) return;

    setStatus("Creating seed...");
    try {
      const file = new File(["Hello from WebTorrent!"], "test-file.txt", {
        type: "text/plain",
      });

      clientRef.current.seed(file, { announce: trackerURLs }, (torrent) => {
        setStatus(`Seeding: ${torrent.infoHash}`);
        setMagnetUri(torrent.magnetURI);

        navigator.clipboard.writeText(torrent.magnetURI);
        console.log("Magnet URI copied to clipboard:", torrent.magnetURI);

        torrent.on("upload", (bytes) => {
          console.log(`Uploaded ${bytes} bytes`);
        });

        torrent.on("wire", (wire) => {
          console.log("Connected to peer:", wire.remoteAddress);
        });
      });
    } catch (error) {
      console.error("Seeding failed:", error);
      setStatus("Seeding failed");
    }
  };

  const handleDownload = () => {
    if (!clientRef.current) return;

    const uri = prompt("Enter Magnet URI:", magnetUri);
    if (!uri) return;

    setStatus("Downloading...");

    try {
      const existingTorrent = clientRef.current.get(uri);
      if (existingTorrent) {
        setStatus("Torrent already exists");
        return;
      }

      clientRef.current.add(uri, { announce: trackerURLs }, (torrent) => {
        console.log("Downloading torrent:", torrent.infoHash);

        torrent.on("done", () => {
          setStatus("Download complete");
          console.log("Download completed");

          torrent.files.forEach((file) => {
            file.getBlobURL((err, url) => {
              if (err) return console.error(err);
              setDownloads((prev) => [...prev, { name: file.name, url }]);
            });
          });
        });

        torrent.on("error", (err) => {
          console.error("Download error:", err);
          setStatus("Download failed");
        });
      });
    } catch (error) {
      console.error("Download failed:", error);
      setStatus("Download failed");
    }
  };

  return (
    <div
      style={{
        padding: "20px",
        border: "1px solid #eaeaea",
        borderRadius: "8px",
        marginTop: "20px",
      }}
    >
      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px",
        }}
      >
        <button
          onClick={handleSeed}
          style={{
            padding: "10px 20px",
            background: "#0070f3",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
        >
          Seed File
        </button>
        <button
          onClick={handleDownload}
          style={{
            padding: "10px 20px",
            background: "#28a745",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
        >
          Download File
        </button>
      </div>

      <div style={{ marginBottom: "20px", color: "#666" }}>
        Status: {status}
        {magnetUri && (
          <div style={{ marginTop: "10px", fontSize: "0.9em" }}>
            Magnet URI:{" "}
            <code style={{ wordBreak: "break-all" }}>{magnetUri}</code>
          </div>
        )}
      </div>

     {downloads &&  downloads.length > 0 && (
        <div>
          <h3>Downloaded Files:</h3>
          {downloads.map(({ name, url }) => (
            <a
              key={url}
              href={url}
              download={name}
              style={{
                display: "block",
                padding: "10px",
                margin: "5px 0",
                background: "#f8f9fa",
                borderRadius: "4px",
                textDecoration: "none",
                color: "#0070f3",
              }}
            >
              Download {name}
            </a>
          ))}
        </div>
      )}
    </div>
  );
}
