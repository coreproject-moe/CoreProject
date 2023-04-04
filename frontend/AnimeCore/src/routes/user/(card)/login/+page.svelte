<script lang="ts">
    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";
    import { createForm } from "felte";
    import Cookies from "js-cookie";
    import * as yup from "yup";

    import { UrlMaps } from "$data/urls";
    import { user_is_logged_in } from "$store/User";
    let errorText = "";

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

            const res = await fetch(urls.login(), {
                method: "post",
                body: data
            });
            if (res.ok) {
                const data = await res.json();
                Cookies.set("token", data.token);
                user_is_logged_in.set(true);
            } else {
                errorText = "No such user found with the given <b>Username</b> and <b>Password</b>";
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

{#if $user_is_logged_in}
    <div class="text-center text-2xl text-white">
        You are logged in.
        <br />
        Did you mean to
        <a
            class="link"
            href="./logout"
        >
            log out
        </a>
        ?
    </div>
{:else}
    <div class="h-24 text-center text-2xl text-error">
        {@html errorText}
    </div>
    <form use:form>
        <div class="flex flex-col gap-8">
            {#each input_mapping as input_item}
                <input
                    style="--tw-bg-opacity:0.30"
                    type={input_item.type}
                    placeholder={input_item.placeholder}
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
{/if}
