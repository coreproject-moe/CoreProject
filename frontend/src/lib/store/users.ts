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

setInterval(async () => {
	if (browser && localStorage.getItem('tokens')) {
		const tokenObj: { access: string; refresh: string } = JSON.parse(
			localStorage.getItem('tokens')
		);
		const res = await fetch(tokenRefreshUrl, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				refresh: tokenObj.refresh
			})
		});
		const data = await res.json();
		userToken.set({ refresh: tokenObj.refresh, access: data?.access });
	}
}, 5000);
