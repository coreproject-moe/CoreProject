<script context="module" lang="ts">
	import { get } from "svelte/store";
	import { browser } from "$app/env";
	import { userToken } from "$lib/store/users";

	export async function load({ fetch }) {
		// For the love of GOD.
		// Run this only in Browser.
		// Wasted 2+ hours debugging this stupid shit.
		if (browser && get(isUserAuthenticated)) {
			try {
				const res = await fetch(userInfoUrl, {
					method: "GET",
					headers: new Headers({
						Accept: "application/json",
						"Content-Type": "application/json",
						Authorization: `Bearer ${get(userToken).access}`
					})
				});
				const data = await res.json();

				return {
					props: {
						userInfo: data
					}
				};
			} catch (err) {
				if (err instanceof Error) {
					userToken.set({ refresh: "", access: "" });
					console.error(`Can't fetch from backend | Flushing Tokens | Reason : ${err.message}`);
				}
			}
		}
		return {
			props: {
				userInfo: {}
			}
		};
	}
</script>

<script lang="ts">
	export let userInfo = {
		first_name: "",
		last_name: "",
		email: "",
		date_joined: "",
		username: "",
		id: 0,
		last_login: "",
		avatar: ""
	};
	// Main SCSS import
	import "../app.scss";

	// Import JS libraries
	import anime from "animejs";
	import tippy from "tippy.js";
	import dayjs from "dayjs";
	import md5 from "md5";

	// Svelte Import
	import { onMount } from "svelte";

	// Responsive helper
	import { responsiveMode } from "$lib/store/responsive";
	import { isUserAuthenticated } from "$lib/store/users";

	import { useEffect } from "$hooks/useEffect";

	// Constants
	import { baseUrl } from "$lib/constants/backend/urls/baseUrl";
	import { userInfoUrl } from "$lib/constants/backend/urls/restEndpoints";
	import { signupPageUrl, userEditInfoPageUrl } from "$lib/constants/backend/urls/pageUrlEndpoints";

	import { goto } from "$app/navigation";
	import { page } from "$app/stores";

	let arrowButtonTurned = false;

	let navbarBurger: HTMLElement;
	let navbarBurgerClosed = false;
	// Auto close the navbar Buger to close if its on Mobile or Tablet
	$: navbarBurgerClosed = $responsiveMode === "mobile" || $responsiveMode === "tablet";

	// Listen to changes on arrow button
	useEffect(
		() => {
			switch (arrowButtonTurned) {
				case true: {
					anime({
						targets: ".animejs__github__button",
						translateX: 0,
						easing: "easeOutSine",
						duration: 50,
						opacity: 1,
						scale: 1
					});
					break;
				}
				case false: {
					anime({
						targets: ".animejs__github__button",
						translateX: 40,
						easing: "easeOutSine",
						duration: 50,
						opacity: 0,
						scale: 0.2
					});
					break;
				}
			}
		},
		() => [arrowButtonTurned]
	);

	onMount(async () => {
		// https://bulma.io/documentation/components/navbar/#fixed-navbar
		const HTMLTAG = browser && document.getElementsByTagName("html")[0]; // '0' to assign the first (and only `HTML` tag)
		browser && HTMLTAG.classList.add("has-navbar-fixed-top");

		// AnimeJS
		anime({
			targets: ".animejs__arrow__back",
			easing: "linear",
			duration: 100,
			color: "hsl(0, 0%, 80%)"
		});

		// TippyJS

		tippy(".animejs__github__button", {
			content: "Github",
			theme: "black",
			touch: false
		});

		tippy(".tippyjs__avatar__picture", {
			content: `<b>ID</b> : ${userInfo?.id} <br /> <b>First Name</b> : ${
				userInfo?.first_name
			}<br/> <b>Last Name</b> : ${userInfo?.last_name}<br/> <b>Username</b> : ${
				userInfo?.username
			}<br/>  <b>Email</b> : ${userInfo?.email}<br/><b>Date Joined</b> : ${dayjs(
				userInfo?.date_joined
			)}<br/>
			<b>Last Active</b> : ${dayjs(userInfo?.last_login)}`,
			theme: "black",
			allowHTML: true,
			touch: false,
			placement: "bottom",
			trigger: get(responsiveMode) === "mobile" ? "click" : "mouseenter focus",
			triggerTarget: get(responsiveMode) === "mobile" ? navbarBurger : null,
			interactive: get(responsiveMode) === "mobile" ? true : false,
			appendTo: () => document.body
		});
	});
