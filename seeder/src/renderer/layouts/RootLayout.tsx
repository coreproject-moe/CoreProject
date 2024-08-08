import Navbar from "@components/navbar";
import Sidebar from "@components/sidebar";
import { RouteSectionProps } from "@solidjs/router";
import { Component } from "solid-js";

const HomeLayout: Component<RouteSectionProps> = ({ children }) => {
	return (
		<div class="flex h-screen w-screen flex-col">
			<Navbar />
			<div class="flex flex-1 md:gap-3 md:p-3">
				<Sidebar />
				<div class="w-full">{children}</div>
			</div>
		</div>
	);
};

export default HomeLayout;
