<script>
    import anime from "animejs";
</script>

<div
    class="card"
    on:mouseenter|preventDefault={(event) => {
        anime({
            targets: [event?.currentTarget],
            scale: 1.1,
            easing: "easeInSine",
            duration: 200
        });
    }}
    on:mouseleave|preventDefault={(event) => {
        anime({
            targets: [event?.currentTarget],
            scale: 1,
            easing: "easeOutSine",
            duration: 200
        });
    }}
>
    <div class="card-image has-background-black">
        <figure class="image is-3by5">
            <img
                src="https://cdn.myanimelist.net/images/anime/6/73245.jpg"
                alt="Placeholder_image"
                style="border-radius:20px"
            />
        </figure>
    </div>
    <div class="card-content has-background-black">
        <div class="content">
            <p class="subtitle has-text-white mb-0">
                <span class="is-size-7">
                    <ion-icon
                        class="is-size-5"
                        style="color: firebrick; transform: translateY(5px);"
                        name="tv-outline"
                    />
                </span>
                <span class="is-size-5">∞</span>
                <span class="is-size-7">
                    <ion-icon
                        class="is-size-5"
                        style="color: yellow; transform: translateY(5px);"
                        name="star-outline"
                    />
                </span>
                <span class="is-size-5">∞</span>
            </p>
        </div>
    </div>
</div>
