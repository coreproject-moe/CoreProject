"use client";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  AudioLines,
  EarthLock,
  File,
  GlobeLock,
  HardDriveDownload,
  HardDriveUpload,
  Layers2,
  LoaderCircle,
  Router,
  WaypointsIcon,
  X,
} from "lucide-react";
import RedisIcon from "@/icons/redis.svg";

import Image from "next/image";
import { useBackendData } from "@/hooks/useBackendData";
import React from "react";

/* eslint-disable  @typescript-eslint/no-explicit-any */
function VersionCardComponent({ data }: { data: any }) {
  const mapping = [
    {
      title: "Quart",
      description:
        "An async Python micro framework for building web applications.",
      icon: "/quart.png",
      version: data.quart_version,
    },
    {
      title: "Python",
      description:
        "Python is a programming language that lets you work quickly and integrate systems more effectively.",
      icon: "/python.svg",
      version: data.python_version,
    },
    {
      title: "Redis",
      description: "Redis is an in-memory database that persists on disk.",
      icon: RedisIcon,
      version: {
        client: data.redis_version.client,
        server: data.redis_version.server,
      },
    },
  ];

  return (
    <div className="grid grid-cols-1 items-center justify-center gap-10 md:grid-cols-3">
      {mapping.map((value, index) => {
        return (
          <Card
            key={`version-card-component-${index}`}
            className="md:h-[22vh] lg:h-[19vh]"
          >
            <CardHeader>
              <CardTitle>{value.title}</CardTitle>
              <CardDescription>
                <p>{value.description}</p>
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="relative inset-0 flex h-[50px] items-center justify-center">
                {typeof value.icon === "string" && (
                  <Image
                    src={value.icon}
                    width="120"
                    height="250"
                    alt="quart"
                    className="absolute z-20 h-[40px] object-fill"
                  />
                )}

                {typeof value.icon === "function" && (
                  <value.icon
                    width="120"
                    height="250"
                    className="absolute z-20 h-[40px]"
                  />
                )}

                <div className="bg-primary absolute z-10 h-[45px] w-[125px] rounded-lg"></div>
              </div>
            </CardContent>
            <CardFooter className="justify-center gap-2">
              {typeof value.version === "string" && (
                <>
                  <p>Version:</p>
                  <code>{value.version}</code>
                </>
              )}
              {typeof value.version === "object" && (
                <>
                  <div className="space-x-2">
                    <span>Server:</span>
                    <code>{value.version.server}</code>
                  </div>
                  <div className="text-primary/30">|</div>
                  <div className="space-x-2">
                    <span>Client:</span>
                    <code>{value.version.client}</code>
                  </div>
                </>
              )}
            </CardFooter>
          </Card>
        );
      })}
    </div>
  );
}

