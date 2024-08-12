import "./main.css";

import { render } from "solid-js/web";
import { RouteDefinition, HashRouter } from "@solidjs/router";
import { lazy, onMount } from "solid-js";
import { defineCustomElements } from "@coreproject-moe/icons/loader";

const routes: RouteDefinition[] = [
	{
		path: "/",
		component: lazy(() => import("@layouts/RootLayout")),
		children: [
			{
				path: "",
				component: lazy(() => import("@routes/home"))
			},
			{
				path: "/character-urls",
				component: lazy(() => import("@routes/character"))
			},
			{
				path: "/demographics",
				component: lazy(() => import("@routes/demographics"))
			},
			{
				path: "/staff-urls",
				component: lazy(() => import("@routes/staff"))
			},
			{
				path: "/anime-explicit-genres",
				component: lazy(() => import("@routes/anime/explicit-genres"))
			},
			{
				path: "/anime-genres",
				component: lazy(() => import("@routes/anime/genres"))
			},
			{
				path: "/anime-urls",
				component: lazy(() => import("@routes/anime"))
			},
			{
				path: "/anime-themes",
				component: lazy(() => import("@routes/anime/themes"))
			}
		]
	}
];

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
