import type { Component } from "solid-js";
import CoreLogo from "@assets/icons/core/logo.svg?component-solid";
import CoreSeederLogo from "@assets/icons/core/coreseeder.svg?component-solid";
import sidebarStore from "@stores/sidebar";

const Navbar: Component = () => {
  return (
    <div class="relative flex h-14 w-full items-center justify-between p-3">
      <div class="flex h-full items-center gap-3">
        <button onClick={() => sidebarStore.setOpen((prev) => !prev)} class="outline-none btn aspect-square btn-neutral h-full min-h-full rounded">
          {/* @ts-ignore: solid support issue */}
          <coreproject-shape-list class="size-5"></coreproject-shape-list>
        </button>
        <CoreLogo class="h-full w-auto" />
      </div>
      <CoreSeederLogo class="h-4 w-auto absolute left-1/2 transform -translate-x-1/2" />
      <div class="h-full">
        <button class="btn btn-neutral h-full min-h-full rounded outline-none">Logout</button>
      </div>
    </div>
  );
};

export default Navbar;
