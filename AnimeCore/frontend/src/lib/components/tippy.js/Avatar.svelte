<script lang="ts">
    export let nextPage = "";
    export let userInfo = {
        first_name: "",
        last_name: "",
        email: "",
        date_joined: "",
        username: "",
        id: 0,
        last_login: "",
        avatar: ""
    };

    import dayjs from "dayjs";
    import anime from "animejs";
    import tippy, { sticky, animateFill, type Instance } from "tippy.js";

    let animeJSEditInfoIcon: HTMLElement;
    let animeJSLogOutIcon: HTMLElement;

    let parentElement: HTMLElement;
    // TippyJS bindings
    let tippyIdElement: HTMLElement & { _tippy?: Instance };
    let tippyFirstNameElement: HTMLElement & { _tippy?: Instance };
    let tippyLastNameElement: HTMLElement & { _tippy?: Instance };
    let tippyUserNameElement: HTMLElement & { _tippy?: Instance };
    let tippyEmailElement: HTMLElement & { _tippy?: Instance };
    let tippyJsDateJoinedElement: HTMLElement & { _tippy?: Instance };
    let tippyJsLastLoginElement: HTMLElement & { _tippy?: Instance };

    $: {
        if (tippyIdElement) {
            tippy(tippyIdElement, {
                content: "<p class='is-size-7'>ID</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });
        }
        if (tippyFirstNameElement) {
            tippy(tippyFirstNameElement, {
                content: "<p class='is-size-7'>First Name</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left-start",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                maxWidth: 100,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });
            if (!userInfo?.first_name) {
                tippy(tippyFirstNameElement, {
                    content: "<p class='is-size-7'>Its a bird</p>",
                    allowHTML: true,
                    delay: 200,
                    theme: "black",
                    placement: "right-start",
                    offset: [-2, 12],
                    showOnCreate: true,
                    hideOnClick: false,
                    trigger: "manual",
                    zIndex: 1000000,
                    animateFill: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: () => parentElement
                });
            }
        }
        if (tippyLastNameElement) {
            tippy(tippyLastNameElement, {
                content: "<p class='is-size-7'>Last Name</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });

            if (!userInfo?.last_name) {
                tippy(tippyLastNameElement, {
                    content: "<p class='is-size-7'>Its a plane</p>",
                    allowHTML: true,
                    delay: 200,
                    theme: "black",
                    placement: "right-start",
                    offset: [-2, 12],
                    showOnCreate: true,
                    hideOnClick: false,
                    trigger: "manual",
                    zIndex: 1000000,
                    animateFill: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: () => parentElement
                });
            }
        }
        if (tippyUserNameElement) {
            tippy(tippyUserNameElement, {
                content: "<p class='is-size-7'>Username</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });
        }
        if (tippyEmailElement) {
            tippy(tippyEmailElement, {
                content: "<p class='is-size-7'>Email</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });
        }
        if (tippyJsDateJoinedElement) {
            tippy(tippyJsDateJoinedElement, {
                content: "<p class='is-size-7'>Date Joined</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });
        }
        if (tippyJsLastLoginElement) {
            tippy(tippyJsLastLoginElement, {
                content: "<p class='is-size-7'>Last Login</p>",
                allowHTML: true,
                delay: 100,
                theme: "black",
                placement: "left",
                showOnCreate: true,
                hideOnClick: false,
                trigger: "manual",
                zIndex: 1000000,
                animateFill: true,
                sticky: true,
                plugins: [animateFill, sticky],
                appendTo: () => parentElement
            });
        }
    }
</script>

<div class="columns is-mobile is-flex-direction-column" bind:this={parentElement}>
    <div class="column pt-4">
        <p class="is-flex">
            <ion-icon name="id-card-outline" class="is-size-5 pr-1" bind:this={tippyIdElement} />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {userInfo?.id}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <p class="is-flex">
            <ion-icon
                name="information-circle-outline"
                class="is-size-5 pr-1"
                bind:this={tippyFirstNameElement}
            />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {userInfo?.first_name}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <p class="is-flex">
            <ion-icon
                name="information-circle-outline"
                class="is-size-5 pr-1"
                bind:this={tippyLastNameElement}
            />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {userInfo?.last_name}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <p class="is-flex">
            <ion-icon
                name="person-circle-outline"
                class="is-size-5 pr-1"
                bind:this={tippyUserNameElement}
            />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {userInfo?.username}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <p class="is-flex">
            <ion-icon name="mail-outline" class="is-size-5 pr-1" bind:this={tippyEmailElement} />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {userInfo?.email}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <p class="is-flex">
            <ion-icon
                name="calendar-outline"
                class="is-size-5 pr-1"
                bind:this={tippyJsDateJoinedElement}
            />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {dayjs(userInfo?.date_joined)?.format("MMMM D, YYYY - h:mm A")}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <p class="is-flex">
            <ion-icon
                name="today-outline"
                class="is-size-5 pr-1"
                bind:this={tippyJsLastLoginElement}
            />
            :
            <span class="is-size-7 is-flex is-align-items-center pl-2">
                {dayjs(userInfo?.last_login)?.format("MMMM D, YYYY - h:mm A")}
            </span>
        </p>
    </div>
    <div class="column pt-1">
        <!-- Main container -->
        <nav class="level is-mobile">
            <!-- Left side -->
            <div class="level-left">
                <a
                    sveltekit:prefetch
                    class="is-size-7 has-text-white has-background-black button is-ghost has-no-text-decoration is-rounded has-hover-gray"
                    href="/user/edit_info"
                    on:mouseenter|preventDefault={async () => {
                        anime({
                            targets: [animeJSEditInfoIcon],
                            color: "#e50000"
                        });
                    }}
                    on:mouseleave|preventDefault={async () => {
                        anime({
                            targets: [animeJSEditInfoIcon],
                            color: "#d9d9d9"
                        });
                    }}
                >
                    <ion-icon
                        class="pr-2 is-size-5"
                        name="create-outline"
                        bind:this={animeJSEditInfoIcon}
                    />
                    Edit Info
                </a>
            </div>

            <!-- Right side -->
            <div class="level-right">
                <a
                    sveltekit:prefetch
                    class="is-size-7 has-text-white has-background-black button is-ghost has-no-text-decoration is-rounded has-hover-gray"
                    href="/user/logout?next=${nextPage}"
                    on:mouseenter|preventDefault={async () => {
                        anime({
                            targets: [animeJSLogOutIcon],
                            color: "#e50000"
                        });
                    }}
                    on:mouseleave|preventDefault={async () => {
                        anime({
                            targets: [animeJSLogOutIcon],
                            color: "#d9d9d9"
                        });
                    }}
                >
                    <ion-icon
                        class="pr-2 is-size-5"
                        name="log-out-outline"
                        bind:this={animeJSLogOutIcon}
                    />
                    Log Out
                </a>
            </div>
        </nav>
    </div>
</div>
