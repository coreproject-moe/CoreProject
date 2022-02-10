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
			class={`columns is-mobile ${
				$responsiveMode === 'mobile' || $responsiveMode === 'tablet'
					? 'is-flex-direction-column'
					: 'is-flex-direction-row'
			}`}
		>
			<div class="column is-6">
				<table class="table is-bordered">
					<tbody>
						<tr>
							<td class="is-size-7">Name :</td>
							<td>anime.name</td>
						</tr>
						<tr>
							<td>Hello world</td>
						</tr>
						<tr>
							<td>Hello world</td>
						</tr>
						<tr>
							<td>Hello world</td>
						</tr>
					</tbody>
				</table>
			</div>
			<div class="column is-narrow">Second column</div>
		</div>
	</div>
</section>
