"use client";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { IframeMessage } from "@/types/iframe";
import { WS_ENDPOINT } from "@/constants/url";
import { isDataBencoded } from "@/functions/bencode";
import { useHttpData } from "@/hooks/useHttpData";
import { CheckCheck, HeartPulse, LoaderCircle, X } from "lucide-react";
import { useState, useRef, useEffect, RefObject } from "react";

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
              <X className="text-red-500" />
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
  const ws = new WebSocket(WS_ENDPOINT);

  const [loading, setLoading] = useState(true);
  const [wsLoaded, setWsLoaded] = useState(false);
  const [wsError, setWsError] = useState<Error>();

  ws.onopen = () => {
    setWsLoaded(true);
    setLoading(false);
  };

  ws.onerror = () => {
    setLoading(false);
    setWsError(new Error("WebSocket connection error"));
  };

  return (
    <>
      <Card className="md:h-[22vh] lg:h-[17vh]">
        <CardHeader>
          <CardTitle>Websocket Check</CardTitle>
          <CardDescription>
            {loading ? (
              <p>Checking if the tracker is responding with http</p>
            ) : (
              !wsError && <p>There is no error</p>
            )}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex h-full flex-col items-center justify-center gap-2">
            {loading ? (
              <>
                <LoaderCircle className="animate-spin" />
                Checking
              </>
            ) : wsError ? (
              <>
                <X className="text-red-500" />
                <p className="text-red-300"> {wsError.toString()}</p>
              </>
            ) : (
              wsLoaded && (
                <>
                  <CheckCheck className="text-green-400" />
                  <p className="text-primary/90">Tracker is working</p>
                </>
              )
            )}
          </div>
        </CardContent>
      </Card>
    </>
  );
}

function WebsocketTrackerCard() {
  const SHOW_CONSOLE = false;

  const seederIframeRef = useRef<HTMLIFrameElement>(null);
  const clientIframeRef = useRef<HTMLIFrameElement>(null);

  const [websocketClientWorking, setWebsocketClientWorking] = useState(false);

  // Iframe states
  const [seederIframeLoaded, setSeederIframeLoaded] = useState(false);

  const disableConsole = (ref: RefObject<HTMLIFrameElement | null>) => {
    if (ref.current && ref.current.contentWindow) {
      // @ts-expect-error: There is console at runtime
      ref.current.contentWindow.console!.log = function () {};
    }
  };

  // Post a message to `seeder-iframe`
  useEffect(() => {
    if (
      seederIframeLoaded &&
      seederIframeRef.current &&
      seederIframeRef.current.contentWindow
    ) {
      const msgToSeederIframe: IframeMessage = {
        from: "parent",
        message: JSON.stringify({
          type: "seeder",
          data: WS_ENDPOINT,
        }),
      };
      seederIframeRef.current.contentWindow.postMessage(msgToSeederIframe, "*");
    }
  }, [seederIframeLoaded]);

  // Receive message
  useEffect(() => {
    const handleMessage = (event: MessageEvent) => {
      const data = event.data as IframeMessage;
      if (!data.message) return;

      if (data.from === "seeder-iframe") {
        // Check if message here is valid
        if (typeof data.message === "string") {
          const magnetURI = data.message;
          const msgToClientIframe: IframeMessage = {
            from: "parent",
            message: JSON.stringify({
              type: "client",
              data: magnetURI,
              trackerURI: WS_ENDPOINT,
            }),
          };

          clientIframeRef.current?.contentWindow?.postMessage(
            msgToClientIframe,
            "*",
          );
        }
      } else if (data.from === "client-iframe") {
        if (data.message === "Download Complete") {
          setWebsocketClientWorking(true);
        }
      }
    };

    window.addEventListener("message", handleMessage);
    return () => window.removeEventListener("message", handleMessage);
  }, []);

  return (
    <>
      {/* Iframes  */}
      <div className="hidden">
        <iframe
          ref={seederIframeRef}
          onLoad={() => {
            setSeederIframeLoaded(true);
            if (!SHOW_CONSOLE) {
              disableConsole(seederIframeRef);
            }
          }}
          src="/torrent-tester.html"
          name="seeder-iframe"
          width="400"
          height="200"
          title="Seeder Iframe"
        />
        <iframe
          ref={clientIframeRef}
          onLoad={() => {
            if (!SHOW_CONSOLE) {
              disableConsole(clientIframeRef);
            }
          }}
          src="/torrent-tester.html"
          name="client-iframe"
          width="400"
          height="200"
          title="Client Iframe"
        />
      </div>
      {/* Show the cards  */}
      <Card className="md:h-[22vh] lg:h-[17vh]">
        <CardHeader>
          <CardTitle>Http Check</CardTitle>
          <CardDescription>pass1</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex h-full flex-col items-center justify-center gap-2">
            {websocketClientWorking ? (
              <>
                <CheckCheck className="text-green-400" />
                <p className="text-primary/90">Tracker is working</p>
              </>
            ) : (
              <>
                <LoaderCircle className="animate-spin" />
                Checking
              </>
            )}
          </div>
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
        <WebsocketTrackerCard />
      </div>
    </div>
  );
}
