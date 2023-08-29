export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0'),
	() => import('./nodes/1'),
	() => import('./nodes/2'),
	() => import('./nodes/3'),
	() => import('./nodes/4'),
	() => import('./nodes/5'),
	() => import('./nodes/6'),
	() => import('./nodes/7'),
	() => import('./nodes/8'),
	() => import('./nodes/9'),
	() => import('./nodes/10'),
	() => import('./nodes/11'),
	() => import('./nodes/12'),
	() => import('./nodes/13'),
	() => import('./nodes/14'),
	() => import('./nodes/15')
];

export const server_loads = [];

export const dictionary = {
		"/": [3],
		"/anilist/[id=int]": [4],
		"/explore": [5],
		"/kitsu/[id=int]": [6],
		"/list": [7],
		"/openapi/stoplight": [8],
		"/openapi/swagger": [9],
		"/upload": [10],
		"/user/login": [11,[2]],
		"/user/register": [12,[2]],
		"/user/reset-password": [13,[2]],
		"/[...slugs=myanimelist]/episode/[id=int]": [14],
		"/[...slugs=myanimelist]/[id=int]": [15]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),
};

export { default as root } from '../root.svelte';