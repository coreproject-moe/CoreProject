import "./main.css";

import { render } from "solid-js/web";
import { Router } from "@solidjs/router";
import { routes } from "./router";

render(() => <Router>{routes}</Router>, document.getElementById("root") as HTMLElement);
