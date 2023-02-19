<script lang="ts">
	import reporter from '@felte/reporter-tippy';
	import { validator } from '@felte/validator-yup';
	import { createForm } from 'felte';
	import Cookies from 'js-cookie';
	import * as yup from 'yup';

	import { page } from '$app/stores';
	import { UrlMaps } from '$lib/urls';
	import CoreProject from '$icons/CoreProject.svelte';
	const urls = new UrlMaps();
	// Creating yup schema
	const schema = yup.object({
		username: yup
			?.string()
			?.required('Please Enter User Name')
			?.min(0)
			?.max(50, 'User name must be less than 50 Characters'),
		password: yup
			?.string()
			?.min(8, 'Password must be more than 8 Characters')
			?.max(1024, 'Password must be less than 1024 Characters')
	});

	// Creating the form
	const { form } = createForm({
		initialValues: {
			username: '',
			password: ''
		},
		onSubmit: async (values /*context*/) => {
			const data = new FormData();
			data.append('username', values.username);
			data.append('password', values.password);

			const res = await fetch(urls.login_url, {
				method: 'post',
				body: data
			});
			if (res.ok) {
				const data = await res.json();
				Cookies.set('token', data.token, { domain: $page.url.hostname });
			}
		},
		// onSuccess(response, context) {
		// 	// Do something with the returned value from `onSubmit`.
		// },
		// onError(err, context) {
		// 	// Do something with the error thrown from `onSubmit`.
		// },
		extend: [
			validator({ schema }),
			reporter({
				tippyProps: {
					allowHTML: true
				}
			})
		]

		// Debounced async validation
		// debounced: {}
	});
</script>

<svelte:head>
	<title>CoreProject | Login</title>
</svelte:head>

<form use:form>
	<div class="flex justify-center mb-10">
		<CoreProject />
	</div>

	<div class="grid gap-6">
		<input
			style="--tw-bg-opacity:0.30"
			type="text"
			placeholder="Username or Email"
			name="username"
			class="input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0"
		/>

		<input
			style="--tw-bg-opacity:0.30"
			type="text"
			placeholder="Password"
			name="password"
			class="input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0"
		/>
	</div>
	<div class="flex justify-center mt-5 items-center gap-2">
		<button class="btn btn-secondary font-bold text-black" type="submit">Login</button>
		or <a class="underline" href="/signup">signup</a>
	</div>
</form>
