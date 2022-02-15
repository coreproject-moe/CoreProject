<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/env';

	onMount(async () => {
		// https://bulma.io/documentation/components/navbar/#fixed-navbar
		const HTMLTAG = browser && document.getElementsByTagName('html')[0]; // '0' to assign the first (and only `HTML` tag)
		browser && HTMLTAG.classList.remove('has-navbar-fixed-top');
	});
</script>

<section class="hero is-fullheight">
	<div class="hero-body">
		<div class="container">
			<div class="columns is-centered is-desktop">
				<div class="column is-half-desktop is-full-mobile is-narrow-tablet">
					<div class="icon-box box">
						<div class="columns is-mobile is-centered">
							<div class="column is-narrow">
								<div
									data-href="/placeholder-96x96.avif"
									class="progressive replace"
									style="border-radius: 9999px"
								>
									<img
										src="/logo.avif"
										style="width: 150px; height: 40px"
										width="150"
										height="40"
										alt=""
									/>
								</div>
							</div>
						</div>
					</div>
					<div class="box form-box">
						<slot />
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style global lang="scss">
	.icon-box {
		background-color: transparent !important;
	}
	.form-box {
		background-color: transparent !important;
		border: 1.95px solid var(--border-color);

		.items {
			padding: 0.4em;
		}

		.input {
			background-color: transparent !important;
			border: 1px solid var(--border-color);
			color: white;

			&::placeholder {
				color: white !important;
				opacity: 0.75;
				font-family: 'Ubuntu';
			}
		}

		.button {
			border-color: var(--button-border-color) !important;
			border-width: 1.8px;
			text-decoration: none !important;
			color: hsl(0, 0%, 85%) !important;
			transition: 0.2s;

			&:hover {
				background-color: var(--button-color-hover) !important;
			}
		}

		.level {
			transition: 0.2s;
		}
		.new_here_tag {
			font-family: 'Cantarell';
			color: white;
			opacity: 0.85;
		}

		.error {
			color: var(--error-message-color);
		}
		.error-list::marker {
			color: #b02a2a;
		}
		a.has-text-white {
			text-decoration-line: underline;
			text-underline-offset: 4px;
		}
	}
</style>
