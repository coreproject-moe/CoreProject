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
  HardDriveDownload,
  HardDriveUpload,
  Layers2,
  LoaderCircle,
  Router,
  TrendingUp,
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
  const totalValueLengths = Object.values(data.redis_data).map(
    (value) => Object.keys(value as Record<string, unknown>).length,
  );
  const totalLength = totalValueLengths.reduce(
    (acc, length) => acc + length,
    0,
  );

  // Counting seeders and leechers
  let seeders = 0;
  let leechers = 0;

  // Iterate through redis_data
  for (const key in data.redis_data) {
    const value = data.redis_data[key];
    for (const peer in value) {
      const peerData = value[peer];
      try {
        // Parse the peer data string into an object
        const peerInfo = JSON.parse(peerData);
        if (peerInfo.left === 0) {
          seeders++;
        } else {
          leechers++;
        }
      } catch (e) {
        // If the data is invalid or can't be parsed, skip it
        continue;
      }
    }
  }

  const mapping = [
    {
      title: "Total Torrents",
      description: "The amount of torrents in the database.",
      value: totalTorrent,
      icon: TrendingUp,
      valueDescription: "Count:",
    },
    {
      title: "Total Clients",
      description: "The amount of clients that are either seeding or leeching.",
      value: totalLength,
      icon: Router,
      valueDescription: "Count:",
    },
  ];

  return (
    <div className="grid grid-cols-1 items-center justify-center gap-10 md:grid-cols-3">
      {mapping.map((value, index) => {
        return (
          <Card
            key={`torrent-card-component-${index}`}
            className="md:h-[22vh] lg:h-[17vh]"
          >
            <CardHeader>
              <CardTitle>{value.title}</CardTitle>
              <CardDescription>
                <p>{value.description}</p>
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="relative flex items-center justify-center">
                <value.icon />
              </div>
            </CardContent>
            <CardFooter className="justify-center gap-2">
              <p>{value.valueDescription}</p>
              <code>{value.value}</code>
            </CardFooter>
          </Card>
        );
      })}
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
                Total Seeders: {seeders}
              </p>
            </div>
            <div className="flex flex-col items-center justify-center gap-3">
              <HardDriveDownload className="text-red-400" />

              <p className="text-primary/90 text-sm">
                Total Leechers: {leechers}
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
            <div className="flex items-center justify-center">
              Error occured while fetching data from backend
            </div>
          ) : (
            <>
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
