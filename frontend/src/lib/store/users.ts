import { writable } from 'svelte/store';
import { browser } from '$app/env';
import { tokenRefreshUrl } from '$lib/constants/backend/restEndpoints';

// So we are getting the Authorization cookie.
// I have set up this in the  backend so that,
// When a user logs in, it will create the token.
// On logout delete the cookie.
// We can listen to the cookie changes to determine if a user is logged in or not.

export const isUserAuthenticated = writable(
	browser && JSON.parse(localStorage.getItem('tokens')).access === ''
);

export const userToken = writable(browser && JSON.parse(localStorage?.getItem('tokens')));

userToken.subscribe((change: { access: string; refresh: string }) => {
	browser && localStorage?.setItem('tokens', JSON.stringify(change));
});

setInterval(async () => {
	if (browser && localStorage.getItem('tokens')) {
		const tokenObj: { access: string; refresh: string } = JSON.parse(
			localStorage?.getItem('tokens')
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
