<script lang="ts">
	import type { UIEventHandler } from 'svelte/elements';

	let klass = '';
	export let style = '';
	export let parentClass = '';
	export { klass as class };
	export let offsetScrollbar = false;

	export let scroll_top = 0;

	const onScroll: UIEventHandler<HTMLDivElement> = (event) => {
		const el = event?.currentTarget as HTMLElement;
		scroll_top = Math.round((el.scrollTop / (el.scrollHeight - el.clientHeight)) * 100);
	};

</script>


<div
	on:scroll={onScroll}
	{style}
	class="{parentClass} {offsetScrollbar
		? 'pr-3'
		: 'pr-0'} scrollbar overflow-hidden overflow-y-scroll overscroll-y-contain"
>
	<div class="{klass} whitespace-pre-line">
		<slot />
	</div>
</div>

<style lang="scss">
	.scrollbar {
		scrollbar-width: thin;
		scrollbar-color: rgba(255, 255, 255, 0.12);
		/* fill parent */
		display: block;
		width: 100%;
		height: 100%;
		/* set to some transparent color */
		border-color: rgba(255, 255, 255, 0);
		/* here we make the color transition */
		transition: border-color 0.2s linear;
		&:hover {
			/* the color we want the scrollbar on hover */
			border-color: rgba(255, 255, 255, 0.15);
		}
		&::-webkit-scrollbar,
		&::-webkit-scrollbar-corner,
		&::-webkit-scrollbar-thumb {
			width: 5px;
			border-radius: 16px;
			/* add border to act as background-color */
			border-right-style: inset;
			/* sum viewport dimensions to guarantee border will fill scrollbar */
			border-right-width: calc(100vw + 100vh);
			/* inherit border-color to inherit transitions */
			border-color: inherit;
		}
		&::-webkit-scrollbar-track {
			background: transparent !important;
		}
	}

	.scroll-top {
		mask-image: linear-gradient(0deg, rgba(7, 5, 25, 0.8) 80%, rgba(0, 0, 0, 0) 100%);
		mask-repeat: no-repeat;
		mask-position: top;
	}
	.scroll-bottom {
		mask-image: linear-gradient(180deg, rgba(7, 5, 25, 0.8) 80%, rgba(0, 0, 0, 0) 100%);
		mask-repeat: no-repeat;
		mask-position: bottom;
	}
	.scroll-middle {
		mask-image: linear-gradient(
			0deg,
			rgba(0, 0, 0, 0.5) 20%,
			rgba(7, 5, 25, 0.9) 40%,
			rgba(7, 5, 25, 0.9) 80%,
			rgba(0, 0, 0, 0.5) 100%
		);
		mask-repeat: no-repeat;
		mask-position: bottom;
	}
</style>
