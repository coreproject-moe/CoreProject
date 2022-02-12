<script lang="ts">
	import { projectName } from '$lib/constants/frontend/projectName';
</script>

<svelte:head>
	<title>Home Page | {projectName}</title>
</svelte:head>

<section class="hero is-fullheight-with-navbar">
	<div class="hero-body is-flex-direction-column">
		<div class="container has-text-centered">
			<p class="title has-text-white">Imagine a place,</p>
			<p class="subtitle has-text-white">
				where you can get all of your <br />
				animes, mangas, songs, share <br />
				your favorite anime pictures.<br />
			</p>
		</div>
		<div class="container pt-6">
			<p class="title has-text-centered has-text-white">Anime</p>
			<p class="subtitle has-text-centered has-text-white">
				Powered by
				<a
					class="has-text-white"
					href="https://github.com/baseplate-admin/CoreProject/tree/main/pages/anime">AnimeCore.</a
				>
				<br />
				The modern full stack anime streaming program.
			</p>
		</div>
		<div class="container pt-6">
			<p class="title has-text-centered has-text-white">Manga</p>
		</div>
		<div class="container pt-6">
			<p class="title has-text-centered has-text-white">OST</p>
			<p class="subtitle has-text-centered has-text-white">
				Powered by SoundCore.<br />
				The modern Single Page music streaming program.
			</p>
		</div>
		<div class="container pt-6">
			<p class="title has-text-centered has-text-white">Shots</p>
		</div>
		<div class="container pt-6">
			<div class="content">
				<h2 class="has-text-white has-text-centered">FAQ</h2>

				<details>
					<summary class="has-text-white"> How do you plan to fund this site? </summary>
					<p class="pl-4 pt-2 has-text-white">
						<span class="is-size-5">⇢</span>
						I don't know. For now at least <br />
						<span class="pl-5">
							But I have made the site to be <br />
						</span>
						<span class="pl-5"> as cost effective as possible. </span><br />
						<span class="pl-5"> I plan to have a patreon at some point. </span>
					</p>
				</details>
				<details>
					<summary class="has-text-white pt-2"> How do I get banned ? </summary>
					<p class="has-text-white pl-4 pt-2">
						<span class="is-size-5">⇢</span>
						I plan to ban nobody. <br />
						<span class="pl-5">But if you can't access the site</span>

						<a class="has-text-white" href="https://github.com/baseplate-admin/coreProject/"
							>submit an issue</a
						>.
					</p>
				</details>

				<details>
					<summary class="has-text-white pt-2"> How do I set an avatar ? </summary>
					<p class="has-text-white pl-4 pt-2">
						<span class="is-size-5">⇢</span>
						You can set your own avatar by going to <br />
						<span class="pl-5"
							><a class="has-text-white" href="https://www.libravatar.org/">Libravatar</a>
							and opening an account with</span
						>
						<br />
						<span class="pl-5"> the mail you used to open an account in this site. </span>
					</p>
				</details>
				<details>
					<summary class="has-text-white pt-2"> Where do you get the contents from? </summary>
					<p class="pl-4 pt-2 has-text-white">
						<span class="is-size-5">⇢</span> Mostly from
						<a class="has-text-white" href="https://nyaa.si">nyaa</a>
					</p>
				</details>
				<details>
					<summary class="has-text-white pt-2"> Do you store the contents in your server? </summary>
					<dl class="pl-4 pt-2 has-text-white">
						<dl>
							<span class="is-size-5">⇢</span>
							I plan to serve the content directly from the server.
							<br />
							<span class="pl-5"> So the workflow is </span>
							<p class="is-size-5 has-text-centered">↧</p>
						</dl>
						<dd>Nyaa → My PC → CDN → Server → User</dd>
					</dl>
				</details>
				<details>
					<summary class="has-text-white pt-2"> What will you do to a DMCA takedown? </summary>
					<p class="pl-4 pt-2 has-text-white">
						<span class="is-size-5">⇢</span>
						I am not storing much for this site.
						<br />
						<span class="pl-5">But in reality our site will eventually be DMCA striked. </span>
						<br />
						<span class="pl-5">Thats why this site will have an import export feature.</span>
						<br /><span class="pl-5"> Since the code is </span>
						<a class="has-text-white" href="https://github.com/baseplate-admin/coreProject/"
							>open source</a
						>
						,<br /><span class="pl-5">anyone can host the site</span>
						<br />
						<span class="pl-5"> and the user can just import the data. </span>
					</p>
				</details>
				<details>
					<summary class="has-text-white pt-2"> When can we expect a working site ? </summary>
					<p class="has-text-white pl-4 pt-2">
						<span class="is-size-5">⇢</span>
						I don't know actually. <br />
						<span class="pl-5"> With my current financial status, </span>
						<br />
						<span class="pl-5">it's really hard for me to host this site.</span>
					</p>
				</details>
				<details>
					<summary class="has-text-white pt-2">
						Whats the gurantee that an anime will stay forever?
					</summary>
					<p class="has-text-white pl-4 pt-2">
						<span class="is-size-5">⇢</span>
						Theres no gurantee.<br />
						<span class="pl-5"> But we have 2 cloud provider, </span>
						<br />
						<span class="pl-5">an offline hard disk backup.</span>
						<br />
						<span class="pl-5"> Unless we get DMCA striked at both CDN, </span>
						<br />
						<span class="pl-5"> my house catches on fire, </span>
						<br /><span class="pl-5"> all the content uploaded on the </span>
						<br />
						<span class="pl-5">site should stay for lifetime</span>
					</p>
				</details>
				<details>
					<summary class="has-text-white pt-2"> But the x,y,z site does this better. </summary>
					<p class="has-text-white pl-4 pt-2">
						<span class="is-size-5">⇢</span>
						I am sorry i couldn't meet your expectations<br />
						<span class="pl-5">
							So maybe you can make
							<a class="has-text-white" href="https://github.com/baseplate-admin/coreProject/"
								>this</a
							>
							site look even better?
						</span>
					</p>
				</details>

				<details>
					<summary class="has-text-white pt-2">
						What tech stack did you choose for this site?
					</summary>
					<p class="has-text-white pl-4 pt-2">
						<span class="is-size-5">⇢</span>
						Python
						<br />
						<span class="is-size-5 pl-5"> •</span>
						Django ( Web Framework )
						<br />
						<span class="is-size-5 pl-5">•</span>
						Uvicorn ( ASGI Server )
						<br />
						<span class="is-size-5 pl-5">•</span>
						Gunicorn ( Web Server )
						<br />
						<span class="is-size-5 pl-5">•</span>
						HTTPX ( HTTP Client )
						<br />
						<span class="is-size-5">⇢</span>
						GoLang
						<br />
						<span class="is-size-5 pl-5">•</span>
						Caddy ( Reverse Proxy )
						<br />
						<span class="is-size-5">⇢</span>
						JavaScript
						<br />
						<span class="is-size-5 pl-5">•</span>
						Svelte ( SPA Library )
						<br />
						<span class="is-size-5 pl-5">•</span>
						AnimeJS ( Animation Library )
						<br />
						<span class="is-size-5 pl-5">•</span>
						Tippy ( Tooltip Library )
						<br />
						<span class="is-size-5 pl-5">•</span>
						VideoJS ( Player )
						<br />
						<span class="is-size-5">⇢</span>
						CSS
						<br />
						<span class="is-size-5 pl-5">•</span>
						Bulma ( Framework )
						<br />
						<span class="is-size-5">⇢</span>
						Extras
						<br />
						<span class="is-size-5 pl-5">•</span>
						Ionicons ( Icon Library )
						<br />

						<span class="is-size-5 pl-5">•</span>
						Libravatar ( Avatar Provider )
						<br />
					</p>
				</details>
			</div>
		</div>
	</div>
</section>
