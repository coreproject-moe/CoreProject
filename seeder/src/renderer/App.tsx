import { Route, Router } from "@solidjs/router";
import { type Component } from "solid-js";
import RootLayout from "@layouts/RootLayout";
// Routes
import Home from "@routes/home";
import Character from "@routes/character";
import DemoGraphics from "@routes/demographics";
import Staff from "@routes/staff";
import AnimeExplicitGenres from "@routes/anime/explicit-genres";
import AnimeGenres from "@routes/anime/genres";
import Anime from "@routes/anime";
import AnimeThemes from "@routes/anime/themes";

const App: Component = () => {
  return (
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
};

export default App;
