<script context="module" lang="ts">
	import { browser } from "$app/env";
	
	import { get } from "svelte/store";

	import { tokenBlacklistUrl } from "$lib/constants/backend/urls/restEndpoints";
	import { isUserAuthenticated, userToken } from "$store/users";

	export async function load({ fetch }) {
		if (browser && get(isUserAuthenticated)) {
			const res = await fetch(tokenBlacklistUrl, {
				method: "POST",
				headers: {
					Accept: "application/json",
					"Content-Type": "application/json"
				},
				body: JSON.stringify({
					refresh: get(userToken).refresh
				})
			});
			if (res?.ok) {
				return {
					props: {
						logoutState: true
					}
				};
			}
		}
		return {
			props: {
				logoutState: false
			}
		};
	}
</script>

<script lang="ts">
	export let logoutState: boolean;
</script>

{#if logoutState}
	<div />
{:else}
	<div />
{/if}
