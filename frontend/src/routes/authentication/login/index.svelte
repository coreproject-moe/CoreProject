<script lang="ts">
	import { onMount } from 'svelte';
	import anime from 'animejs';

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
		// bind this to jwt
		console.log(username, password);
	};
</script>

{#if errorMessage}
	<div class="columns is-mobile is-centered">
		<div class="column is-narrow">
			<p class="error">{errorMessage}</p>
		</div>
	</div>
{/if}

<form on:submit|preventDefault={handleFormSubmit} method="POST">
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
				<a class="has-text-white" href="#"> Forgot password? </a>
			</span>
		</div>
	</div>
	<div class="level-right">
		<div class="level-item is-size-7">
			<p class="new_here_tag">
				New here?
				<span class="has-text-link">
					<a class="has-text-white" href="#"> Register an account </a>
				</span>
			</p>
		</div>
	</div>
</div>
