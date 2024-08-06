<script lang="ts">
	import { Router, Route } from "svelte-routing";
	import HomeLayout from "@layouts/HomeLayout.svelte";
</script>

<Router>
	<HomeLayout>
		<Route path="/">Home</Route>
		<!-- Common routes -->
		<Route path="/get-character-urls">Character Urls</Route>
		<Route path="/get-demographics">DemoGraphics</Route>
		<Route path="/get-staff-urls">Staff Urls</Route>
		<!-- Anime routes -->
		<Route path="/get-anime-explicit-genres">Anime Explicit Geners</Route>
		<Route path="/get-anime-genres">Anime Geners</Route>
		<Route path="/get-anime-urls">Anime Urls</Route>
		<Route path="/get-anime-themes">Anime Themes</Route>
	</HomeLayout>
</Router>
