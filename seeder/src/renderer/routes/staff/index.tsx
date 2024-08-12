import { Component } from "solid-js";

const Staff: Component = () => {
	async function handle_fetch_click() {
		const res = await window.api.get_staff_urls();
		console.log(res);
	}

	return (
		<button class="btn btn-primary" onclick={handle_fetch_click}>
			Fetch
		</button>
	);
};

export default Staff;
