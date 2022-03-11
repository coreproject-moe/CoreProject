<script lang="ts">
    // Main SCSS import
    import "../app.scss";

    // Import JS libraries
    import md5 from "md5";
    import dayjs from "dayjs";
    import anime from "animejs";
    import tippy, { sticky, type Instance } from "tippy.js";

    // Svelte Import
    import { onDestroy, onMount } from "svelte";

    // Responsive helper
    import { responsiveMode } from "$store/responsive";
    import { isUserAuthenticated, userInfo } from "$store/users";

    // Constants
    import { baseUrl } from "$urls/baseUrl";
    import { githubUrl } from "$lib/constants/frontend/project";

    import { page } from "$app/stores";
    import { browser } from "$app/env";
    import { goto } from "$app/navigation";

    let arrowButtonTurned: boolean;

    let navbarBurgerClosed = false;
    // Auto close the navbar Buger to close if its on Mobile or Tablet
    $: navbarBurgerClosed = $responsiveMode === "mobile" || $responsiveMode === "tablet";

    onMount(async () => {
        // https://bulma.io/documentation/components/navbar/#fixed-navbar
        const HTMLTAG = browser && document.getElementsByTagName("html")[0]; // '0' to assign the first (and only `HTML` tag)
        browser && HTMLTAG.classList.add("has-navbar-fixed-top");

        arrowButtonTurned = false;
    });

    onDestroy(async () => {
        // Cleanup
        tippyJsAvatar?._tippy?.destroy();
        animeJsGithubButton?._tippy?.destroy();
    });

    // AnimeJs Bindings
    let animeJsArrowBack: HTMLElement;
    let animejsArrowButton: HTMLElement;
    let animeJsGithubButton: HTMLElement & { _tippy?: Instance };
    // Icons
    let animeJsHomeIcon: HTMLElement;
    let animeJsRequestIcon: HTMLElement;
    let animeJsFaqIcon: HTMLElement;
    let animeJsGithubIcon: HTMLElement;

    $: {
        if (animeJsArrowBack) {
            anime({
                targets: [animeJsArrowBack],
                easing: "linear",
                duration: 100,
                color: "hsl(0, 0%, 80%)"
            });
        }
    }
    // TippyJS
    let tippyJsAvatar: HTMLElement & { _tippy?: Instance };

    $: {
        if (animeJsGithubButton) {
            tippy(animeJsGithubButton, {
                content: "Github",
                theme: "black",
                touch: false
            });
        }

        if (tippyJsAvatar && !tippyJsAvatar?._tippy) {
            tippy(tippyJsAvatar, {
                content: `<b>ID</b> : ${$userInfo?.id} <br /> <b>First Name</b> : ${
                    $userInfo?.first_name
                }<br/> <b>Last Name</b> : ${$userInfo?.last_name}<br/> <b>Username</b> : ${
                    $userInfo?.username
                }<br/> <b>Email</b> : ${$userInfo?.email}<br/><b>Date Joined</b> : ${dayjs(
                    $userInfo?.date_joined
                )?.format("MMMM D, YYYY - h:mm A")}<br/><b>Last Active</b> : ${dayjs(
                    $userInfo?.last_login
                )?.format("MMMM D, YYYY - h:mm A")}<br/>
                    <div class='pt-2'>
                        <a class='is-size-7 has-text-white has-background-black button is-ghost has-no-text-decoration is-rounded has-hover-gray' sveltekit:prefetch style='transition:0.2s' href="/user/edit_info">
                            <ion-icon class='pr-2 is-size-5' name="create-outline"></ion-icon>Edit Info
                        </a>
                        <a class='is-size-7 has-text-white has-background-black button is-ghost has-no-text-decoration is-rounded has-hover-gray' style='transition:0.2s; float:right' sveltekit:prefetch href="/user/logout?next=${
                            $page?.url?.pathname
                        }">
                            <ion-icon class='pr-2 is-size-5' name="log-out-outline"></ion-icon>Log Out
                        </a>
                    </div>
                    <br/>`,
                theme: "black",
                trigger: "click",
                allowHTML: true,
                interactive: true,
                sticky: true,
                placement: "bottom",
                plugins: [sticky],
                appendTo: () => browser && document.body
            });
        }
    }
</script>

<nav
    class="navbar is-clipped has-background-black is-fixed-top {$responsiveMode === 'widescreen'
        ? ''
        : 'container'}"
    style="z-index:100;"
