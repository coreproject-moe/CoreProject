const time_map = [
	[0, 12, "Good morning"],
	[12, 18, "Good afternoon"],
	[18, 24, "Good night"]
];

export function get_humanize_time() {
	const current_hr = new Date().getHours();

	for (let i = 0; i < time_map.length; i++) {
		if (current_hr >= Number(time_map[i][0]) && current_hr <= Number(time_map[i][1])) {
			return time_map[i][2];
		}
	}

	// if nothing matches
	return "Good day";
}
