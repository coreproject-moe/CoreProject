import { RouteDefinition } from "@solidjs/router";
import { lazy } from "solid-js";

export const routes: RouteDefinition[] = [
  {
    path: "/",
    component: lazy(() => import("@layouts/RootLayout")),
    children: [
      {
        path: "",
        component: lazy(() => import("@routes/home"))
      },
      {
        path: "/get-character-urls",
        component: lazy(() => import("@routes/character"))
      },
      {
        path: "/get-demographics",
        component: lazy(() => import("@routes/demographics"))
      },
      {
        path: "/get-staff-urls",
        component: lazy(() => import("@routes/staff"))
      },
      {
        path: "/get-anime-explicit-genres",
        component: lazy(() => import("@routes/anime/explicit-genres"))
      },
      {
        path: "/get-anime-genres",
        component: lazy(() => import("@routes/anime/genres"))
      },
      {
        path: "/get-anime-urls",
        component: lazy(() => import("@routes/anime"))
      },
      {
        path: "/get-anime-themes",
        component: lazy(() => import("@routes/anime/themes"))
      }

    ]
  }
]
