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
</script>

<div
	style="grid-area: 1 / 1 / 2 / 2"
	class="inline-grid justify-center md:justify-end content-center"
>
	<div class="card w-96 bg-base-100 shadow-xl mr-0 md:mr-6 bg-transparent">
		<div class="card-body">
			<input
				class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
				id="username"
				type="text"
				placeholder="Username"
			/>
		</div>
	</div>
</div>
