import type { Component } from "solid-js";
import CoreLogo from "@assets/icons/core/logo.svg?component-solid";
import CoreSeederLogo from "@assets/icons/core/coreseeder.svg?component-solid";

const Navbar: Component = () => {
	return (
		<div class="relative flex h-14 w-full items-center justify-between p-3">
			<div class="flex h-full items-center gap-3">
				<CoreLogo class="h-full w-auto" />
				<CoreSeederLogo class="h-4 w-auto" />
			</div>
			<div class="h-full">
				<button class="btn btn-neutral h-full min-h-full rounded outline-none">Logout</button>
			</div>
		</div>
	);
};

export default Navbar;
