<script lang="ts">
    import { onMount } from "svelte";

    // @ts-ignore
    import Typewriter from "typewriter-effect/dist/core";

    onMount(() => {
        var app = document.getElementById('typing_text');

        var typewriter = new Typewriter(app, {
            loop: true,
            delay: 75,
        });

        typewriter
            .typeString('For watching <b class="text-primary">Animes.</b>')
            .pauseFor(2000)
            .deleteChars(16)
            .typeString('reading <b class="text-warning">Mangas.</b>')
            .pauseFor(2000)
            .deleteChars(15)
            .typeString('listening to <b class="text-accent">Musics.</b>')
            .pauseFor(2000)
            .deleteAll()
            .typeString('Welcome to <b class="text-accent">CoreProject.</b>')
            .pauseFor(5000)
            .start();
    });
</script>

<main class="w-screen h-screen bg-secondary pt-[5vw] flex justify-center">
    <div class="flex flex-col text-center light-animate leading-none gap-[1.5vw]">
        <h2 class="light-animate text-[5vw] font-bold">Imagine a new platform.</h2>
        <p class="text-[2.75vw] text-neutral-content/75" id="typing_text"></p>
    </div>
</main>

<style lang="scss">
@keyframes lights {
  0% {
    color: hsl(230, 40%, 80%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.2),
      0 0 0.125em hsla(320, 100%, 60%, 0.3),
      -1em -0.125em 0.5em hsla(40, 100%, 60%, 0),
      1em 0.125em 0.5em hsla(200, 100%, 60%, 0);
  }
  
  30% { 
    color: hsl(230, 80%, 90%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.5),
      0 0 0.125em hsla(320, 100%, 60%, 0.5),
      -0.5em -0.125em 0.25em hsla(40, 100%, 60%, 0.2),
      0.5em 0.125em 0.25em hsla(200, 100%, 60%, 0.4);
  }
  
  40% { 
    color: hsl(230, 100%, 95%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.5),
      0 0 0.125em hsla(320, 100%, 90%, 0.5),
      -0.25em -0.125em 0.125em hsla(40, 100%, 60%, 0.2),
      0.25em 0.125em 0.125em hsla(200, 100%, 60%, 0.4);
  }
  
  70% {
    color: hsl(230, 80%, 90%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.5),
      0 0 0.125em hsla(320, 100%, 60%, 0.5),
      0.5em -0.125em 0.25em hsla(40, 100%, 60%, 0.2),
      -0.5em 0.125em 0.25em hsla(200, 100%, 60%, 0.4);
  }
  
  100% {
    color: hsl(230, 40%, 80%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.2),
      0 0 0.125em hsla(320, 100%, 60%, 0.3),
      1em -0.125em 0.5em hsla(40, 100%, 60%, 0),
      -1em 0.125em 0.5em hsla(200, 100%, 60%, 0);
  }
  
}

.light-animate {
  animation: lights 5s linear infinite;
}
</style>