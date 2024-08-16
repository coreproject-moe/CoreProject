import { get_free_port } from "../utils/port";

export const express_port = await get_free_port();

const base_url = `http://localhost:${express_port}`;

export const EXPRESS_URLS = {
	shiinobi_healthcheck: `${base_url}/shiinobi-healthcheck`,
	staff: `${base_url}/staff`
};
