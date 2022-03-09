<script lang="ts">
    import { trapFocus } from "$lib/functions/trapFocus";
    import { userInfo } from "$store/users";

    import * as yup from "yup";
    import { createForm } from "felte";

    import { validator } from "@felte/validator-yup";
    import reporter from "@felte/reporter-tippy";

    const schema = yup.object({
        first_name: yup?.string()?.max(20, "First name must be less than 20 Characters"),
        last_name: yup?.string()?.max(20, "Last name must be less than 20 Characters"),
        username: yup
            ?.string()
            ?.required("Please Enter User Name")
            ?.min(0)
            ?.max(50, "User name must be less than 50 Characters"),
        email: yup?.string()?.email("Enter a valid Email")?.required("Please Enter Email"),
        password: yup
            ?.string()
            ?.min(8, "Password must be more than 8 Characters")
            ?.matches(
                /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/,
                "Must Contain 8 Characters, One Uppercase, One Lowercase, One Number and one special case Character"
            )
            ?.max(1024, "Password must be less than 1024 Characters"),
        confirmPassword: yup
            ?.string()
            ?.oneOf([yup.ref("password"), null], "Passwords are not the same")
    });
    const { form } = createForm<yup.InferType<typeof schema>>({
        initialValues: {
            first_name: $userInfo?.first_name,
            last_name: $userInfo?.last_login,
            username: $userInfo?.username,
            email: $userInfo?.email
        },
        extend: [
            validator({ schema }),
            reporter({
                tippyProps: {
                    theme: "black"
                }
            })
        ]
        
        // ...
    });
</script>

<form use:form use:trapFocus>
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
                        class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                        placeholder="First Name"
                        autocomplete="off"
                    />
                    <span class="icon is-small is-left">
                        <ion-icon class="is-size-4 has-text-white" name="alert-circle-outline" />
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
                        class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                        placeholder="Last Name"
                        autocomplete="off"
                    />
                    <span class="icon is-small is-left">
                        <ion-icon class="is-size-4 has-text-white" name="alert-circle-outline" />
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
                        class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                        placeholder="Username"
                        autocomplete="off"
                    />
                    <span class="icon is-small is-left">
                        <ion-icon class="is-size-4 has-text-white" name="person-circle-outline" />
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
                        name="email"
                        class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
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
