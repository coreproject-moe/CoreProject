import { get_free_port } from "$utils/port";

export type ExpressUrls = {
	shiinobi_healthcheck: string;
	staff: string;
};

export const express_port = await get_free_port();

const base_url = `http://localhost:${express_port}`;

export const EXPRESS_URLS: ExpressUrls = {
	shiinobi_healthcheck: `${base_url}/shiinobi-healthcheck`,
	staff: `${base_url}/staff`
};
