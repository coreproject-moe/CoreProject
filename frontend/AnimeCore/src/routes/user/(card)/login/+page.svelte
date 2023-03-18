<script lang="ts">
    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";
    import { createForm } from "felte";
    import Cookies from "js-cookie";
    import * as yup from "yup";

    import { page } from "$app/stores";
    import { UrlMaps } from "$data/urls";
    const urls = new UrlMaps();
    // Creating yup schema
    const schema = yup.object({
        username: yup
            ?.string()
            ?.required("Please Enter User Name")
            ?.min(0)
            ?.max(50, "User name must be less than 50 Characters"),
        password: yup
            ?.string()
            ?.min(8, "Password must be more than 8 Characters")
            ?.max(1024, "Password must be less than 1024 Characters")
    });

    // Creating the form
    const { form } = createForm({
        initialValues: {
            username: "",
            password: ""
        },
        onSubmit: async (values /*context*/) => {
            const data = new FormData();
            data.append("username", values.username);
            data.append("password", values.password);

            const res = await fetch(urls.login_url, {
                method: "post",
                body: data
            });
            if (res.ok) {
                const data = await res.json();
                Cookies.set("token", data.token, { domain: $page.url.hostname });
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
</script>

<svelte:head>
    <title>CoreProject | Login</title>
</svelte:head>

<div
    style="grid-area: 1 / 1 / 2 / 2"
    class="inline-grid justify-center md:justify-end content-center"
>
    <div
        class="card w-96 bg-base-100 shadow-xl mr-0 md:mr-6 bg-transparent from-base-100 bg-gradient-to-t"
    >
        <div class="card-body rounded-2xl">
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
                    <input
                        style="--tw-bg-opacity:0.30"
                        type="text"
                        placeholder="Username or Email"
                        name="username"
                        class="input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0"
                    />

                    <input
                        style="--tw-bg-opacity:0.30"
                        type="text"
                        placeholder="Password"
                        name="password"
                        class="input w-full text-white font-semibold max-w-xs border-[3px] border-warning focus:outline-0"
                    />
                </div>
                <div class="flex justify-center mt-5 items-center gap-2">
                    <button
                        class="btn btn-secondary font-bold text-black"
                        type="submit"
                    >
                        Login
                    </button>
                    or
                    <a
                        class="underline"
                        href="/signup"
                    >
                        signup
                    </a>
                </div>
            </form>
        </div>
    </div>
</div>

<style lang="scss">
    $border-width: 3px;

    .card {
        border-image: linear-gradient(
                to top,
                transparent 0.1%,
                white 15%,
                transparent,
                rgba(0, 0, 0, 0)
            )
            1 100%;
        border-image-width: $border-width;

        &::before {
            content: "";
            position: absolute;
            bottom: 10.5px;
            right: 0;
            border-left: $border-width solid white;
            border-radius: 9999px;
            width: 1px;
            height: 100px;
            background-color: white;
        }
        &::after {
            content: "";
            position: absolute;
            bottom: 10.5px;
            left: 0;
            border-left: $border-width solid white;
            border-radius: 9999px;
            width: 1px;
            height: 100px;
            background-color: white;
        }
    }
    .card-body {
        z-index: 1;

        &::after {
            position: absolute;
            top: 0px;
            bottom: 0px;
            left: 0px;
            right: 0px;
            z-index: -1;
            box-shadow: inset 0 $border-width * -1 0 0 rgba(250, 250, 250, 0.9);
            content: "";
            border-radius: 16px;
        }
    }
</style>
