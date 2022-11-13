<!-- https://github.com/baseplate-admin/CoreProject/blob/django-patch/backend/django_core/apps/user/templates/user/signup.html -->
<script lang="ts">
	import { createForm } from 'felte';
	import { validator } from '@felte/validator-yup';
	import * as yup from 'yup';

	let submitted;

	// Creating yup schema
	const schema = yup.object({
		email: yup.string().email().required(),
		password: yup.string().required(),
		type: yup.string().required()
	});

	// Creating the form
	const { form, data, unsetField, addField } = createForm({
		initialValues: {
			email: '',
			password: ''
		},
		onSubmit: (values) => (submitted = values),
		extend: [
			validator({ schema })
			// reporter()
		],
		// Debounced async validation
		debounced: {}
	});
	const KokoroColorWOrdMap: {
		[key: string]: string | undefined;
	} = {
		c: 'white',
		o: 'yellow',
		r: 'white',
		e: 'white',
		p: 'white',
		j: 'white',
		t: 'white'
	};

	const TailwindColorMap: {
		[key: string]: string | undefined;
	} = {
		white: 'text-white',
		yellow: 'text-warning'
	};

	function formatStringColor(input: string) {
		const string = 'coreproject';

		const stringRegex = new RegExp(string, 'gm');

		// There is no kokoro-chan in the input ( which is odd )
		if (!stringRegex.exec(input)) {
			return input;
		}

		const coloredWrappedWords = string.split('').map((word) => {
			return `<span class="inline-flex ${
				TailwindColorMap[
					KokoroColorWOrdMap[word] ?? 'white' //default to white
				]
			}">${word}</span>`;
		});

		// Color the font.
		input = input.replaceAll(stringRegex, coloredWrappedWords.join('').toString());

		return input;
	}
</script>

<svelte:head>
	<title>CoreProject | Sign Up</title>
</svelte:head>

<div
	style="grid-area: 1 / 1 / 2 / 2"
	class="inline-grid justify-center md:justify-end content-center"
>
	<div
		class="card w-96 bg-base-100 shadow-xl mr-0 md:mr-6 bg-transparent from-base-100 bg-gradient-to-t"
	>
		<div class="card-body rounded-2xl">
			<div class="flex justify-center mb-10">
				<div class="font-bold text-4xl">
					{@html formatStringColor('coreproject')}
				</div>
			</div>

			<div class="grid gap-6">
				<input
					style="--tw-bg-opacity:0.30"
					type="text"
					placeholder="Username"
					class="input w-full font-semibold max-w-xs border-[3px] border-warning"
				/>
				<input
					style="--tw-bg-opacity:0.30"
					type="text"
					placeholder="Email"
					class="input w-full font-semibold max-w-xs border-[3px] border-warning"
				/>
				<input
					style="--tw-bg-opacity:0.30"
					type="text"
					placeholder="Password"
					class="input w-full font-semibold max-w-xs border-[3px] border-warning"
				/>
				<input
					style="--tw-bg-opacity:0.30"
					type="text"
					placeholder="Confirm Password"
					class="input w-full font-semibold max-w-xs border-[3px] border-warning"
				/>
			</div>
			<div class="flex justify-center mt-5 items-center gap-2">
				<button class="btn btn-secondary font-bold text-black">Register</button>
				or <a class="underline" href="/login">login</a>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	.card {
		border-image: linear-gradient(
				to top,
				transparent 0.01%,
				white 20%,
				transparent,
				rgba(0, 0, 0, 0)
			)
			1 100%;
		border-image-width: 3px;
	}
	.card-body {
		z-index: 1;

		&::after {
			position: absolute;
			top: 0px;
			bottom: 0px;
			left: 0px;
			right: 0px;
			z-index: -1;
			box-shadow: inset 0 -3px 0 0 rgba(250, 250, 250, 0.9);
			content: '';
			border-radius: 16px;
		}
	}
</style>
