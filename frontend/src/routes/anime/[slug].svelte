<script>
	import { page } from '$app/stores';
	import { responsiveMode } from '$lib/store/responsive';
	{
		$page.params.slug;
	}
</script>

<section class="hero is-fullheight-with-navbar">
	<div class="hero-body is-flex-direction-column">
		<div
			class={`columns is-mobile container ${
				$responsiveMode === 'mobile' ? 'is-flex-direction-column' : 'is-flex-direction-row'
			}`}
		>
			<div
				class={`column is-align-self-center is-flex is-justify-content-center ${
					$responsiveMode === 'mobile' ? 'is-10' : ''
				}
			${$responsiveMode === 'tablet' ? 'is-5' : ''}
			${$responsiveMode === 'desktop' ? 'is-3' : ''}`}
			>
				<table class="table is-bordered has-text-white" style="background-color:black; ">
					<tbody>
						<tr>
							<td
								colspan="2"
								style="border: none;padding-top: 0;padding-bottom: 0;padding-right: 0;padding-left: 0;"
							>
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
			<div
				class={`column is-7 is-flex ${$responsiveMode === 'desktop' ? '' : 'is-align-self-center'}`}
			>
				<div class="content  has-text-white">
					<h1 class="has-text-white">Hello World</h1>
					<p>
						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla accumsan, metus ultrices
						eleifend gravida, nulla nunc varius lectus, nec rutrum justo nibh eu lectus. Ut
						vulputate semper dui. Fusce erat odio, sollicitudin vel erat vel, interdum mattis neque.
						Sub<sub>script</sub> works as well!
					</p>
				</div>
			</div>
		</div>
	</div>
</section>
