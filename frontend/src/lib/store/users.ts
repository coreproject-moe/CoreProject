import { writable } from 'svelte/store';
import { getCookie } from '$lib/functions/getCookie';
import { browser } from '$app/env';

export const isUserAuthenticated = writable(browser && getCookie('Authorization'));
