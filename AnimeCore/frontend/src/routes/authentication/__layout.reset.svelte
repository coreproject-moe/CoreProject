<script lang="ts">
	import { onMount } from "svelte";
	import { browser } from "$app/env";

	onMount(async () => {
		// https://bulma.io/documentation/components/navbar/#fixed-navbar
		const HTMLTAG = browser && document.getElementsByTagName("html")[0]; // '0' to assign the first (and only `HTML` tag)
		browser && HTMLTAG.classList.remove("has-navbar-fixed-top");
	});
</script>

<section class="hero is-fullheight">
	<div class="hero-body">
		<div class="container">
			<div class="columns is-centered is-desktop">
				<div class="column is-half-desktop is-full-mobile is-narrow-tablet">
					<div class="icon-box box has-background-black">
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
					<div class="box form-box has-background-black has-border-gray">
						<slot />
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style global lang="scss">
	.form-box {
		.input {
			border: 1px solid var(--border-color);

			&::placeholder {
				opacity: 0.75;
			}
		}

		.button {
			transition: 0.2s;
			opacity: 0.85;

			&:hover {
				background-color: var(--button-color-hover) !important;
				opacity: 1;
			}
		}

		.level {
			transition: 0.2s;
		}
		.new_here_tag {
			opacity: 0.85;
		}

		.error {
			color: var(--error-message-color);

			.error-list {
				&::marker {
					color: #b02a2a;
				}
			}
		}
	}
</style>
