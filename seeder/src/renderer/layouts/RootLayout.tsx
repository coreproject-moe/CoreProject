import Navbar from "@components/navbar";
import Sidebar from "@components/sidebar";
import { RouteSectionProps } from "@solidjs/router";
import { Component, Show } from "solid-js";
import sidebarStore from "@stores/sidebar";

const HomeLayout: Component<RouteSectionProps> = (props) => {
  return (
    <div class="flex h-screen w-screen flex-col overflow-hidden">
      <Navbar />
      <div class="flex flex-1 gap-3 overflow-hidden p-3">
        <Show when={sidebarStore.open()}>
          <Sidebar />
        </Show>
        <div class="w-full">{props.children}</div>
      </div>
    </div>
  );
};

export default HomeLayout;
