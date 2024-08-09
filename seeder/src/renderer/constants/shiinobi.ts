export const PLATFORMS = ["myanimelist"];

export const COMMANDS = {
	common: ["character-urls", "demographics", "staff-urls"],
	anime: ["anime-explicit-genres", "anime-genres", "anime-themes", "anime-urls"]
};

export const COMMANDS_MAPPING = {
  common: {
    "Characters": "character-urls",
    "Staffs": "staff-urls",
    "Demographics": "demographics"
  },
  anime: {
    "Animes": "anime-urls",
    "Genres": "anime-genres",
    "Explicit Genres": "anime-explicit-genres",
    "Themes": "anime-themes"
  }
}
