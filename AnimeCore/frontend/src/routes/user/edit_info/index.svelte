<script lang="ts">
    import tippy from "tippy.js";

    import { page } from "$app/stores";
    import { trapFocus } from "$lib/functions/trapFocus";
    import { isUserAuthenticated, userInfo } from "$store/users";

    import * as yup from "yup";
    import { createForm } from "felte";

    import { validator } from "@felte/validator-yup";
    import reporter from "@felte/reporter-tippy";
    import { browser } from "$app/env";
    import dayjs from "dayjs";

    let passwordShown = false;
    let dateJoined: HTMLElement;
    let lastLogin: HTMLElement;

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
            ?.min(8, "<b>Password</b> must be more than <b>8 Characters</b>")
            ?.matches(
                /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/,
                `<b>Password</b> must contain at least <b>8 Characters</b> with the following <b>attributes</b> :
                <br/>
                <br/>
                <ul>
                    <li>1 Uppercase ( eg : ABCD ) </li>
                    <li>1 Lowercase ( eg : abcd ) </li> 
                    <li>1 Number ( eg : 1234 ) </li>
                    <li>1 Special Character ( eg : @%^& ) </li>
                </ul>
                <br/>
                A valid password = <b>Ex@mple1234</b>`
            )
            ?.max(1024, "<b>Password</b> must be less than <b>1024 Characters<b/>"),
        avatar: yup
            ?.mixed()
            .test("fileType", "Unsupported File Format", (value) =>
                SUPPORTED_FORMATS.includes(value?.type)
            ),
        confirm_password: yup
            ?.string()
            ?.oneOf(
                [yup.ref("password"), null],
                "<b>Password</b> and <b>Confirm Password</b> are not the same"
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
        onSubmit: (values) => {
            console.log(values);
        }
        // ...
    });
    
    $: {
        if (browser) {
            if (dateJoined) {
                tippy(dateJoined, {
                    content: "Date joined",
                    placement: "top",
                    theme: "black"
                });
            }
            if (lastLogin) {
                tippy(lastLogin, {
                    content: "Last Login",
                    placement: "top",
                    theme: "black"
                });
            }
        }
    }
</script>

{#if $isUserAuthenticated}
    <form use:form use:trapFocus>
        <div class="box has-background-black">
            <div class="columns is-mobile is-centered">
                <div class="column is-narrow">
                    <div class="title is-size-4 has-text-white is-unselectable">
                        Hi there, baseplate-admin 👋
                    </div>
                </div>
            </div>
            <div class="columns is-mobile is-centered">
                <div class="column is-narrow">
                    <figure class="image is-96x96">
                        <input
                            type="file"
                            name="avatar"
                            class="file-input is-clickable"
                            placeholder="Upload avatar"
                            style="z-index:1000000;"
                            accept="image/*"
                        />

                        <a
                            href="/media/avatars/a41723bb-6921-451f-84e3-7694a7196dfe.avif"
                            class="progressive"
                            style="border-radius: 9999px; height: 96px; margin: auto; cursor: default;"
                        >
                            <img
                                src="http://127.0.0.1:8000/media/avatars/a41723bb-6921-451f-84e3-7694a7196dfe.avif"
                                class="is-rounded avatar-preview"
                                alt=""
                            />
                        </a>
                    </figure>
                </div>
            </div>

            <div class="columns is-mobile is-centered">
                <div class="column is-narrow">
                    <div class="subtitle is-size-7 has-text-white is-unselectable">
                        <input type="checkbox" name="clear_image" id="id_clear_image" />
                        <span class="pl-3"> Clear image </span>
                    </div>
                </div>
            </div>

            <div class="columns is-mobile is-centered">
                <div class="column is-narrow">
                    <div class="title is-size-6 has-text-white is-unselectable">
                        Currently serving avatar locally
                    </div>
                </div>
            </div>
        </div>

        <div class="items field is-horizontal py-1">
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
                        <span class="icon is-small is-left">
                            <ion-icon
                                class="is-size-4 has-text-white"
                                name="alert-circle-outline"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>

        <div class="items field is-horizontal py-1">
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
                        <span class="icon is-small is-left">
                            <ion-icon
                                class="is-size-4 has-text-white"
                                name="alert-circle-outline"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items field is-horizontal py-1">
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
                        <span class="icon is-small is-left">
                            <ion-icon
                                class="is-size-4 has-text-white"
                                name="person-circle-outline"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items field is-horizontal py-1">
            <div class="field-label is-normal is-hidden-desktop">
                <div class="label has-text-white is-unselectable">Email :</div>
            </div>
            <div class="field-body">
                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            value={$userInfo.email}
                            class="input is-font-face-ubuntu is-unselectable has-text-white has-background-black has-border-gray"
                            placeholder="Email"
                            autocomplete="off"
                            disabled
                        />
                        <span class="icon is-small is-left">
                            <ion-icon class="is-size-4 has-text-white" name="mail-outline" />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items field is-horizontal py-1">
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
                            on:click={() => {
                                passwordShown = !passwordShown;
                            }}
                        >
                            👀
                        </span>
                        <span class="icon is-small is-left">
                            <ion-icon class="is-size-4 has-text-white" name="document-outline" />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items field is-horizontal py-1">
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
                        <span class="icon is-small is-left">
                            <ion-icon
                                class="is-size-4 has-text-white"
                                name="document-lock-outline"
                            />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items field is-horizontal py-1">
            <div class="field-body">
                <div class="field">
                    <div class="field-label is-normal is-hidden-desktop">
                        <div class="label has-text-white is-unselectable">Date Joined :</div>
                    </div>
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            value={dayjs($userInfo?.date_joined).format("MMMM D, YYYY - h:mm A")}
                            class="input is-static is-font-face-ubuntu is-unselectable has-text-white has-background-black"
                            placeholder="Date Joined"
                            readonly={true}
                            disabled={true}
                        />

                        <span class="icon is-small is-left is-clickable" bind:this={dateJoined}>
                            <ion-icon class="is-size-4 has-text-white" name="calendar-outline" />
                        </span>
                    </p>
                </div>
                <div class="field">
                    <div class="field-label is-normal is-hidden-desktop">
                        <div class="label has-text-white is-unselectable">Last Login :</div>
                    </div>
                    <p class="control is-expanded has-icons-left">
                        <input
                            type="text"
                            value={dayjs($userInfo?.last_login).format("MMMM D, YYYY - h:mm A")}
                            class="input is-static is-font-face-ubuntu is-unselectable has-text-white has-background-black"
                            placeholder="Date Joined"
                            readonly={true}
                            disabled={true}
                        />

                        <span class="icon is-small is-left is-clickable" bind:this={lastLogin}>
                            <ion-icon class="is-size-4 has-text-white" name="today-outline" />
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="items columns is-mobile is-centered pt-3">
            <div class="column is-narrow">
                <button
                    type="submit"
                    class="button is-rounded is-centered has-text-white has-border-gray is-black"
                    >Submit</button
                >
            </div>
        </div>
    </form>
{:else}
    <div class="has-text-white">
        <p class="has-text-centered">
            How can one edit one's info without <a href="/user/login?next={$page?.url?.pathname}"
                >logging in?</a
            >
        </p>
    </div>
{/if}
