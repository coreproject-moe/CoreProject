import { writable } from 'svelte/store';
import { userInfoUrl } from '$lib/constants/restEndpoints';
import { getCookie } from '$lib/functions/getCookie';
import { browser } from '$app/env';

export const isUserAuthenticated = writable(browser && getCookie('Authorization'));

const getData = () => {
	fetch(userInfoUrl, {
		method: 'GET',
		headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json',
			Authorization: `Token ${browser && getCookie('Authorization')}`
		}
	}).then(async (res) => {
		const data = await res.json();
		userInfo.set(data);
	});
};

getData();

export const userInfo = writable({}, (set) => {
	
});

// Finally works i guess, God i hate JS.