</script>

<nav
	class={`navbar is-clipped has-background-black is-fixed-top ${
		$responsiveMode === "widescreen" ? "" : "container"
	}`}
	style="z-index:100;"
>
	<div class="navbar-brand is-clipped">
		<a class="navbar-item is-clickable" href="https://bulma.io">
			<img src="/logo.avif" alt="logo" width={112} height={28} />
		</a>

		<button
			class={`navbar-burger has-text-white is-clickable ${navbarBurgerClosed ? "" : "is-active"}`}
			bind:this={navbarBurger}
			style="margin-top: -0.5em"
			aria-label="menu"
			aria-expanded="false"
			on:click|preventDefault={async () => {
				navbarBurgerClosed = !navbarBurgerClosed;
			}}
		>
			<span class="has-text-white" aria-hidden="true" />
			<span class="has-text-white" aria-hidden="true" />
			<span class="has-text-white" aria-hidden="true" />
		</button>
	</div>

	<div class={`navbar-menu has-background-black ${navbarBurgerClosed ? "" : "is-active"}`}>
		<div
			class={`navbar-start mt-3 ${
				$responsiveMode === "mobile" || $responsiveMode === "tablet"
					? "is-flex is-flex-direction-row is-justify-content-center"
					: ""
			}`}
		>
			<a
				href="/home"
				sveltekit:prefetch
				class={`navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration ${
					$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "pl-2 pr-2" : "ml-2"
				} ${$page.url.pathname.includes("home") ? "hover" : ""}
					`}
				on:mouseenter={async () => {
					anime({
						targets: ".animejs__home__icon",
						color: "#e50000"
					});
				}}
				on:mouseleave={async () => {
					anime({
						targets: ".animejs__home__icon",
						color: "#d9d9d9"
					});
				}}
			>
				<ion-icon name="home-sharp" class="animejs__home__icon" />
				<p
					class={`${
						$responsiveMode === "mobile" || $responsiveMode === "tablet"
							? "pt-2 nav-icon-button"
							: ""
					}
						${$responsiveMode === "widescreen" ? "is-size-7" : ""}`}
				>
					<span class="is-hidden-touch">&nbsp;</span> Home
				</p>
			</a>
			<a
				href="/anime"
				sveltekit:prefetch
				class={`navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration ${
					$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "pl-2 pr-2" : "ml-2"
				} ${$page.url.pathname.includes("anime") ? "hover" : ""}
					`}
				on:mouseenter={async () => {
					anime({
						targets: ".animejs__anime__icon",
						color: "#e50000"
					});
				}}
				on:mouseleave={async () => {
					anime({
						targets: ".animejs__anime__icon",
						color: "#d9d9d9"
					});
				}}
			>
				<ion-icon name="film-outline" class="animejs__anime__icon" />
				<p
					class={`${
						$responsiveMode === "mobile" || $responsiveMode === "tablet"
							? "pt-2 nav-icon-button"
							: ""
					} ${$responsiveMode === "widescreen" ? "is-size-7" : ""}`}
				>
					<span class="is-hidden-touch">&nbsp;</span>
					Anime
				</p>
			</a>
			<a
				href="/manga"
				sveltekit:prefetch
				class={`navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration ${
					$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "pl-2 pr-2" : "ml-2"
				} ${$page.url.pathname.includes("manga") ? "hover" : ""}`}
				on:mouseenter={async () => {
					anime({
						targets: ".animejs__manga__icon",
						color: "#e50000"
					});
				}}
				on:mouseleave={async () => {
					anime({
						targets: ".animejs__manga__icon",
						color: "#d9d9d9"
					});
				}}
			>
				<ion-icon name="images-outline" class="animejs__manga__icon" />
				<p
					class={`${
						$responsiveMode === "mobile" || $responsiveMode === "tablet"
							? "pt-2 nav-icon-button"
							: ""
					} ${$responsiveMode === "widescreen" ? "is-size-7" : ""}`}
				>
					<span class="is-hidden-touch">&nbsp;</span> Manga
				</p>
			</a>
			<a
				sveltekit:prefetch
				href="/soundcore"
				class={`navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration ${
					$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "pl-2 pr-2" : "ml-2"
				} ${$page.url.pathname.includes("soundcore") ? "hover" : ""}`}
				on:mouseenter={async () => {
					anime({
						targets: ".animejs__music__icon",
						color: "#e50000"
					});
				}}
				on:mouseleave={async () => {
					anime({
						targets: ".animejs__music__icon",
						color: "#d9d9d9"
					});
				}}
			>
				<ion-icon name="musical-note-outline" class="animejs__music__icon" />
				<p
					class={`${
						$responsiveMode === "mobile" || $responsiveMode === "tablet"
							? "pt-2 nav-icon-button"
							: ""
					} ${$responsiveMode === "widescreen" ? "is-size-7" : ""}`}
				>
					<span class="is-hidden-touch">&nbsp;</span>
					Soundcore
				</p>
			</a>
			<a
				sveltekit:prefetch
				href="/shots"
				class={`navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration ${
					$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "pl-2 pr-2" : "ml-2"
				} ${$page.url.pathname.includes("shots") ? "hover" : ""}`}
				on:mouseenter={async () => {
					anime({
						targets: ".animejs__shots__icon",
						color: "#e50000"
					});
				}}
				on:mouseleave={async () => {
					anime({
						targets: ".animejs__shots__icon",
						color: "#d9d9d9"
					});
				}}
			>
				<ion-icon name="aperture-outline" class="animejs__shots__icon" />
				<p
					class={`${
						$responsiveMode === "mobile" || $responsiveMode === "tablet"
							? "pt-2 nav-icon-button"
							: ""
					} ${$responsiveMode === "widescreen" ? "is-size-7" : ""}`}
				>
					<span class="is-hidden-touch">&nbsp;</span>
					Shots
				</p>
			</a>
			<div class="control has-icons-left  ml-4 is-hidden-touch">
				<input
					class="input has-background-black has-text-white search__input"
					type="text"
					placeholder="Search Away"
				/>
				<span class="icon is-small is-left">
					<ion-icon name="search-outline" class="has-text-white is-size-4" />
				</span>
			</div>
		</div>
		<div class="navbar-end is-clipped">
			<div
				class={`navbar-item ${
					$responsiveMode === "mobile"
						? "is-flex is-flex-direction-row is-justify-content-center pt-6"
						: ""
				}`}
			>
				<button
					class={`is-rounded is-dark animejs__github__button has-background-black-bis is-clickable ${
						$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "is-hidden " : ""
					}`}
					on:mouseenter={async () => {
						anime({
							targets: ".animejs__logo__github",
							color: "hsl(0, 0%, 100%)"
						});
						anime({
							targets: ".animejs__github__button",
							scale: 1.3
						});
					}}
					on:mouseleave={async () => {
						anime({
							targets: ".animejs__logo__github",
							color: "hsl(0, 0%, 80%)"
						});
						anime({
							targets: ".animejs__github__button",
							scale: 1
						});
					}}
					on:click={async () => {
						goto("https://github.com/baseplate-admin/CoreProject");
					}}
				>
					<ion-icon
						class="animejs__logo__github has-text-white"
						style="width: 100%; height: 100%;"
						name="logo-github"
					/>
				</button>

				<button
					style="z-index: 1000000"
					class={`is-rounded is-dark animejs__arrow__button has-background-black-bis is-clickable ${
						$responsiveMode === "mobile" || $responsiveMode === "tablet" ? "is-hidden" : ""
					}`}
					on:mouseenter={async () => {
						anime({
							targets: ".animejs__arrow__back",
							color: "#e50000"
						});
						anime({
							targets: ".animejs__arrow__button",
							scale: 1.2
						});
					}}
					on:mouseleave={async () => {
						anime({
							targets: ".animejs__arrow__back",
							color: "hsl(0, 0%, 80%)"
						});
						anime({
							targets: ".animejs__arrow__button",
							scale: 1
						});
					}}
					on:click|preventDefault={async () => {
						arrowButtonTurned = !arrowButtonTurned;

						switch (arrowButtonTurned) {
							case true: {
								anime({
									targets: ".animejs__arrow__back",
									rotate: [0, 180]
								});
								break;
							}
							case false: {
								anime({
									targets: ".animejs__arrow__back",
									rotate: [180, 360]
								});
								break;
							}
						}
					}}
				>
					<ion-icon
						class="animejs__arrow__back"
						name="arrow-back-outline"
						style="width: 100%; height: 100%;"
					/>
				</button>
			</div>
			{#if $isUserAuthenticated}
				<div class="columns is-mobile is-centered">
					<div class="column is-narrow">
						<figure class="image is-48x48 pt-2 pl-2 tippyjs__avatar__picture">
							<a
								href={userEditInfoPageUrl}
								rel="external"
								data-href={userInfo?.avatar
									? `${baseUrl}${userInfo?.avatar}`
									: `https://seccdn.libravatar.org/avatar/${md5(userInfo.email)}/?s=64`}
								class="progressive replace"
								style="border-radius: 9999px; height:40px; width:40px; z-index: 1000000;margin: auto;"
							>
								<img
									class="is-rounded preview avatar-preview"
									alt="logo"
									src="/placeholder-64x64.avif"
								/>
							</a>
						</figure>
					</div>
				</div>
			{:else}
				<div class="navbar-item">
					<div class="columns is-mobile is-centered">
						<div class="column is-narrow">
							<div class="buttons">
								<a
									class="button has-text-white is-black has-border-gray is-rounded"
									href={`/authentication/login?next=${$page?.url?.pathname}`}
								>
									Log in
								</a>
								<a
									class="button has-text-white is-black has-border-gray is-rounded"
									href={`${signupPageUrl}?next=${$page?.url?.pathname}`}
								>
									Sign Up
								</a>
							</div>
						</div>
					</div>
				</div>
			{/if}
		</div>
	</div>
</nav>
<slot />

<style lang="scss">
	.navbar {
		// @TODO Fix this
		// border-bottom: 1px solid var(--border-color);

		.navbar-menu {
			.navbar-start {
				.button {
					margin-left: 0.3em;
					margin-bottom: 0.5em;
				}
			}
		}

		.navbar-burger {
			transition: 0.2s;
			transform: translateY(10px);
			text-decoration: none !important;
		}

		.navbar-start {
			.navbar-item {
				&.hover,
				&:hover {
					background-color: hsl(0, 0%, 7.8%) !important;
				}
			}
		}

		.navbar-item {
			button {
				width: 25px;
				height: 25px;
				margin-left: 1em !important;
				border-radius: 9999px;
				border-width: 1.8px;
				border-color: hsl(0, 0%, 20%) !important;
				transition: 0.2s;

				&:hover {
					background-color: hsl(0, 0%, 20%) !important;
				}
			}
		}

		.search__input {
			&:active,
			&:focus {
				border-color: rgb(175, 7, 7);
				box-shadow: 0 0 0 0.125em rgba(158, 13, 13, 0.76);
			}
		}
		.buttons {
			.button {
				border-color: var(--button-border-color) !important;
				border-width: 1.8px;
				text-decoration: none;
				transition: 0.2s;

				&:hover {
					background-color: var(--button-color-hover) !important;
				}
				&:focus {
					box-shadow: 0 0 0 0.125em rgba(199, 72, 72, 0.3) !important;
				}

				.centered_button {
					width: 50% !important;
				}
			}
		}
		.avatar-preview {
			position: absolute;
			top: -9999px;
			bottom: -9999px;
			left: -9999px;
			right: -9999px;
			margin: auto;
		}

		.mobile__friendly__avatar__stats {
			max-width: 20em;
			white-space: nowrap;
			text-overflow: ellipsis;
		}
	}
</style>
