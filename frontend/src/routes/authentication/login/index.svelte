<script lang="ts">
	import { onMount } from 'svelte';
	import anime from 'animejs';

	import { page } from '$app/stores';
	import { browser } from '$app/env';

	import { trapFocus } from '$lib/functions/trapFocus';
	import { isUserAuthenticated, userToken } from '$lib/store/users';
	import { projectName } from '$lib/constants/frontend/projectName';
	import { tokenObtainUrl } from '$lib/constants/backend/urls/restEndpoints';

	onMount(async () => {
		anime({
			targets: '.animejs__password__icon',
			color: '#FFFFFF',
			scale: 1.5
		});
		anime({
			targets: '.animejs__account__icon',
			color: '#FFFFFF',
			scale: 1.5
		});
	});

	// Bind it to show or hide passwords
	let passwordShown = false;

	// Bindable variables.
	let username = '';
	let password = '';

	// Show error message if theres an error.
	let errorMessage = '';

	const handlePasswordInput = async (e: Event) => {
		const target = e.target as HTMLInputElement;
		password = target?.value;
	};

	const handleFormSubmit = async () => {
		try {
			const res = await fetch(tokenObtainUrl, {
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json'
				},
				method: 'POST',
				body: JSON.stringify({
					username: username,
					password: password
				})
			});
			const data = await res.json();

			if (res?.ok) {
				userToken.set(data);

				const next = $page.url.searchParams.get('next');

				// Goto Next page if it exists.
				if (browser) {
					if (next) window.location.href = next;

					window.location.href = '/home/';
				}
			}

			errorMessage = data.detail;
		} catch {
			errorMessage = 'Cannot POST to Backend | Is backend down ? 🤔';
		}
	};
</script>

<svelte:head>
	<title>Login Page | {projectName}</title>
</svelte:head>

{#if errorMessage}
	<div class="columns is-mobile is-centered">
		<div class="column is-narrow">
			<p class="error">{errorMessage}</p>
		</div>
	</div>
{/if}

{#if $isUserAuthenticated}
	<div class="columns is-mobile is-centered">
		<div class="column is-narrow"><p class="has-text-white">You are already logged in 😕</p></div>
	</div>
{:else}
	<form on:submit|preventDefault={handleFormSubmit} method="POST" use:trapFocus>
		<div class="items field is-horizontal">
			<div class="field-body">
				<div class="field">
					<p class="control is-expanded has-icons-left">
						<input
							type="text"
							name="username"
							class="input"
							placeholder="Username"
							maxlength={50}
							required={true}
							bind:value={username}
						/>
						<span class="icon is-small is-left">
							<ion-icon class="animejs__account__icon" name="person-circle-outline" />
						</span>
					</p>
				</div>
			</div>
		</div>
		<div class="items field is-horizontal">
			<div class="field-body">
				<div class="field">
					<p class="control is-expanded has-icons-left has-icons-right">
						<input
							type={passwordShown ? 'text' : 'password'}
							name="password"
							class="input"
							placeholder="Password"
							maxlength={1024}
							minlength={8}
							required={true}
							on:input={handlePasswordInput}
						/>
						<span
							class="icon is-small is-right is-clickable is-unselectable"
							on:click={async () => {
								passwordShown = !passwordShown;
							}}
						>
							👀
						</span>
						<span class="icon is-small is-left">
							<ion-icon class="animejs__password__icon" name="lock-closed-outline" />
						</span>
					</p>
				</div>
			</div>
		</div>
		<div class="items columns is-mobile is-centered">
			<div class="column is-narrow">
				<button id="button" class="button is-rounded is-centered is-ghost"> Sign in </button>
			</div>
		</div>
	</form>
	<div class="level">
		<div class="level-left">
			<div class="level-item is-size-7">
				<span class="has-text-link">
					<a class="has-text-white" href="/authentication/forget_password/"> Forgot password? </a>
				</span>
			</div>
		</div>
		<div class="level-right">
			<div class="level-item is-size-7">
				<p class="new_here_tag">
					New here?
					<span class="has-text-link">
						<a class="has-text-white" href="/authentication/register/"> Register an account </a>
					</span>
				</p>
			</div>
		</div>
	</div>
{/if}
