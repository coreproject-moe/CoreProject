import { browser } from '$app/env';
import { writable } from 'svelte/store';
import { tokenRefreshUrl } from '$lib/constants/backend/restEndpoints';

const getUserState = () => {
	// Try catch block to get value
	try {
		const data = browser && localStorage.getItem('tokens');
		return JSON.parse(data).access !== undefined;
	} catch {
		return false;
	}
};

export const isUserAuthenticated = writable(getUserState());

export const userToken = writable(
	(browser && JSON.parse(localStorage.getItem('tokens'))) || { refresh: '', access: '' }
);

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
