import { get_humanize_time } from "@renderer/utils/time";
import { Component } from "solid-js";

const Home: Component = () => {
	return (
		<div class="flex size-full flex-col md:gap-10 md:px-10">
			<div>
				<h1 class="font-bold text-accent md:text-3xl">Hello, Sora</h1>
				<span class="md:text-sm">{get_humanize_time()}!</span>
			</div>
		</div>
	);
};

export default Home;
