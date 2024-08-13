import Navbar from "@components/navbar";
import Sidebar from "@components/sidebar";
import { RouteSectionProps } from "@solidjs/router";
import { Component } from "solid-js";

const HomeLayout: Component<RouteSectionProps> = (props) => {
  return (
    <div class="flex h-screen w-screen flex-col overflow-hidden">
      <Navbar />
      <div class="flex flex-1 md:gap-3 md:p-3 overflow-hidden">
        <Sidebar />
        <div class="w-full">{props.children}</div>
      </div>
    </div>
  );
};

export default HomeLayout;
