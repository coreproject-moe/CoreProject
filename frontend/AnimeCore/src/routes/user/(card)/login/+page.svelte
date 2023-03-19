<script lang="ts">
    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";
    import { createForm } from "felte";
    import Cookies from "js-cookie";
    import * as yup from "yup";
    import voca from "voca";

    import { page } from "$app/stores";
    import { UrlMaps } from "$data/urls";

    const input_mapping = [
        {
            type: "text",
            placeholder: "Username or Email",
            name: "username"
        },
        {
            type: "password",
            placeholder: "Password",
            name: "password"
        }
    ];

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

<form use:form>
    <div class="mb-36 flex justify-center">
        <div class="flex select-none text-4xl font-bold">
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

    <div class="flex flex-col gap-8">
        {#each input_mapping as input_item}
            <input
                style="--tw-bg-opacity:0.30"
                type={input_item.type}
                placeholder={voca.upperCase(input_item.placeholder)}
                name={input_item.name}
                class="input h-16 border-[3px] border-warning font-semibold text-white placeholder:uppercase focus:outline-0"
            />
        {/each}
    </div>
    <div class="mt-10 flex items-center justify-center gap-2">
        <button
            class="btn-secondary btn font-bold text-black"
            type="submit"
        >
            Login
        </button>
        or
        <a
            class="link"
            href="./signup"
        >
            signup
        </a>
    </div>
</form>
