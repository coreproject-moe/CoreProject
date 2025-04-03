"use client";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Layers2, LoaderCircle } from "lucide-react";
import RedisIcon from "@/icons/redis.svg";

import Image from "next/image";
import { useBackendData } from "@/hooks/useBackendData";

export default function Home() {
  const {
    data: backendData,
    isLoading: backendIsLoading,
    isError: backendIsError,
  } = useBackendData();

  return (
    <div className="mx-10 flex flex-col gap-5">
      <div className="flex items-center gap-3">
        <Layers2 />
        <h1 className="text-3xl">Stack version:</h1>
      </div>

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
            <div className="grid grid-cols-1 items-center justify-center gap-10 md:grid-cols-3">
              <Card className="md:h-[22vh] lg:h-[17vh]">
                <CardHeader>
                  <CardTitle>Quart</CardTitle>
                  <CardDescription>
                    <p>
                      An async Python micro framework for building web
                      applications.
                    </p>
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="relative inset-0 flex h-[50px] items-center justify-center">
                    <Image
                      src="/quart.png"
                      width="120"
                      height="250"
                      alt="quart"
                      className="absolute z-20 h-[40px] object-fill"
                    />
                    <div className="bg-primary absolute z-10 h-[45px] w-[125px] rounded-lg"></div>
                  </div>
                </CardContent>
                <CardFooter className="justify-center gap-2">
                  <p>Version:</p>
                  <code>{backendData.quart_version}</code>
                </CardFooter>
              </Card>

              <Card className="md:h-[22vh] lg:h-[17vh]">
                <CardHeader>
                  <CardTitle>Python</CardTitle>
                  <CardDescription>
                    <p>
                      Python is a programming language that lets you work
                      quickly and integrate systems more effectively.
                    </p>
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="relative inset-0 flex h-[50px] items-center justify-center">
                    <Image
                      src="/python.svg"
                      width="120"
                      height="250"
                      alt="quart"
                      className="absolute z-20 h-[40px] object-fill"
                    />
                    <div className="bg-primary absolute z-10 h-[45px] w-[125px] rounded-lg"></div>
                  </div>
                </CardContent>
                <CardFooter className="justify-center gap-2">
                  <p>Version:</p>
                  <code>{backendData.python_version}</code>
                </CardFooter>
              </Card>

              <Card className="md:h-[22vh] lg:h-[17vh]">
                <CardHeader>
                  <CardTitle>Redis</CardTitle>
                  <CardDescription>
                    <p>Redis is an in-memory database that persists on disk.</p>
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="relative inset-0 flex h-[50px] items-center justify-center">
                    <RedisIcon
                      width="120"
                      height="250"
                      className="absolute z-20 h-[40px]"
                    />
                    <div className="bg-primary absolute z-10 h-[45px] w-[125px] rounded-lg"></div>
                  </div>
                </CardContent>
                <CardFooter className="justify-center gap-2">
                  <div className="space-x-2">
                    <span>Server:</span>
                    <code>{backendData.redis_version.server}</code>
                  </div>
                  <div className="text-primary/30">|</div>
                  <div className="space-x-2">
                    <span>Client:</span>
                    <code>{backendData.redis_version.client}</code>
                  </div>
                </CardFooter>
              </Card>
            </div>
          )}
        </>
      )}
    </div>
  );
}
