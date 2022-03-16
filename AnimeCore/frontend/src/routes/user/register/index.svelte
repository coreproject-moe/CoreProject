<script lang="ts">
    import { fade } from "svelte/transition";

    import * as yup from "yup";
    import { createForm } from "felte";
    import tippy, { animateFill, sticky, type Instance } from "tippy.js";

    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";

    import { goto } from "$app/navigation";
    import { registerEndpoint } from "$urls/restEndpoints";
    
    import { responsiveMode } from "$store/responsive";
    import { isUserAuthenticated } from "$store/users";

    import { trapFocus } from "$lib/functions/trapFocus";
    import { projectName } from "$lib/constants/frontend/project";

    let avatarSrc = "";
    let passwordShown = false;
    let avatarShown: boolean;

    let parentElement: HTMLElement;
    // Tippyjs Declarations
    let avatarElement: HTMLElement & { _tippy?: Instance };

    let tippyJsFirstNameIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsLastNameIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsUserNameIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsEmailIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsPasswordIcon: HTMLElement & { _tippy?: Instance };
    let tippyJsConfirmPasswordIcon: HTMLElement & { _tippy?: Instance };

    // Desktop only declaration
    $: {
        if (
            $responsiveMode === "desktop" ||
            $responsiveMode === "widescreen" ||
            $responsiveMode === "fullhd"
        ) {
            tippyJsFirstNameIcon?._tippy?.show();
            tippyJsLastNameIcon?._tippy?.show();
            tippyJsUserNameIcon?._tippy?.show();
            tippyJsEmailIcon?._tippy?.show();
            tippyJsPasswordIcon?._tippy?.show();
            tippyJsConfirmPasswordIcon?._tippy?.show();
        } else {
            // Cleanup
            tippyJsFirstNameIcon?._tippy?.hide();
            tippyJsLastNameIcon?._tippy?.hide();
            tippyJsUserNameIcon?._tippy?.hide();
            tippyJsEmailIcon?._tippy?.hide();
            tippyJsPasswordIcon?._tippy?.hide();
            tippyJsConfirmPasswordIcon?._tippy?.hide();
        }
    }

    const SUPPORTED_FORMATS = ["image/jpg", "image/jpeg", "image/gif", "image/png"];

    const schema = yup.object({
        first_name: yup
            ?.string()
            ?.required("Did you type your <b>First Name</b> ? 🤔")
            ?.max(20, "<b>First Name</b> must be less than <b>20 Characters</b>"),
        last_name: yup
            ?.string()
            ?.required("Did you type your <b>Last Name</b> ? 🤔")
            ?.max(20, "<b>Last Name</b> must be less than <b>20 Characters</b>"),
        username: yup
            ?.string()
            ?.required("Did you type your <b>Username</b> ? 🤔")
            ?.min(0)
            ?.max(50, "<b>User Name</b> must be less than <b>50 Characters</b>"),
        email: yup
            ?.string()
            ?.email(
                `
                <b>Email</b> must be valid.
                <br/>
                For example : <b>SomeOne@example.com</b>`
            )
            ?.required("Did you type your <b>Email</b> ? 🤔")
            ?.test(
                "email",
                `Did you actually use <b>SomeOne@example.com</b> as your email?`,
                async (value) => {
                    return value === "SomeOne@example.com" ? false : true;
                }
            ),
        password: yup
            ?.string()
            ?.required("How can <b>one</b> create <b>ones</b> account without <b>Password</b> ? 🤔")
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
            const data = new FormData();

            data.append("first_name", values?.first_name as string);
            data.append("last_name", values?.last_name as string);
            data.append("username", values?.username);
            data.append("email", values?.email);
            data.append("avatar", values?.avatar ?? new File([], ""));

            if (
                values?.password === values?.confirm_password && // Why are you not same ?
                values?.password !== "" && // Must not be empty. Will cause a massacare at backend
                values?.password !== "Ex@mple1234" // Are you joking ? How did you escape Yup ?
            ) {
                data.append("password", values?.password);
            } else {
                console.error(`Mom bring the gun. We need to find and eliminate this guy`);
                return;
            }

            try {
                await fetch(registerEndpoint, {
                    method: "POST",
                    body: data
                }).then(async (res) => {
                    if (res?.ok) {
                        goto("/user/login");
                    }
                });
            } catch (err) {
                if (err instanceof Error) {
                    console.error(`Cannot POST data to ${registerEndpoint} | Reason ${err}`);
                }
            }
        }
    });

    const handleImageInput = (e: Event) => {
        const target = e?.target as HTMLInputElement;
        const file = target.files instanceof FileList ? target.files[0] : null;

        if (file) {
            const reader = new FileReader();
            reader.onload = function () {
                avatarShown = false;
                let dataURL = reader.result as string;

                // If datasrc and avatarsrc is not same only then destroy the ref.
                // Else it will cause a werid error, which will destroy the tippy element
                // if you upload the same image twice
                if (dataURL !== avatarSrc) {
                    avatarElement?._tippy?.destroy();
                }

                avatarSrc = dataURL;

                // Setting timeout is the best way to remount.
                // Please don't change this logic.
                // This will only make it harder

                setTimeout(() => {
                    avatarShown = true;
                }, 10);
            };
            reader.readAsDataURL(file);
        }
    };
    $: {
        if (avatarElement) {
            tippy(avatarElement, {
                content: avatarSrc === "" ? "Wow such empty 😺" : "Wow nice pic ! 😻",
                theme: "black",
                placement: "bottom",
                showOnCreate: true,
                sticky: true,
                interactive: true,
                hideOnClick: false,
                trigger: "manual",
                appendTo: () => parentElement,
                plugins: [sticky]
            });
        }
    }
