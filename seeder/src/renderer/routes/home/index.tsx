import { get_humanize_time } from "@renderer/utils/time";
import { Component } from "solid-js";

const Home: Component = () => {
	return (
		<div class="flex size-full flex-col gap-10 px-10">
			<div>
				<h1 class="text-3xl font-bold text-warning">Hello, Sora</h1>
				<span class="text-sm">{get_humanize_time()}!</span>
			</div>
		</div>
	);
};

export default Home;