/* eslint-disable  @typescript-eslint/no-explicit-any */
function TorrentCardComponent({ data }: { data: any }) {
  const totalTorrent = Object.keys(data.redis_data).length;
  const totalClientValueLengths = Object.values(data.redis_data).map(
    (value) => Object.keys(value as Record<string, unknown>).length,
  );
  const totalClientLength = totalClientValueLengths.reduce(
    (acc, length) => acc + length,
    0,
  );

  // Counting seeders and leechers
  let seeders = 0;
  let leechers = 0;
  let udpClients = 0;
  let websocketClients = 0;
  let httpClients = 0;

  // Iterate through redis_data
  for (const key in data.redis_data) {
    const value = data.redis_data[key];
    for (const peer in value) {
      const peerData = value[peer];
      try {
        const peerInfo = JSON.parse(peerData);

        // Seeder and Leechers
        if (peerInfo.left === 0) {
          seeders++;
        } else {
          leechers++;
        }

        // Client type
        if (peerInfo.type === "http") {
          httpClients++;
        } else if (peerInfo.type === "udp") {
          udpClients++;
        } else if (peerInfo.type === "websocket") {
          websocketClients++;
        } else {
          console.error(`Unknown client type: ${peerInfo.type}`);
        }
      } catch {
        // If the data is invalid or can't be parsed, skip it
        continue;
      }
    }
  }

  return (
    <div className="grid grid-cols-1 items-center justify-center gap-10 md:grid-cols-3">
      <Card className="md:h-[22vh] lg:h-[17vh]">
        <CardHeader>
          <CardTitle>Total Torrents and Clients</CardTitle>
          <CardDescription>
            <p>The amount of torrents and clients</p>
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid h-full grid-cols-2">
            <div className="flex flex-col items-center justify-center gap-3">
              <File className="text-green-400" />

              <p className="text-primary/90 text-sm">
                Total Torrents: <code>{totalTorrent}</code>
              </p>
            </div>
            <div className="flex flex-col items-center justify-center gap-3">
              <Router className="text-green-600" />

              <p className="text-primary/90 text-sm">
                Total Clients: <code>{totalClientLength}</code>
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card className="md:h-[22vh] lg:h-[17vh]">
        <CardHeader>
          <CardTitle>Client Distribution</CardTitle>
          <CardDescription>
            <p>The amount of client in udp or http/websocket</p>
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid h-full grid-cols-3">
            <div className="flex flex-col items-center justify-center gap-3">
              <GlobeLock className="text-green-400" />

              <p className="text-primary/90 text-sm">
                Total UDP Clients: <code>{udpClients}</code>
              </p>
            </div>
            <div className="flex flex-col items-center justify-center gap-3">
              <EarthLock className="text-green-400" />

              <p className="text-primary/90 text-sm">
                Total HTTP Clients: <code>{httpClients}</code>
              </p>
            </div>

            <div className="flex flex-col items-center justify-center gap-3">
              <WaypointsIcon className="text-green-400" />

              <p className="text-primary/90 text-sm">
                Total Websocket Clients: <code>{websocketClients}</code>
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card className="md:h-[22vh] lg:h-[17vh]">
        <CardHeader>
          <CardTitle>Total Seeders/Leechers</CardTitle>
          <CardDescription>
            <p>The amount of seeders or leechers</p>
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid h-full grid-cols-2">
            <div className="flex flex-col items-center justify-center gap-3">
              <HardDriveUpload className="text-green-400" />

              <p className="text-primary/90 text-sm">
                Total Seeders: <code>{seeders}</code>
              </p>
            </div>
            <div className="flex flex-col items-center justify-center gap-3">
              <HardDriveDownload className="text-red-400" />

              <p className="text-primary/90 text-sm">
                Total Leechers: <code>{leechers}</code>
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

export default function Page() {
  const {
    data: backendData,
    isLoading: backendIsLoading,
    isError: backendIsError,
  } = useBackendData();

  return (
    <div className="mx-10">
      {backendIsLoading ? (
        <div className="flex w-full items-center justify-center gap-3">
          <p>Loading</p>
          <LoaderCircle className="animate-spin" />
        </div>
      ) : (
        <>
          {backendIsError ? (
            <div className="flex h-96 flex-col items-center justify-center">
              <X className="text-red-500" />
              <p className="text-red-300"> {backendIsError.toString()}</p>
            </div>
          ) : (
            <>
              {/* Stack version */}
              <div className="mb-5 flex flex-col gap-5">
                <div className="flex items-center gap-3">
                  <Layers2 />
                  <h1 className="text-3xl">Stack version:</h1>
                </div>
              </div>

              {/* Grid to show version  */}
              <VersionCardComponent data={backendData} />

              {/* Tracker information */}
              <div className="my-10 flex flex-col gap-5">
                <div className="flex items-center gap-3">
                  <AudioLines />
                  <h1 className="text-3xl">Tracker information:</h1>
                </div>
              </div>

              {/* Grid to show tracker information  */}
              <TorrentCardComponent data={backendData} />
            </>
          )}
        </>
      )}
    </div>
  );
}
