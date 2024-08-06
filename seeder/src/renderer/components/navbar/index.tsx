import type { Component } from "solid-js";
import CoreLogoPath from "@assets/icons/core/logo.svg";
import CoreSeederLogoPath from "@assets/icons/core/coreseeder.svg";

const Navbar: Component = () => {
  return (
    <div class="relative flex w-full items-center justify-between md:h-14 md:p-3">
      <div class="flex h-full items-center md:gap-3">
        <img src={CoreLogoPath} class="h-full w-auto" alt="" />
        <img src={CoreSeederLogoPath} class="w-auto md:h-4" alt="" />
      </div>
    </div>
  );
};

export default Navbar;
