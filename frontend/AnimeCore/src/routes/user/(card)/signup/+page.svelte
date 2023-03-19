<!-- https://github.com/baseplate-admin/CoreProject/blob/django-patch/backend/django_core/apps/user/templates/user/signup.html -->
<script lang="ts">
    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";
    import { createForm } from "felte";
    import * as yup from "yup";

    import { goto } from "$app/navigation";
    import { UrlMaps } from "$data/urls";
    const urls = new UrlMaps();
    // Creating yup schema
    const schema = yup.object({
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
        confirm_password: yup
            ?.string()
            ?.oneOf(
                [yup.ref("password"), null],
                "<b>Confirm Password</b> and <b>Password</b> are not the same"
            )
    });
    // Creating the form
    const { form } = createForm({
        initialValues: {
            username: "",
            email: "",
            password: "",
            confirm_password: ""
        },
        onSubmit: async (values /*context*/) => {
            const data = new FormData();
            data.append("username", values.username);
            data.append("email", values.email);
            data.append("password", values.password);

            const res = await fetch(urls.signup_url, {
                method: "post",
                body: data
            });

            if (res.ok) {
                goto("/login");
            }
        },
        // onSuccess(response, context) {
        // 	// Do something with the returned value from `onSubmit`.
        // },
        // onError(err, context) {
        // 	// Do something with the error thrown from `onSubmit`.
        // },
        extend: [
            validator({ schema }),
            reporter({
                tippyProps: {
                    allowHTML: true
                }
            })
        ]

        // Debounced async validation
        // debounced: {}
    });
    const input_mapping = [
        {
            type: "text",
            placeholder: "Username",
            name: "username"
        },
        {
            type: "email",
            placeholder: "Email",
            name: "email"
        },
        {
            type: "password",
            placeholder: "Password",
            name: "password"
        },
        {
            type: "password",
            placeholder: "Confirm Password",
            name: "confirm_password"
        }
    ];
</script>

<svelte:head>
    <title>CoreProject | Sign Up</title>
</svelte:head>

<form use:form>
    <div class="flex justify-center mb-10">
        <div class="font-bold text-4xl select-none flex">
            <span class="inline-flex text-white">c</span>
            <span class="inline-flex text-warning">o</span>
            <span class="inline-flex text-white">r</span>
            <span class="inline-flex text-white">e</span>
            &nbsp;
            <span class="inline-flex text-info">p</span>
            <span class="inline-flex text-info">r</span>
            <span class="inline-flex text-info">o</span>
            <span class="inline-flex text-info">j</span>
            <span class="inline-flex text-info">e</span>
            <span class="inline-flex text-info">c</span>
            <span class="inline-flex text-info">t</span>
        </div>
    </div>

    <div class="grid gap-6">
        {#each input_mapping as input_item}
            <input
                style="--tw-bg-opacity:0.30"
                type={input_item.type}
                placeholder={input_item.placeholder}
                name={input_item.name}
                class="input text-white font-semibold border-[3px] h-16 border-warning focus:outline-0 placeholder:uppercase"
            />
        {/each}
    </div>
    <div class="flex justify-center mt-10 items-center gap-2">
        <button
            class="btn btn-secondary font-bold text-black"
            type="submit"
        >
            Register
        </button>
        or
        <a
            class="link"
            href="./login"
        >
            login
        </a>
    </div>
</form>
