import { Route, Router } from "@solidjs/router";
import { lazy, type Component } from "solid-js";
import RootLayout from "@layouts/RootLayout";
// Routes
const Home = lazy(() => import("@routes/home"));
const Character = lazy(() => import("@routes/character"));
const DemoGraphics = lazy(() => import("@routes/demographics"));
const Staff = lazy(() => import("@routes/staff"));
const AnimeExplicitGenres = lazy(() => import("@routes/anime/explicit-genres"));
const AnimeGenres = lazy(() => import("@routes/anime/genres"));
const Anime = lazy(() => import("@routes/anime"));
const AnimeThemes = lazy(() => import("@routes/anime/themes"));

const App: Component = () => (
	<Router>
		<Route path="/" component={RootLayout}>
			<Route path="/" component={Home} />

			<Route path="/get-character-urls" component={Character} />
			<Route path="/get-demographics" component={DemoGraphics} />
			<Route path="/get-staff-urls" component={Staff} />

			<Route path="/get-anime-explicit-genres" component={AnimeExplicitGenres} />
			<Route path="/get-anime-genres" component={AnimeGenres} />
			<Route path="/get-anime-urls" component={Anime} />
			<Route path="/get-anime-themes" component={AnimeThemes} />
		</Route>
	</Router>
);

export default App;
