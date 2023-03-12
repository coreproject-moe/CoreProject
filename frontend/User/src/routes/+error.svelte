<script lang="ts">
	import { page } from '$app/stores';
	import Alone from '$kaomoji/Alone.svelte';
	import Confused from '$kaomoji/Confused.svelte';
	import HowCouldYouDoIt from '$kaomoji/HowCouldYouDoIt.svelte';
	import OverWorked from '$kaomoji/Overworked.svelte';

	const KokoroColorWOrdMap: {
		[key: string]: string | undefined;
	} = {
		'-': 'white',
		a: 'white',
		c: 'white',
		h: 'white',
		k: 'white',
		n: 'white',
		o: 'yellow',
		r: 'white'
	};

	const TailwindColorMap: {
		[key: string]: string | undefined;
	} = {
		white: 'text-white',
		yellow: 'text-warning'
	};

	function formatKokoroColor(input: string) {
		const kokoroRegex = new RegExp(/kokoro-chan/gm);

		// There is no kokoro-chan in the input ( which is odd )
		if (!kokoroRegex.exec(input)) {
			return input;
		}

		const coloredWrappedWords = 'kokoro-chan'.split('').map((word) => {
			return `<span class="inline-flex ${
				TailwindColorMap[
					KokoroColorWOrdMap[word] ?? 'white' //default to white
				]
			}">${word}</span>`;
		});

		// Color the font.
		input = input.replaceAll(kokoroRegex, coloredWrappedWords.join('').toString());
		// Hyperlink the home
		return input;
	}

	const errorPages = {
		403: {
			text: formatKokoroColor(
				`Even to her precious user-kun, kokoro-chan has some secrets that she wants to hide. Well, since there’s nothing you can do about that, you can go back home, browse the forums or come say hi!`
			),
			kaomoji: {
				component: Alone,
				width: 321,
				height: 118
			}
		},
		404: {
			text: formatKokoroColor(
				`Our hardworking kokoro-chan was unable to find that page. While she collects more data on it, why don’t you go back home, explore some random anime, browse the forums or come say hi!`
			),
			kaomoji: {
				component: Confused,
				width: 414,
				height: 123
			}
		},
		418: {
			text: formatKokoroColor(
				`kokoro-chan refuses to brew coffee with a teapot. While she buys an electric coffee maker, why don’t you go back home, explore some random anime, browse the forums or come say hi!`
			),
			kaomoji: {
				component: HowCouldYouDoIt,
				width: 309,
				height: 108
			}
		},
		500: {
			text: formatKokoroColor(
				`Uh-oh, looks like our cute kokoro-chan worked really hard for the past few days and has now fallen asleep. You can wait for her to wake up by looking at the status page, or come say hi to other fellow kokoro-chan worshippers! ah- also let’s wish her sweet dreams!`
			),
			kaomoji: {
				component: OverWorked,
				width: 387,
				height: 114
			}
		}
	};

	// Thanks stackoverflow
	// https://stackoverflow.com/questions/57086672/element-implicitly-has-an-any-type-because-expression-of-type-string-cant-b
	let errorPage = errorPages[Number($page.status) as keyof typeof errorPages] ?? undefined;

	const errorMessage = $page?.error?.message as string;
</script>

<svelte:head>
	<title>CoreProject | {$page.status}</title>
</svelte:head>

<div class="flex items-center justify-center h-screen flex-col text-center gap-12">
	<svelte:component
		this={errorPage?.kaomoji.component}
		width={errorPage?.kaomoji?.width}
		height={errorPage?.kaomoji.height}
	/>
	<h1 class="text-indigo-700 text-3xl">
		<b>{$page.status}</b>
		-
		<b>{errorMessage}</b>
	</h1>
	<p class="w-[70vw] font-bold">
		{@html errorPage?.text}
	</p>
</div>
