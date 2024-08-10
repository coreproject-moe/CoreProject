export const PLATFORMS = ["myanimelist"];

export const COMMANDS_MAPPING = {
	shared: {
		Characters: {
			command: "character-urls",
			icon: `<coreproject-shape-user class="md:size-3"></coreproject-shape-user>`
		},
		Staffs: {
			command: "staff-urls",
			icon: `<coreproject-shape-headphone class="md:size-3"></coreproject-shape-headphone>`
		}
	},
	anime: {
		Animes: {
			command: "anime-urls",
			icon: `<coreproject-shape-play class="md:size-3"></coreproject-shape-play>`
		},
		Genres: {
			command: "anime-genres",
			icon: `<coreproject-shape-explore class="md:size-3"></coreproject-shape-misc>`
		},
		Themes: {
			command: "anime-themes",
			icon: `<coreproject-shape-preference class="md:size-3"></coreproject-shape-preference>`
		}
	}
};
