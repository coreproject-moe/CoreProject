<script>
	import { page } from '$app/stores';
	import { projectName } from '$lib/constants/frontend/projectName';
	import { responsiveMode } from '$lib/store/responsive';
	const params = $page.params.slug;
</script>

<svelte:head>
	<title
		>{params
			.split('_')
			.filter((x) => x.length > 0)
			.map((x) => x.charAt(0).toUpperCase() + x.slice(1))
			.join(' ')} | {projectName}</title
	>
</svelte:head>

<section class="hero is-fullheight-with-navbar">
	<div class="hero-body is-flex-direction-column">
		<div
			class={`columns is-desktop container ${
				$responsiveMode === 'mobile' ? 'is-flex-direction-column' : 'is-flex-direction-row'
			}`}
		>
			<div
				class={`column is-align-self-center is-flex is-justify-content-center 
				${$responsiveMode === 'desktop' ? 'is-3' : ''}`}
			>
				<table
					class={`table is-bordered has-text-white has-background-black ${
						$responsiveMode === 'desktop' ? 'is-position-fixed' : ''
					}`}
					style={$responsiveMode === 'desktop' ? 'top: 5em;' : 'width: 80%;'}
				>
					<tbody>
						<tr>
							<td colspan="2" class="pb-0 pt-0 pr-0 pl-0 is-borderless">
								<div class="is-align-self-center is-flex is-justify-content-center pb-1">
									<div
										class="progressive replace"
										data-href="https://cdn.myanimelist.net/images/anime/6/73245.jpg"
										style="border-top-left-radius: 10px;border-top-right-radius: 10px;"
									>
										<img alt="" src="/placeholder-225x350.avif" class="preview" />
									</div>
								</div>
							</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Name :</p></td>
							<td>anime.name</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Score :</p></td>
							<td> anime.score</td>
						</tr>
						<tr>
							<td>
								<p class="is-size-7">Episodes :</p>
							</td>
							<td>anime.episodes</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Aired :</p></td>
							<td>anime.aired_from</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Producers:</p></td>
							<td>anime.producers</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Studios :</p></td>
							<td>anime.studios</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Source :</p></td>
							<td>anime.source</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Genres :</p></td>
							<td>anime.genres</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Theme :</p></td>
							<td>anime.theme</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Duration :</p></td>
							<td>anime.duration</td>
						</tr>
						<tr>
							<td><p class="is-size-7">Rating :</p></td>
							<td>anime.rating</td>
						</tr>
					</tbody>
				</table>
			</div>
			<div class={`column is-flex ${$responsiveMode === 'desktop' ? '' : 'is-align-self-center'}`}>
				<div class="content has-text-white">
					<h1 class="has-text-white">Hello World</h1>
					<p>
						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan, metus ultrices
						eleifend gravida, nulla nunc varius lectus, nec rutrum justo nibh eu lectus. Ut
						vulputate semper dui. Fusce erat odio, sollicitudin vel erat vel, interdum mattis neque.
						Sub<sub>script</sub> works as well!
					</p>
					<h1 class="has-text-white">Episodes :</h1>

					<div class="grid-container">
						{#each Array(100) as _, i}
							<div class="grid-item is-size-6 has-border-white is-clickable">{i}</div>
						{/each}
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<style lang="scss">
	.grid-container {
		display: grid;
		align-items: center;
		grid-template-columns: repeat(auto-fit, minmax(4em, 1fr));
		background-color: black;
	}
	.grid-item {
		background-color: black;
		padding: 1.2em;
		text-align: center;
	}
</style>
