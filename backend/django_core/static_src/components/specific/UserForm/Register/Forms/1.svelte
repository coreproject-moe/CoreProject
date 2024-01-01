<script lang="ts">
    import CoreText from "$icons/CoreText/Index.svelte";
    import Tick from "$icons/Tick/Index.svelte";
    import ArrowUpRight from "$icons/ArrowUpRight/Index.svelte";
</script>

<form
    on:submit|preventDefault
    class="flex flex-col justify-between h-full"
>
    <div class="flex flex-col gap-2 whitespace-nowrap font-bold uppercase leading-none tracking-widest text-white md:text-[1.2vw] md:gap-[0.5vw]">
        <span class="inline-flex gap-2 md:gap-[0.5vw]">
            create your
            <CoreText />
            account
        </span>
        <span class="uppercase text-xs md:text-[1vw] font-medium text-white/90">unlock the anime world - join us!</span>
    </div>
    <div class="flex flex-col gap-5 md:gap-[1.5vw]">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label for="email" class="mt-4 text-lg font-semibold leading-none md:mt-[1.1vw] md:text-[1.1vw]">
                Email:
            </label>
            <input
                placeholder="Email address"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <span class="mt-[0.75vw] text-xs leading-none text-base-content md:mt-0 md:text-[0.75vw]">
                help text or errors here
            </span>
        </div>
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <label for="password" class="text-lg font-semibold leading-none md:text-[1.1vw]">
                Password:
            </label>
            <input
                placeholder="Password"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <div class="flex flex-col">
                <div class="grid grid-cols-4 gap-[1.5vw] md:gap-[0.75vw]">
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                    <span class="h-[1.75vw] rounded-[0.5vw] md:h-[0.75vw] md:rounded-[0.1875vw] transition-colors md:border-[0.15vw] border-white/25"></span>
                </div >

                <div class="mt-3 md:mt-[1.25vw]">
                    <span class="text-sm font-semibold uppercase leading-none tracking-wider text-surface-50 md:text-[1vw]">must contain</span>

                    <div class="flex flex-col gap-1 md:gap-[0.3vw] md:mt-[0.5vw]">
                        <div class="flex items-center gap-2 md:gap-[0.5vw]">
                            <Tick class="opacity-30 w-3 text-primary md:w-[0.7vw] transition-opacity" />
                            <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">minimum 8 characters</span>
                        </div>
                        <div class="flex items-center gap-2 md:gap-[0.5vw]">
                            <Tick class="opacity-30 w-3 text-primary md:w-[0.7vw] transition-opacity" />
                            <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">minimum 1 special character</span>
                        </div>
                        <div class="flex items-center gap-2 md:gap-[0.5vw]">
                            <Tick class="opacity-30 w-3 text-primary md:w-[0.7vw] transition-opacity" />
                            <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">minimum 1 number</span>
                        </div>
                        <div class="flex items-center gap-2 md:gap-[0.5vw]">
                            <Tick class="opacity-30 w-3 text-primary md:w-[0.7vw] transition-opacity" />
                            <span class="text-[0.7rem] leading-none text-surface-300 md:text-[0.75vw]">minimum 1 lower-case or upper-case character</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-[0.3rem] md:gap-[0.5vw]" >
            <label for="confirm-password" class="text-lg font-semibold leading-none md:text-[1.1vw]">
                Confirm Password:
            </label>
            <input
                placeholder="Confirm Password"
                class="h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
            />
            <span class="leading-none text-xs md:text-[0.75vw]">
                help text or errors here
            </span>
        </div>
    </div>
    <div class="flex items-center justify-between">
        <div class="flex flex-col gap-1 md:gap-[0.5vw]">
            <span class="text-xs leading-none text-surface-100 md:text-[0.75vw]">Already have an account?</span>
            <button class="text-start text-base leading-none md:text-[1.1vw] text-primary underline">
                Login
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
