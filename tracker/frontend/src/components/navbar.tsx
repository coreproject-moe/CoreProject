"use client";

import { Button } from "@/components/ui/button";
import { usePathname } from "next/navigation";
import CoreIcon from "@/icons/CoreProject.svg";

const buttonMapping = {
  Dashboard: "/",
  Test: "/test",
};

export function Navbar() {
  const pathname = usePathname();
  return (
    <div className="mx-10 my-5 grid grid-cols-3">
      {/* Left section */}
      <div className="flex flex-col items-start justify-center">
        <CoreIcon />
      </div>

      {/* Middle section  */}
      <div className="flex items-center justify-center gap-3">
        {Object.entries(buttonMapping).map(([name, link], key) => {
          const isActive = pathname === link;

          return (
            <Button key={key} variant={isActive ? "default" : "outline"}>
              {name}
            </Button>
          );
        })}
      </div>
      {/* Right section */}
      <div className="flex flex-col items-end justify-center">hello</div>
    </div>
  );
}
