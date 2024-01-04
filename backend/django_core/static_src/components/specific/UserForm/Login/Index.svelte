<script lang="ts">
    import Info from "$icons/Info/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
    import * as z from "zod";
    import Markdown from "$components/minor/Markdown/Index.svelte";

    let form_data = {
        email_or_username: "",
        password: ""
    }, form_errors: {
        email_or_username?: string[],
        password?: string[]
    } = {};

    const schema = z.object({
        email_or_username: z.string().min(1, "Please enter a **Email address** or **Username**"),
        password: z.string().min(1, "**Password** can't be empty")
    })

    function validateZod() {
        try {
            schema.parse(form_data);
            // if valid
            form_errors = {};
        } catch (err) {
            if (err instanceof z.ZodError) {
                form_errors = err.flatten().fieldErrors;
            }
        }
    }

    function handleInput() {
        validateZod();
    }

    function handleSubmit() {
        validateZod();

        if (Object.values(form_errors).some((err) => err)) return;
        // do submit logic
    }
</script>

<form
    on:submit|preventDefault={handleSubmit}
    class="flex flex-col justify-between h-full"
>
    <span class="flex items-center text-lg font-bold uppercase leading-none tracking-widest text-white md:text-[1.5vw]">hey there! welcome back 👋</span>

    <div class="flex flex-col gap-5 md:block">
        <div class="flex flex-col gap-2 md:gap-[0.5vw]">
            <label for="username" class="text-base font-semibold leading-none md:text-[1.1vw]">
                Email address / Username:
            </label>
            <input
                bind:value={form_data.email_or_username}
                on:input={handleInput}
                placeholder="sora_amamiya@coreproject.moe / soraamamiya#0001"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex items-center gap-2 md:gap-[0.5vw] text-[0.7rem] leading-none text-surface-300 md:text-[0.8vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if form_errors.email_or_username}
                <Markdown class="text-error" markdown={form_errors.email_or_username[0]} />
                {:else}
                    <span>we’ll send you a verification email, so please ensure it’s active</span>
                {/if}
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:mt-[1.5vw] md:gap-[0.5vw]">
            <label for="username" class="text-base font-semibold leading-none md:text-[1.1vw]">
                Password:
            </label>
            <div class="relative flex flex-col">
                <input
                    bind:value={form_data.password}
                    on:input={handleInput}
                    placeholder="enter your existing password"
                    class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                />
            </div>
            <div class="flex items-center gap-2 md:gap-[0.5vw] text-[0.7rem] leading-none text-surface-300 md:text-[0.8vw]">
                <Info class="w-3 opacity-70 md:w-[0.9vw]" />
                {#if form_errors.password}
                    <Markdown class="text-error" markdown={form_errors.password[0]} />
                {:else}
                    <span>enter password of your account</span>
                {/if}
            </div>
        </div>
        <button
            class="text-start btn btn-secondary p-0 h-max min-h-max text-base font-semibold leading-none text-primary underline md:text-[1vw] flex flex-col items-start md:mt-[2vw]"
        >
            &lt; forgot password? &gt;
        </button>
    </div>

    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-xs leading-none text-surface-100 md:text-[0.75vw]">Don't have a core account?</span>
            <button
                class="text-start text-base leading-none md:text-[1.1vw] text-primary underline"
            >
                Register
            </button>
        </div>
        <button
            type="submit"
            class="btn btn-primary text-accent rounded-lg text-base font-semibold md:rounded-[0.5vw] md:text-[0.95vw] leading-none h-max min-h-max md:p-[1vw] p-4"
        >
            <span>Continue</span>
            <ArrowUpRight class="w-4 rotate-45 md:w-[1vw]" />
        </button>
    </div>
</form>