>
    <div class="navbar-brand is-clipped">
        <a class="navbar-item is-clickable" href="https://bulma.io">
            <img src="/logo.avif" alt="logo" width={112} height={28} />
        </a>

        <button
            class="navbar-burger has-text-white is-clickable {navbarBurgerClosed
                ? ''
                : 'is-active'}"
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

    <div class="navbar-menu has-background-black {navbarBurgerClosed ? '' : 'is-active'}">
        <div
            class="navbar-start mt-3 {$responsiveMode === 'mobile' || $responsiveMode === 'tablet'
                ? 'is-flex is-flex-direction-row is-justify-content-center'
                : ''}"
        >
            <a
                href="/anime"
                sveltekit:prefetch
                class="navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration {$responsiveMode ===
                    'mobile' || $responsiveMode === 'tablet'
                    ? 'pl-2 pr-2'
                    : 'ml-2'} {$page.url.pathname === '/anime' ? 'hover' : ''}
					"
                on:mouseenter|preventDefault={async () => {
                    anime({
                        targets: [animeJsHomeIcon],
                        color: "#e50000"
                    });
                }}
                on:mouseleave|preventDefault={async () => {
                    anime({
                        targets: [animeJsHomeIcon],
                        color: "#d9d9d9"
                    });
                }}
            >
                <ion-icon name="home-sharp" bind:this={animeJsHomeIcon} />
                <p
                    class="{$responsiveMode === 'mobile' || $responsiveMode === 'tablet'
                        ? 'pt-2 nav-icon-button'
                        : ''} {$responsiveMode === 'widescreen' ? 'is-size-7' : ''}"
                >
                    <span class="is-hidden-touch">&nbsp;</span> Home
                </p>
            </a>
            <a
                href="#"
                class="navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration {$responsiveMode ===
                    'mobile' || $responsiveMode === 'tablet'
                    ? 'pl-2 pr-2'
                    : 'ml-2'}"
                on:mouseenter|preventDefault={async () => {
                    anime({
                        targets: [animeJsRequestIcon],
                        color: "#e50000"
                    });
                }}
                on:mouseleave|preventDefault={async () => {
                    anime({
                        targets: [animeJsRequestIcon],
                        color: "#d9d9d9"
                    });
                }}
            >
                <ion-icon
                    name="cloud-upload-outline"
                    class="is-size-5"
                    bind:this={animeJsRequestIcon}
                />
                <p
                    class="{$responsiveMode === 'mobile' || $responsiveMode === 'tablet'
                        ? 'pt-2 nav-icon-button'
                        : ''} {$responsiveMode === 'widescreen' ? 'is-size-7' : ''}"
                >
                    <span class="is-hidden-touch">&nbsp;</span>
                    Request
                </p>
            </a>

            <a
                sveltekit:prefetch
                href="/faq"
                class="navbar-item button is-ghost is-rounded is-unselectable has-text-white has-background-black has-no-text-decoration {$responsiveMode ===
                    'mobile' || $responsiveMode === 'tablet'
                    ? 'pl-2 pr-2'
                    : 'ml-2'} {$page.url.pathname.includes('faq') ? 'hover' : ''}"
                on:mouseenter|preventDefault={async () => {
                    anime({
                        targets: [animeJsFaqIcon],
                        color: "#e50000"
                    });
                }}
                on:mouseleave|preventDefault={async () => {
                    anime({
                        targets: [animeJsFaqIcon],
                        color: "#d9d9d9"
                    });
                }}
            >
                <ion-icon name="help-circle-outline" class="is-size-5" bind:this={animeJsFaqIcon} />
                <p
                    class="{$responsiveMode === 'mobile' || $responsiveMode === 'tablet'
                        ? 'pt-2 nav-icon-button'
                        : ''} {$responsiveMode === 'widescreen' ? 'is-size-7' : ''}"
                >
                    <span class="is-hidden-touch">&nbsp;</span>
                    FAQ
                </p>
            </a>
        </div>
        <div class="control has-icons-left mt-4 is-hidden-touch">
            <input
                class="input has-background-black has-text-white search__input"
                type="text"
                placeholder="Search Away"
            />
            <span class="icon is-small is-left">
                <ion-icon name="search-outline" class="has-text-white is-size-4" />
            </span>
        </div>
        <div class="navbar-end is-clipped">
            <div
                class="navbar-item {$responsiveMode === 'mobile'
                    ? 'is-flex is-flex-direction-row is-justify-content-center pt-6'
                    : ''}"
            >
                <button
                    class="is-rounded is-dark has-background-black-bis is-clickable {$responsiveMode ===
                        'mobile' || $responsiveMode === 'tablet'
                        ? 'is-hidden '
                        : ''}"
                    bind:this={animeJsGithubButton}
                    style="transform:translateX(40px);scale(0.1);"
                    on:mouseenter|preventDefault={async () => {
                        anime({
                            targets: [animeJsGithubIcon],
                            color: "hsl(0, 0%, 100%)"
                        });
                        anime({
                            targets: [animeJsGithubButton],
                            scale: 1.3
                        });
                    }}
                    on:mouseleave|preventDefault={async () => {
                        anime({
                            targets: [animeJsGithubIcon],
                            color: "hsl(0, 0%, 80%)"
                        });
                        anime({
                            targets: [animeJsGithubButton],
                            scale: 1
                        });
                    }}
                    on:click|preventDefault={async () => {
                        goto(githubUrl);
                    }}
                >
                    <ion-icon
                        class="has-text-white"
                        bind:this={animeJsGithubIcon}
                        style="width: 100%; height: 100%;"
                        name="logo-github"
                    />
                </button>

                <button
                    style="z-index: 1000000"
                    class="is-rounded is-dark has-background-black-bis is-clickable {$responsiveMode ===
                        'mobile' || $responsiveMode === 'tablet'
                        ? 'is-hidden'
                        : ''}"
                    bind:this={animejsArrowButton}
                    on:mouseenter|preventDefault={async () => {
                        anime({
                            targets: [animeJsArrowBack],
                            color: "#e50000"
                        });
                        anime({
                            targets: [animejsArrowButton],
                            scale: 1.2
                        });
                    }}
                    on:mouseleave|preventDefault={async () => {
                        anime({
                            targets: [animeJsArrowBack],
                            color: "hsl(0, 0%, 80%)"
                        });
                        anime({
                            targets: [animejsArrowButton],
                            scale: 1
                        });
                    }}
                    on:click|preventDefault={async () => {
                        arrowButtonTurned = !arrowButtonTurned;

                        switch (arrowButtonTurned) {
                            case true: {
                                anime({
                                    targets: [animeJsArrowBack],
                                    rotate: [0, 180]
                                });
                                anime({
                                    targets: [animeJsGithubButton],
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
                                    targets: [animeJsArrowBack],
                                    rotate: [180, 360]
                                });
                                anime({
                                    targets: [animeJsGithubButton],
                                    translateX: 40,
                                    easing: "easeOutSine",
                                    duration: 50,
                                    opacity: 0,
                                    scale: 0.2
                                });
                                break;
                            }
                        }
                    }}
                >
                    <ion-icon
                        bind:this={animeJsArrowBack}
                        name="arrow-back-outline"
                        style="width: 100%; height: 100%;"
                    />
                </button>
            </div>
            <!-- Username is the most unique thing to listen to -->
            {#if $isUserAuthenticated && $userInfo?.username}
                <div class="columns is-mobile is-centered">
                    <div class="column is-narrow">
                        <figure class="image is-48x48 pt-2 pl-2">
                            <!--
                                Please dont change this if else statement  
                                Because the store state will change as we are doing lazy fetching.
                                To reflect that change, we need to do optimistic update,
                                which this if else statement is doing down.
                            -->
                            {#if $userInfo.avatar}
                                <div
                                    bind:this={tippyJsAvatar}
                                    data-href={`${baseUrl}${$userInfo?.avatar}`}
                                    class="progressive replace"
                                    style="border-radius: 9999px; height:40px; width:40px; z-index: 1000000;margin: auto;"
                                >
                                    <img
                                        class="is-rounded preview"
                                        alt={$userInfo?.username}
                                        src="/placeholder-64x64.avif"
                                    />
                                </div>
                            {:else}
                                <div
                                    data-href={`https://seccdn.libravatar.org/avatar/${md5(
                                        $userInfo?.email ?? ""
                                    )}/?s=64`}
                                    bind:this={tippyJsAvatar}
                                    class="progressive replace"
                                    style="border-radius: 9999px; height:40px; width:40px; z-index: 1000000;margin: auto;"
                                >
                                    <img
                                        class="is-rounded preview"
                                        alt={$userInfo?.username}
                                        src="/placeholder-64x64.avif"
                                    />
                                </div>
                            {/if}
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
                                    sveltekit:prefetch
                                    href="/user/login?next={$page?.url?.pathname}"
                                >
                                    Log in
                                </a>
                                <a
                                    class="button has-text-white is-black has-border-gray is-rounded"
                                    sveltekit:prefetch
                                    href="/user/register"
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
            }
        }
    }
</style>