</script>

<svelte:head>
    <title>Register Page | {projectName}</title>
</svelte:head>

{#if $isUserAuthenticated}
    <div transition:fade>
        <p class="has-text-white has-text-centered">How can a man be registered twice ? 🤔</p>
        <p class="has-text-white has-text-centered">Thats a question for the wise. 🧙‍♂️</p>
    </div>
{:else}
    <form use:form use:trapFocus transition:fade bind:this={parentElement}>
        <div class="is-flex is-justify-content-center has-text-white is-size-5 has-text-centered">
            <p>↓&nbsp; Avatar &nbsp;↓</p>
        </div>
        <div class="columns is-mobile is-centered pb-5 pt-3">
            <div class="column is-narrow">
                <figure class="image is-96x96" bind:this={avatarElement}>
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
                            <img src="/placeholder-96x96.avif" class="is-rounded preview" alt="" />
                        </div>
                    {:else}
                        <div
                            class="progressive replace"
                            style="border-radius: 9999px; height: 96px; margin: auto; cursor: default;border:2px solid white"
                        />
                    {/if}
                </figure>
            </div>
        </div>
        <div class="field is-horizontal py-1">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            name="first_name"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="First Name"
                        />
                        <span
                            class="icon is-small is-left"
                            bind:this={tippyJsFirstNameIcon}
                            use:tippy={{
                                content: "First Name",
                                hideOnClick: false,
                                theme: "black",
                                placement: "left",
                                animateFill: true,
                                trigger: "manual",
                                showOnCreate: true,
                                sticky: true,
                                plugins: [animateFill, sticky]
                            }}
                        >
                            <img
                                alt=""
                                class="is-size-7"
                                style="transform: scale(0.8)"
                                src="/svg/character_a.svg"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="field is-horizontal py-1">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            name="last_name"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Last Name"
                        />
                        <span
                            class="icon is-small is-left"
                            bind:this={tippyJsLastNameIcon}
                            use:tippy={{
                                content: "Last Name",
                                hideOnClick: false,
                                theme: "black",
                                placement: "left",
                                animateFill: true,
                                trigger: "manual",
                                showOnCreate: true,
                                sticky: true,
                                plugins: [animateFill, sticky]
                            }}
                        >
                            <img
                                alt=""
                                class="is-size-7"
                                style="transform: scale(0.8)"
                                src="/svg/character_z.svg"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="field is-horizontal py-1">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            name="username"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Username"
                        />
                        <span
                            class="icon is-small is-left"
                            bind:this={tippyJsUserNameIcon}
                            use:tippy={{
                                content: "Username",
                                hideOnClick: false,
                                theme: "black",
                                placement: "left",
                                animateFill: true,
                                trigger: "manual",
                                showOnCreate: true,
                                sticky: true,
                                plugins: [animateFill, sticky]
                            }}
                        >
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
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="email"
                            name="email"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Email"
                        />
                        <span
                            class="icon is-small is-left"
                            bind:this={tippyJsEmailIcon}
                            use:tippy={{
                                content: "Email",
                                hideOnClick: false,
                                theme: "black",
                                placement: "left",
                                animateFill: true,
                                trigger: "manual",
                                showOnCreate: true,
                                sticky: true,
                                plugins: [animateFill, sticky]
                            }}
                        >
                            <ion-icon class="is-size-4 has-text-white" name="mail-outline" />
                        </span>
                    </p>
                </div>
            </div>
        </div>

        <div class="field is-horizontal py-1">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left has-icons-right">
                        <input
                            type={passwordShown ? "text" : "password"}
                            name="password"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
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
                        <span
                            class="icon is-small is-left"
                            bind:this={tippyJsPasswordIcon}
                            use:tippy={{
                                content: "Password",
                                hideOnClick: false,
                                theme: "black",
                                placement: "left",
                                animateFill: true,
                                trigger: "manual",
                                showOnCreate: true,
                                sticky: true,
                                plugins: [animateFill, sticky]
                            }}
                        >
                            <ion-icon class="is-size-4 has-text-white" name="lock-closed-outline" />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="field is-horizontal py-1">
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="password"
                            name="confirm_password"
                            class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                            placeholder="Confirm Password"
                            autocomplete="new-password"
                        />
                        <span
                            class="icon is-small is-left"
                            bind:this={tippyJsConfirmPasswordIcon}
                            use:tippy={{
                                content: "Confirm Password",
                                hideOnClick: false,
                                theme: "black",
                                placement: "left",
                                animateFill: true,
                                trigger: "manual",
                                showOnCreate: true,
                                sticky: true,
                                plugins: [animateFill, sticky]
                            }}
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

        <div class="columns is-mobile is-centered pt-3">
            <div class="column is-narrow">
                <button
                    type="submit"
                    class="button is-rounded is-centered has-text-white has-border-gray is-black"
                    >Register</button
                >
            </div>
        </div>
    </form>
{/if}
