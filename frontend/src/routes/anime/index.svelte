<script lang="ts">
	// Import Swiper Svelte components
	import { Swiper, SwiperSlide } from 'swiper/svelte';
	import { projectName } from '$lib/constants/frontend/projectName';

	import { responsiveMode } from '$lib/store/responsive';
	import { goto } from '$app/navigation';

	let swiperSpacesBetween: number;
	let swiperSlidesPerView: number;

	$: switch ($responsiveMode) {
		case 'mobile':
			swiperSpacesBetween = 10;
			swiperSlidesPerView = 2;
			break;
		case 'tablet':
			swiperSpacesBetween = 20;
			swiperSlidesPerView = 3;
			break;
		case 'desktop':
			swiperSpacesBetween = 30;
			swiperSlidesPerView = 5;
			break;
	}
</script>

<svelte:head>
	<title>AnimeCore | {projectName}</title>
</svelte:head>

<div class="container">
	<p class="title is-size-5 pt-6 has-text-white">
		<span class="pr-3 pl-3"
			><ion-icon name="rocket-outline" style="transform: translateY(4px)" /></span
		>
		Recent Uploads :
	</p>
	<div class="box" style="background-color: black; border: 1px dotted white">
		<Swiper spaceBetween={swiperSpacesBetween} slidesPerView={swiperSlidesPerView}>
			{#each Array(12) as _}
				<SwiperSlide>
					<div
						class="card is-clickable"
						style="background-color: black !important;"
						on:click={async () => {
							goto('/anime/one_piece');
						}}
					>
						<div class="card-image has-background-black">
							<figure class="image">
								<div
									style="
                                        border-top-left-radius: 10px;
                                        border-top-right-radius: 10px;
										
                                    "
									data-href="https://cdn.myanimelist.net/images/anime/6/73245.jpg"
									class="progressive replace"
								>
									<img src="/placeholder-225x350.avif" class="preview" alt="" />
								</div>
							</figure>
						</div>
						<div
							class="card-content has-background-black-bis"
							style="
                                border-bottom-left-radius: 10px;
                                border-bottom-right-radius: 10px;
                            "
						>
							<div class="media">
								<div class="media-content is-clipped">
									<p class="title is-4 has-text-white">One Piece</p>
									<p class="subtitle is-6 has-text-white">
										Episodes : <span>&infin;</span>
										<br />
										Duration : total.secnds <br />
									</p>
									<div class="field is-grouped is-grouped-multiline">
										<div class="control">
											<div class="tags has-addons">
												<span class="tag is-dark heading">sub</span>
												<span class="tag is-info heading">dub</span>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</SwiperSlide>
			{/each}
		</Swiper>
	</div>
</div>
