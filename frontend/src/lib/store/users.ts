import { browser } from '$app/env';
import { writable } from 'svelte/store';
import { tokenRefreshUrl } from '$lib/constants/backend/restEndpoints';

export const isUserAuthenticated = writable(
	JSON.parse(browser && localStorage.getItem('tokens')).access !== undefined
);

export const userToken = writable(
	(browser && JSON.parse(localStorage?.getItem('tokens'))) || { refresh: '', access: '' }
);

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
