"use client";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { isDataBencoded } from "@/functions/bencode";
import { useHttpData } from "@/hooks/useHttpData";
import { CheckCheck, CirclePlus, HeartPulse, LoaderCircle } from "lucide-react";

function HttpCard() {
  const {
    data: httpData,
    isLoading: httpIsLoading,
    isError: httpIsError,
  } = useHttpData();

  /*
  useEffect(() => {
    console.log("Loading:", httpIsLoading);
    console.log("Data:", httpData);
    console.log("Error:", httpIsError);

    if (!httpIsLoading && httpData) {
      console.log("Data loaded:", httpData);
      console.log("isDataBencoded:", isDataBencoded(httpData));
    }
  }, [httpIsLoading, httpData, httpIsError]);
  */

  return (
    <Card className="md:h-[22vh] lg:h-[17vh]">
      <CardHeader>
        <CardTitle>Http Check</CardTitle>
        <CardDescription>
          {httpIsLoading ? (
            <p>Checking if the tracker is responding with http</p>
          ) : (
            !httpIsError && <p>There is no error</p>
          )}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex h-full flex-col items-center justify-center gap-2">
          {httpIsLoading ? (
            <>
              <LoaderCircle className="animate-spin" />
              Checking
            </>
          ) : httpIsError ? (
            <>
              <CirclePlus className="rotate-45 text-red-500" />
              <p className="text-red-300"> {httpIsError.toString()}</p>
            </>
          ) : (
            httpData &&
            isDataBencoded(httpData) && (
              <>
                <CheckCheck className="text-green-400" />
                <p className="text-primary/90">Tracker is working</p>
              </>
            )
          )}
        </div>
      </CardContent>
    </Card>
  );
}

function WebsocketCard() {
  return (
    <>
      <Card className="md:h-[22vh] lg:h-[17vh]">
        <CardHeader>
          <CardTitle>Websocket Check</CardTitle>
          <CardDescription></CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex h-full flex-col items-center justify-center gap-2"></div>
        </CardContent>
      </Card>
    </>
  );
}

export default function Page() {
  return (
    <div className="mx-10">
      <div className="mb-5 flex flex-col gap-5">
        <div className="flex items-center gap-3">
          <HeartPulse className="text-red-400" />
          <h1 className="text-3xl">Tracker Health Check:</h1>
        </div>
      </div>

      <div className="grid grid-cols-1 items-center justify-center gap-10 md:grid-cols-3">
        <HttpCard />
        <WebsocketCard />
      </div>
    </div>
  );
}
