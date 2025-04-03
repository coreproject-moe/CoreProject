"use client";

import { Button } from "@/components/ui/button";
import { usePathname } from "next/navigation";
import CoreProjectIcon from "@/icons/CoreProject.svg";
import CoreIcon from "@/icons/CoreIcon.svg";

import Link from "next/link";

const buttonMapping = {
  Dashboard: "/",
};

export function Navbar() {
  const pathname = usePathname();
  return (
    <div className="mx-2 my-5 grid h-12 grid-cols-3 md:mx-10">
      {/* Left section */}
      <div>
        <div className="flex flex-col items-start justify-center">
          <div className="hidden h-3 w-40 md:block">
            <CoreProjectIcon />
          </div>
        </div>
        <div className="flex">
          <div className="block h-3 w-8 md:hidden">
            <CoreIcon />
          </div>
        </div>
      </div>

      {/* Middle section  */}
      <div className="flex items-center justify-center gap-3">
        {Object.entries(buttonMapping).map(([name, link], key) => {
          const isActive = pathname === link;

          if (isActive) {
            return (
              <Button key={key} variant="default">
                {name}
              </Button>
            );
          } else {
            return (
              <Button key={key} variant="outline" asChild>
                <Link href={link}>{name}</Link>
              </Button>
            );
          }
        })}
      </div>
    </div>
  );
}
