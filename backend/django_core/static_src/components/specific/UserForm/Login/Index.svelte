<script lang="ts">
    import * as _ from "lodash-es";
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import { object_to_form_data } from "$functions/object_to_form_data";

    // Bindings
    let username = "";
    let password = "";

    const handle_submit = async () => {
        if (!_.isString(username) && _.isEmpty(username)) {
            throw new Error("`username` is not a `string` or is Empty");
        }
        if (!_.isString(password) && _.isEmpty(password)) {
            throw new Error("`password` is not a `string` or is Empty");
        }
        const form_data = await object_to_form_data({
            username: username,
            password: password
        });

        const res = await fetch("", {
            method: "POST",
            body: form_data
        });
        if (!res.ok) {
            throw new Error("Login failed");
        }
    };
</script>

<form
    class="flex h-full flex-col justify-between"
    on:submit|preventDefault={handle_submit}
>
    <span class="flex items-center text-lg font-bold uppercase leading-none tracking-widest text-white md:text-[1.5vw]">hey there! welcome back 👋</span>

    <div class="flex flex-col gap-5 md:block">
        <div class="flex flex-col gap-2 md:gap-[0.5vw]">
            <label
                for="username"
                class="text-base font-semibold leading-none md:text-[1.1vw]"
            >
                Username:
            </label>
            <input
                bind:value={username}
                placeholder="sora_amamiya@coreproject.moe / soraamamiya#0001"
                class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 md:gap-[0.5vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.8vw]">we’ll send you a verification email, so please ensure it’s active</span>
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:mt-[1.5vw] md:gap-[0.5vw]">
            <label
                for="username"
                class="text-base font-semibold leading-none md:text-[1.1vw]"
            >
                Password:
            </label>
            <div class="relative flex flex-col">
                <input
                    bind:value={password}
                    placeholder="enter your existing password"
                    class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                />
            </div>
        </div>
        <button class="btn btn-secondary flex h-max min-h-max flex-col items-start p-0 text-start text-base font-semibold leading-none text-primary underline md:mt-[2vw] md:text-[1vw]">
            &lt; forgot password? &gt;
        </button>
    </div>

    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-surface-100 text-xs leading-none md:text-[0.75vw]">Don't have a core account?</span>
            <button class="text-start text-base leading-none text-primary underline md:text-[1.1vw]">Register</button>
        </div>
        <button
            type="submit"
            class="btn btn-primary h-max min-h-max rounded-lg p-4 text-base font-semibold leading-none text-accent md:rounded-[0.5vw] md:p-[1vw] md:text-[0.95vw]"
        >
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
