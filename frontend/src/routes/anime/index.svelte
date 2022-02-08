<script>
	// Import Swiper Svelte components
	import { Swiper, SwiperSlide } from 'swiper/svelte';

	// Import Swiper styles
	import 'swiper/css';
</script>

<div class="container">
	<p class="title is-size-5 pt-6 has-text-white">
		<span class="pr-3 pl-3"
			><ion-icon name="rocket-outline" style="transform: translateY(4px)" /></span
		>
		Recent Uploads :
	</p>
	<div class="box" style="background-color: black; border: 1px solid white">
		<Swiper spaceBetween={50} slidesPerView={3} on:swiper={(e) => console.log(e.detail[0])}>
			<!-- {% for i in '0123456789012345678901234567890' %} -->
			<SwiperSlide>
				<div class="swiper-slide">
					<div class="card" style="background-color: black !important">
						<div class="card-image has-background-black">
							<figure class="image">
								<!-- <a
									style="
                                        border-top-left-radius: 10px;
                                        border-top-right-radius: 10px;
                                    "
									data-href="https://cdn.myanimelist.net/images/anime/6/73245.jpg"
									class="progressive replace"
								>
									<img
                                        src="{% static 'images/placeholder/225x350.avif' %}"
                                        class="preview"
                                        alt="image"
                                    /> 
								</a>-->
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
				</div>
			</SwiperSlide>
			<!-- {% endfor %} -->
		</Swiper>
	</div>
</div>
