import { writable } from 'svelte/store';
import { getCookie } from '$lib/functions/getCookie';
import { browser } from '$app/env';

// So we are getting the Authorization cookie.
// I have set up this in the  backend so that,
// When a user logs in, it will create the token.
// On logout delete the cookie.
// We can listen to the cookie changes to determine if a user is logged in or not.

export const isUserAuthenticated = writable(browser && getCookie('Authorization'));
