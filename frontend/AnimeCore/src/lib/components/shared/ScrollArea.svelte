<script lang="ts">
	let klass = '';
	export let style = '';
	export let parentClass = '';
	export { klass as class };
	export let offsetScrollbar = false;
	export let primaryColor = "#ffffff";
	export let fadeColor = "transparent";
	export let fadeHeight = "20px";


	let overlayClasses = [];
	const handleScroll = (e) => {
		let scrollableScrollTop = e.target.scrollTop;
	    let contentHeight = e.target.clientHeight;
	    let atBottom = e.target.scrollHeight === contentHeight + scrollableScrollTop;
	    let updatedOverlayClasses = [];
	    overlayClasses = updatedOverlayClasses;

	    if (scrollableScrollTop === 0) {
	      updatedOverlayClasses.push("top");
	    }
	    if (atBottom) {
	      updatedOverlayClasses.push("bottom");
	    }
	    console.log(overlayClasses)
	}
</script>


<div
	on:scroll={handleScroll}
	{style}
	class="{parentClass} {offsetScrollbar
		? 'pr-3'
		: 'pr-0'} scrollbar overflow-hidden overflow-y-scroll overscroll-y-contain relative"
>
	<div class="overlay {overlayClasses.map(s => styles[s])}" />
	<div class="{klass} whitespace-pre-line content">
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

	.overlay {
		width: 100%;
		height: 100%;
		display: block;
		position: -webkit-sticky;
		position: -moz-sticky;
		position: -ms-sticky;
		position: -o-sticky;
		position: sticky;
		z-index: 1;
		top: 0px;
		pointer-events: none;
		&:before, &:after {
		    content: "";
		    width: 100%;
		    height: 40px;
		    background: transparent;
		    position: absolute;
		}
		&:before {
		    top: 0px;
		    background: linear-gradient(white, transparent);
		}
		&:after {
		    bottom: 0px;
		    background: linear-gradient(transparent, white);
		}
		&.top {
		    &:before {
		      display: none;
		    }
		}
		&.bottom {
		    &:after {
		      display: none;
		    }
		}
	}
</style>
