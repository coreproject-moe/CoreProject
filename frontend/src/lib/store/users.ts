import { browser } from '$app/env';
import { get, writable } from 'svelte/store';
import { tokenRefreshUrl } from '$lib/constants/backend/restEndpoints';

export const userToken = writable(
	(browser && JSON.parse(localStorage.getItem('tokens'))) || { refresh: '', access: '' }
);

export const isUserAuthenticated = writable(get(userToken).access);

// Monitor changes and set it to localStorage
userToken.subscribe((change: { access: string; refresh: string }) => {
	browser && localStorage.setItem('tokens', JSON.stringify(change));
});

// Custom function to refresh tokens

browser && // Is browser
	get(isUserAuthenticated) && // User is authenticated
	localStorage.getItem('tokens') && // Item exists
	setInterval(async () => {
		const res = await fetch(tokenRefreshUrl, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				refresh: get(userToken).refresh
			})
		});
		const data = await res.json();
		userToken.set({ refresh: get(userToken).refresh, access: data?.access });
	}, 5000);
