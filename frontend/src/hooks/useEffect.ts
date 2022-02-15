import { afterUpdate, onDestroy } from 'svelte';

export async function useEffect(cb: CallableFunction, deps: CallableFunction) {
	let cleanup: CallableFunction;

	async function apply() {
		if (cleanup) {
			await cleanup();
		}
		cleanup = await cb();
	}

	if (deps) {
		let values = [];
		afterUpdate(async () => {
			const new_values = deps();
			if (new_values?.some((value: Array<never>[], i: never) => value !== values[i])) {
				await apply();
				values = new_values;
			}
		});
	} else {
		// no deps = always run
		afterUpdate(apply);
	}

	onDestroy(async () => {
		if (cleanup) {
			await cleanup();
		}
	});
}
