import { afterUpdate, onDestroy } from 'svelte';

export function useEffect(cb: CallableFunction, deps: CallableFunction) {
	let cleanup: CallableFunction;

	function apply() {
		if (cleanup) {
			cleanup();
		}
		cleanup = cb();
	}

	if (deps) {
		let values = [];
		afterUpdate(() => {
			const new_values = deps();
			if (new_values?.some((value, i) => value !== values[i])) {
				apply();
				values = new_values;
			}
		});
	} else {
		// no deps = always run
		afterUpdate(apply);
	}

	onDestroy(() => {
		if (cleanup) {
			cleanup();
		}
	});
}
