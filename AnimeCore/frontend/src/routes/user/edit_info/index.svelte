<script lang="ts">
    import dayjs from "dayjs";
    import * as yup from "yup";
    import { Md5 } from "ts-md5/dist/md5";

    import { createForm } from "felte";
    import { fade } from "svelte/transition";
    import tippy, { animateFill, sticky, type Instance } from "tippy.js";

    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";

    import { page } from "$app/stores";
    import { goto } from "$app/navigation";

    import { trapFocus } from "$lib/functions/trapFocus";
    import { projectName } from "$lib/constants/frontend/project";

    import { userInfoUrl } from "$urls/restEndpoints";

    import { responsiveMode } from "$store/responsive";
    import { isUserAuthenticated, userInfo, userToken } from "$store/users";
    $: {
        if ($userInfo?.avatar) {
            avatarShown = false;
            avatarSrc = `${$userInfo?.avatar}`;
            avatarShown = true;

            // Set a timeout because the element is not initialized
            setTimeout(async () => {
                avatarElementIcon?._tippy?.show();
            }, 100);
        } else if ($userInfo?.email) {
            avatarShown = false;
            avatarSrc = `https://seccdn.libravatar.org/avatar/${Md5.hashStr(
                $userInfo?.email ?? ""
            )}/?s=64`;
            avatarShown = true;
        }
    }
    let passwordShown = false;
    let imageCleared = false;
    let avatarShown: boolean;
    let avatarSrc = "";

    let parentElement: HTMLElement;
    // TippyJs icon declarations
    let avatarElementIcon: HTMLElement & { _tippy?: Instance };
    // Icons
    let tippyJsFirstNameIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsLastNameIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsUserNameIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsEmailIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsPasswordIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsConfirmPasswordIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsDateJoinedIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsLastLoginIcon: HTMLElement & { _tippy?: Instance };

    // Tippyjs Declarations
    $: {
        if (avatarElementIcon) {
            tippy(avatarElementIcon, {
                content() {
                    const element = document.createElement("p");
                    element.innerText = "Clear Image";
                    element.classList.add("is-clickable", "has-text-white");
                    element.addEventListener("click", async () => {
                        // Set this to true because we want to bind this to ensure we can clear backend image too.
                        imageCleared = true;

                        avatarShown = false;
                        avatarElementIcon?._tippy?.hide();
                        avatarSrc = `https://seccdn.libravatar.org/avatar/${Md5.hashStr(
                            $userInfo?.email ?? ""
                        )}/?s=64`;

                        // Setting timeout is the best way to remount.
                        // Please don't change this logic.
                        // This will only make it harder

                        setTimeout(async () => {
                            avatarShown = true;
                        }, 10);
                    });
                    return element;
                },
                placement: "bottom",
                theme: "black",
                allowHTML: true,
                sticky: true,
                interactive: true,
                hideOnClick: false,
                trigger: "manual",
                plugins: [sticky],
                appendTo: parentElement
            });
        }
    }

    // Desktop only declaration
    $: {
        if (
            $responsiveMode === "desktop" ||
            $responsiveMode === "widescreen" ||
            $responsiveMode === "fullhd"
        ) {
            if (tippyJsFirstNameIcon) {
                tippy(tippyJsFirstNameIcon, {
                    content: "<p class='is-size-7'>First Name</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "left",
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsLastNameIcon) {
                tippy(tippyJsLastNameIcon, {
                    content: "<p class='is-size-7'>Last Name</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "left",
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsUserNameIcon) {
                tippy(tippyJsUserNameIcon, {
                    content: "<p class='is-size-7'>Username</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "left",
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsEmailIcon) {
                tippy(tippyJsEmailIcon, {
                    content: "<p class='is-size-7'>Email</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "left",
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsPasswordIcon) {
                tippy(tippyJsPasswordIcon, {
                    content: "<p class='is-size-7'>Password</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "left",
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsConfirmPasswordIcon) {
                tippy(tippyJsConfirmPasswordIcon, {
                    content: "<p class='is-size-7'>Confirm Password</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "left",
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsDateJoinedIcon) {
                tippy(tippyJsDateJoinedIcon, {
                    content: "<p class='is-size-7'>Date joined</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "top",
                    offset: [0, -10],
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
            if (tippyJsLastLoginIcon) {
                tippy(tippyJsLastLoginIcon, {
                    content: "<p class='is-size-7'>Last Login</p>",
                    allowHTML: true,
                    hideOnClick: false,
                    theme: "black",
                    placement: "top",
                    offset: [0, -10],
                    animateFill: true,
                    trigger: "manual",
                    showOnCreate: true,
                    sticky: true,
                    plugins: [animateFill, sticky],
                    appendTo: parentElement
                });
            }
        } else {
            tippyJsFirstNameIcon?._tippy?.destroy();
            tippyJsLastNameIcon?._tippy?.destroy();
            tippyJsUserNameIcon?._tippy?.destroy();
            tippyJsEmailIcon?._tippy?.destroy();
            tippyJsPasswordIcon?._tippy?.destroy();
            tippyJsConfirmPasswordIcon?._tippy?.destroy();
            tippyJsDateJoinedIcon?._tippy?.destroy();
            tippyJsLastLoginIcon?._tippy?.destroy();
        }
    }

    const SUPPORTED_FORMATS = ["image/jpg", "image/jpeg", "image/gif", "image/png"];

    const schema = yup.object({
        first_name: yup
            ?.string()
            ?.max(20, "<b>First Name</b> must be less than <b>20 Characters</b>"),
        last_name: yup
            ?.string()
            ?.max(20, "<b>Last Name</b> must be less than <b>20 Characters</b>"),
        username: yup
            ?.string()
            ?.min(0)
            ?.max(50, "<b>User Name</b> must be less than <b>50 Characters</b>"),
        password: yup
            ?.string()
            ?.notRequired()
            ?.test(
                "password",
                `<b>Password</b> must contain at least <b>8 Characters</b> with the following <b>attributes</b> :
                <br/>
                <br/>
                <ul>
                    <li>1 Uppercase <i>( eg : ABCD )</i></li>
                    <li>1 Lowercase <i>( eg : abcd )</i></li>
                    <li>1 Number <i>( eg : 1234 )</i></li>
                    <li>1 Special Character <i>( eg : @%^& )</i></li>
                </ul>
                <br/>
                A valid password = <b>Ex@mple1234</b>`,
                async (value) => {
                    if (value && value?.length > 0) {
                        return /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(
                            value
                        );
                    }
                    return true;
                }
            )
            ?.notOneOf(["Ex@mple1234"], "Did you actually use <b>Ex@mple1234</b> as password ?")
            ?.max(1024, "<b>Password</b> must be less than <b>1024 Characters<b/>"),
        confirm_password: yup
            ?.string()
            ?.oneOf(
                [yup?.ref("password"), null],
                "<b>Password</b> and <b>Confirm Password</b> are not the same"
            ),

        avatar: yup
            ?.mixed()
            ?.notRequired()
            ?.test(
                "fileType",
                `Unsupported <b>File</b> format.
                <br/>
                <b>File</b> must be <b>one of the following</b> :
                <br/>
                <br/>
                <ul>
                    ${SUPPORTED_FORMATS?.map((items) => {
                        return `<li><b>${items}</b></li>`;
                    }).join(" ")}
                </ul>`,
                async (value: File) => {
                    if (value?.size > 0) {
                        return SUPPORTED_FORMATS?.includes(value?.type);
                    }
                    return true;
                }
            )
    });

    const { form } = createForm<yup.InferType<typeof schema>>({
        extend: [
            validator({ schema }),
            reporter({
                tippyProps: {
                    theme: "black",
                    allowHTML: true
                }
            })
        ],
        onSubmit: async (values) => {
            // Consider this the empty dictionary which will have promised values
            const data = new FormData();

            data.append("username", $userInfo?.username);
            if (values?.first_name) {
                data.append("first_name", values?.first_name);
            }
            if (values?.last_name) {
                data.append("last_name", values?.last_name);
            }
            if (values?.password && values?.confirm_password) {
                if (
                    values?.password === values?.confirm_password && // Why are you not same ?
                    values?.password !== "" && // Must not be empty. Will cause a massacare at backend
                    values?.password !== "Ex@mple1234" // Are you joking ? How did you escape Yup ?
                ) {
                    data.append("password", values?.password);
                }
            }
            if (values?.avatar) {
                const avatar = values?.avatar as File;
                data.append("avatar", avatar);
            } else {
                if (imageCleared) {
                    // Thanks random guy from stackoverflow
                    // https://stackoverflow.com/questions/48676365/how-can-i-clear-an-image-with-django-rest-framework
                    data.append("avatar", new File([], ""));
                    // Reset this value
                    imageCleared = false;
                }
            }

            try {
                await fetch(userInfoUrl, {
                    method: "POST",
                    headers: new Headers({
                        Authorization: `Bearer ${$userToken.access}`
                    }),
                    body: data
                }).then(async (res) => {
                    avatarShown = false;
                    userInfo.set(await res.json());
                    setTimeout(() => {
                        avatarShown = true;
                    }, 10);

                    if (data.get("password") || data.get("username") !== $userInfo?.username) {
                        goto(`/user/logout?next=${$page?.url?.pathname}&login_page=true`);
                    }
                });
            } catch (err) {
                if (err instanceof Error) {
                    console.error(`Cannot POST data to ${userInfoUrl} | Reason ${err}`);
                }
            }
        }
    });

    const handleImageInput = (e: Event) => {
        const target = e.target as HTMLInputElement;
        const file = target.files instanceof FileList ? target.files[0] : null;

        if (file) {
            const reader = new FileReader();
            reader.onload = function () {
                avatarShown = false;
                let dataURL = reader.result as string;
                avatarSrc = dataURL;

                // Setting timeout is the best way to remount.
                // Please don't change this logic.
                // This will only make it harder

                setTimeout(() => {
                    avatarShown = true;
                    avatarElementIcon?._tippy?.show();
                }, 10);
            };
            reader.readAsDataURL(file);
        }
    };
</script>

<svelte:head>
    <title>Editing info for {$userInfo?.username} | {projectName}</title>
</svelte:head>

{#if $isUserAuthenticated}
    <form use:form use:trapFocus transition:fade bind:this={parentElement}>
        <div class="box has-background-black">
            <div class="columns is-mobile is-centered">
                <div class="column is-narrow">
                    <div class="title is-size-4 has-text-white is-unselectable">
                        Hi there, {$userInfo?.username} 👋
                    </div>
                </div>
            </div>
            <div class="columns is-mobile is-centered">
                <div class="column is-narrow">
                    <figure class="image is-96x96" bind:this={avatarElementIcon}>
                        <input
                            type="file"
                            name="avatar"
                            class="file-input is-clickable"
                            placeholder="Upload avatar"
                            style="z-index:1000000;"
                            accept="image/*"
                            on:input={handleImageInput}
                        />
                        <!--
                            This is a value to forcefully remount the div programatically
                         -->
                        {#if avatarShown}
                            <div
                                data-href={avatarSrc}
                                class="progressive replace"
                                style="border-radius: 9999px; height: 96px; margin: auto; cursor: default;"
                            >
                                <img
                                    src="/placeholder-96x96.avif"
                                    class="is-rounded preview"
                                    alt=""
                                />
                            </div>
                        {/if}
                    </figure>
                </div>
            </div>

            <div
                class="columns is-mobile is-centered {avatarSrc?.includes(
                    'https://seccdn.libravatar.org'
                )
                    ? ''
                    : 'pt-5'}"
            >
                <div class="column is-narrow">
                    <div class="title is-size-6 has-text-white is-unselectable">
                        {#if avatarSrc?.includes("https://seccdn.libravatar.org")}
                            <p>Serving avatar from libravatar.</p>
                        {:else}
                            <p>Currently serving avatar locally</p>
                        {/if}
                    </div>
                </div>
            </div>

            <div class="field is-horizontal py-1">
                <div class="field-label is-normal is-hidden-desktop">
                    <div class="label has-text-white is-unselectable">First Name :</div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="text"
                                name="first_name"
                                value={$userInfo?.first_name}
                                class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                                placeholder="First Name"
                                autocomplete="off"
                            />
                            <span class="icon is-small is-left" bind:this={tippyJsFirstNameIcon}>
                                <ion-icon
                                    class="is-size-4 has-text-white"
                                    name="alert-circle-outline"
                                />
                            </span>
                        </p>
                    </div>
                </div>
            </div>

            <div class="field is-horizontal py-1">
                <div class="field-label is-normal is-hidden-desktop">
                    <div class="label has-text-white is-unselectable">Last Name :</div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="text"
                                name="last_name"
                                value={$userInfo?.last_name}
                                class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                                placeholder="Last Name"
                                autocomplete="off"
                            />
                            <span class="icon is-small is-left" bind:this={tippyJsLastNameIcon}>
                                <ion-icon
                                    class="is-size-4 has-text-white"
                                    name="alert-circle-outline"
                                />
                            </span>
                        </p>
                    </div>
                </div>
            </div>

            <div class="field is-horizontal py-1">
                <div class="field-label is-normal is-hidden-desktop">
                    <div class="label has-text-white is-unselectable">User Name :</div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="text"
                                name="username"
                                value={$userInfo?.username}
                                class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                                placeholder="Username"
                                autocomplete="off"
                            />
                            <span class="icon is-small is-left" bind:this={tippyJsUserNameIcon}>
                                <ion-icon
                                    class="is-size-4 has-text-white"
                                    name="person-circle-outline"
                                />
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal py-1">
                <div class="field-label is-normal is-hidden-desktop">
                    <div class="label has-text-white is-unselectable">Email :</div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="text"
                                value={$userInfo?.email}
                                class="input is-font-face-ubuntu is-unselectable has-text-white has-background-black has-border-gray"
                                placeholder="Email"
                                autocomplete="off"
                                disabled
                            />
                            <span class="icon is-small is-left" bind:this={tippyJsEmailIcon}>
                                <ion-icon class="is-size-4 has-text-white" name="mail-outline" />
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal py-1">
                <div class="field-label is-normal is-hidden-desktop">
                    <div class="label has-text-white is-unselectable">Password :</div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left has-icons-right">
                            <input
                                type={passwordShown ? "text" : "password"}
                                name="password"
                                class="input is-font-face-ubuntu is-unselectable has-text-white has-background-black has-border-gray"
                                placeholder="Password"
                                autocomplete="new-password"
                            />
                            <span
                                class="icon is-small is-right is-clickable is-unselectable"
                                on:click|preventDefault={() => {
                                    passwordShown = !passwordShown;
                                }}
                            >
                                👀
                            </span>
                            <span class="icon is-small is-left" bind:this={tippyJsPasswordIcon}>
                                <ion-icon
                                    class="is-size-4 has-text-white"
                                    name="document-outline"
                                />
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal py-1">
                <div class="field-label is-normal is-hidden-desktop">
                    <div class="label has-text-white is-unselectable">Confirm Password :</div>
                </div>
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="password"
                                name="confirm_password"
                                class="input is-font-face-ubuntu is-unselectable has-text-white has-background-black has-border-gray"
                                value=""
                                placeholder="Confirm Password"
                                autocomplete="new-password"
                            />
                            <span
                                class="icon is-small is-left"
                                bind:this={tippyJsConfirmPasswordIcon}
                            >
                                <ion-icon
                                    class="is-size-4 has-text-white"
                                    name="document-lock-outline"
                                />
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="field is-horizontal py-1">
                <div class="field-body">
                    <div class="field">
                        <div class="field-label is-normal is-hidden-desktop">
                            <div class="label has-text-white is-unselectable is-flex">
                                Date Joined :
                            </div>
                        </div>
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="text"
                                value={dayjs($userInfo?.date_joined)?.format(
                                    "MMMM D, YYYY - h:mm A"
                                )}
                                class="input is-static is-font-face-ubuntu is-unselectable has-text-white has-background-black"
                                placeholder="Date Joined"
                                readonly={true}
                                disabled={true}
                            />

                            <span
                                class="icon is-small is-left is-clickable"
                                bind:this={tippyJsDateJoinedIcon}
                            >
                                <ion-icon
                                    class="is-size-4 has-text-white"
                                    name="calendar-outline"
                                />
                            </span>
                        </p>
                    </div>
                    <div class="field">
                        <div class="field-label is-normal is-hidden-desktop">
                            <div class="label has-text-white is-unselectable is-flex">
                                Last Login :
                            </div>
                        </div>
                        <p class="control is-expanded has-icons-left">
                            <input
                                type="text"
                                value={dayjs($userInfo?.last_login)?.format(
                                    "MMMM D, YYYY - h:mm A"
                                )}
                                class="input is-static is-font-face-ubuntu is-unselectable has-text-white has-background-black"
                                placeholder="Date Joined"
                                readonly={true}
                                disabled={true}
                            />

                            <span
                                class="icon is-small is-left is-clickable"
                                bind:this={tippyJsLastLoginIcon}
                            >
                                <ion-icon class="is-size-4 has-text-white" name="today-outline" />
                            </span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="columns is-mobile is-centered pt-3">
                <div class="column is-narrow">
                    <button
                        type="submit"
                        class="button is-rounded is-centered has-text-white has-border-gray is-black"
                        >Submit</button
                    >
                </div>
            </div>
        </div>
    </form>
{:else}
    <div class="has-text-white" transition:fade>
        <p class="has-text-centered">
            How can one edit one's info without <a
                class="has-text-white is-underlined"
                href="/user/login?next={$page?.url?.pathname}">logging in?</a
            >
        </p>
    </div>
{/if}
