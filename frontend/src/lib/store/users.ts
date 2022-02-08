import { writable } from 'svelte/store';
import { userInfoUrl } from '$lib/constants/restEndpoints';
import { getCookie } from '$lib/functions/getCookie';
import { browser } from '$app/env';
import axios from 'axios';

export const isUserAuthenticated = writable(browser && getCookie('Authorization'));

const getInfo = async () => {
	const endPoint = userInfoUrl;

	await axios
		.get(endPoint, {
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
				Authorization: `Token ${getCookie('Authorization')}`
			}
		})
		.then(async (res) => {
			await userInfo.set(await res.data);
		})
		.catch((e) => {
			console.error(`Cannot POST to server | Reason : ${e}`);
		});
};

export const userInfo = writable();

// Finally works i guess, God i hate JS.
browser && getInfo();
