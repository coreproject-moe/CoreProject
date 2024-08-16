import "./main.css";

import { routes } from "./routes";
import { render } from "solid-js/web";
import { HashRouter } from "@solidjs/router";
import { onMount } from "solid-js";
import { defineCustomElements } from "@coreproject-moe/icons/loader";

render(() => {
	onMount(() => {
		defineCustomElements(window);
	});

	return (
		<HashRouter preload={true} explicitLinks={true}>
			{routes}
		</HashRouter>
	);
}, document.getElementById("root")!);
