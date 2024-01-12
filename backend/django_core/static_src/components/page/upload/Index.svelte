<script lang="ts">
    let has_token = false;
</script>

{#if has_token}
    <login-container class="h-screen w-screen md:grid md:grid-cols-[2fr_1fr] md:gap-[5vw] md:px-[5vw] md:pt-[5vw]">
        <form class="h-full w-full">
            <span class="text-2xl font-semibold md:text-[1.5vw] md:leading-[1.5vw]">
                Paste your
                <span class="text-warning-400 inline-flex">API</span>
                token
            </span>
            <span class="text-surface-50 text-xl md:text-[1vw] md:leading-[2vw]">for seamless integration</span>

            <providers class="mt-10 flex md:mt-[5vw]">
                <streamsb class="flex w-full flex-col md:gap-[0.35vw]">
                    <span class="text-xl font-semibold md:text-[1.25vw] md:leading-[1.5vw]">Stream SB</span>
                    <token-input class="flex justify-between gap-5 md:gap-[1vw]">
                        <input
                            name="streamsb"
                            placeholder="StreamSB token"
                            class="border-primary-500 focus:border-primary-400 h-12 w-full rounded-xl border-2 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.5vw] md:rounded-[0.6vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]"
                        />
                        <button
                            type="submit"
                            class="btn btn-primary font-semibold leading-none md:h-[3.5vw] md:w-[9vw] md:rounded-[0.6vw] md:text-[1vw]"
                        >
                            <span>Continue</span>
                            <!-- {% include "icons/chevron.html" with class="w-4 -rotate-90 md:w-[1.25vw]" %} -->
                        </button>
                    </token-input>
                    <info class="flex items-center gap-2 md:gap-[0.5vw]">
                        <coreproject-icon-info class="w-3 opacity-70 md:w-[1vw]"></coreproject-icon-info>

                        <span class="text-surface-300 text-[0.7rem] leading-none md:text-[0.9vw]">Insert your unique API token here to unlock the full potential of Streamsb's video services</span>
                    </info>
                </streamsb>
            </providers>
        </form>
        <character-image class="flex flex-col items-end justify-end">
            <gradient class="pointer-events-none absolute [background:var(--mobile-gradient)] md:[background:var(--desktop-gradient)]"></gradient>

            <img
                src="https://github-production-user-asset-6210df.s3.amazonaws.com/114811070/281985715-a3a0f410-bf85-4d99-b736-6a386cba716d.png"
                alt="Fish"
            />
        </character-image>
    </login-container>
{:else}
    <div class="flex h-screen w-screen flex-col bg-secondary p-5 md:gap-[3vw] md:px-[5vw] md:py-[3vw]">
        <upload-area class="grid grid-cols-12 gap-7 md:gap-[5vw] md:px-[10vw]">
            <upload-progress class="col-span-12 mt-20 flex items-end md:col-span-7 md:pb-[1.5vw]">
                <div class="w-full text-center md:text-left">
                    <progress
                        class="progress progress-primary w-full md:h-[0.75vw]"
                        value="75"
                        max="100"
                    ></progress>
                    <progress-info class="mt-5 flex flex-col gap-3 leading-none md:mt-[1.5vw] md:gap-[0.5vw]">
                        <span class="font-semibold md:text-[1vw]">300.69B</span>
                        <span class="text-surface-50 md:text-[1vw]">7 files</span>
                    </progress-info>
                </div>
            </upload-progress>
            <upload-input class="col-span-12 flex cursor-pointer flex-col items-center justify-center bg-neutral md:col-span-5 md:h-[12vw] md:gap-[0.25vw] md:rounded-[0.75vw]">
                <coreproject-icon-upload class="text-white md:w-[2vw]"></coreproject-icon-upload>
                <span class="font-semibold md:mt-[1vw] md:text-[1.1vw]">Drag and Drop files</span>
                <div class="divider m-0 before:bg-accent/25 after:bg-accent/25 md:px-[10vw] md:text-[0.9vw] md:before:h-[0.15vw] md:after:h-[0.15vw]">Or</div>
                <span class="font-semibold md:text-[1.1vw]">Browse</span>
            </upload-input>
        </upload-area>
        <div class="divider md:m-0 md:before:h-[0.2vw] md:after:h-[0.2vw]"></div>
        <uploads>
            <uploads-options class="flex flex-col justify-between md:flex-row">
                <div class="flex items-center justify-between md:justify-start md:gap-[3vw]">
                    <form class="relative flex items-center">
                        <button
                            class="absolute left-2 p-0 md:left-[1vw]"
                            aria-label="Search"
                        >
                            <coreproject-icon-search class="opacity-75 md:w-[1.25vw]"></coreproject-icon-search>
                        </button>
                        <input
                            type="text"
                            placeholder="Search"
                            class="placeholder:text-surface-50 h-full w-56 rounded-lg border-none bg-neutral pl-12 text-base leading-none text-white shadow-lg !ring-0 placeholder:font-medium md:w-full md:rounded-[0.5vw] md:py-[0.75vw] md:pl-[3vw] md:text-[1.1vw]"
                        />
                    </form>
                    <button class="text-surface-50 btn flex min-h-full gap-2 !bg-transparent p-0 capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                        <coreproject-icon-cross class="w-4 rotate-45 md:w-[1vw]"></coreproject-icon-cross>
                        New folder
                    </button>
                </div>

                <div class="mt-5 flex justify-between md:mt-0 md:justify-start md:gap-[3vw]">
                    <button class="text-surface-50 btn flex min-h-full gap-3 !bg-transparent p-0 text-base font-semibold capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                        <coreproject-icon-edit class="w-4 md:w-[1vw]"></coreproject-icon-edit>

                        <span>Rename</span>
                    </button>
                    <button class="text-surface-50 btn flex min-h-full gap-3 !bg-transparent p-0 text-base font-semibold capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                        <coreproject-icon-edit class="w-4 md:w-[1vw]"></coreproject-icon-edit>
                        <span>Edit Details</span>
                    </button>
                    <button class="text-surface-50 btn flex min-h-full gap-3 !bg-transparent p-0 text-base font-semibold capitalize leading-none md:gap-[0.5vw] md:rounded-[0.25vw] md:text-[1vw]">
                        <coreproject-icon-delete class="w-4 md:w-[1vw]"></coreproject-icon-delete>
                        <span>Delete</span>
                    </button>
                </div>
            </uploads-options>

            <uploads-table
                hidden
                class="mt-10 block md:mt-[3vw]"
            >
                <table class="text-surface-50 w-full border-separate border-spacing-y-2 leading-none md:border-spacing-y-[0.25vw]">
                    <thead>
                        <tr class="text-left md:text-[1vw]">
                            <th>
                                <input
                                    type="checkbox"
                                    class="cursor-pointer rounded border-2 bg-transparent focus:ring-0 focus:ring-offset-0 md:h-[1.25vw] md:w-[1.25vw] md:border-[0.2vw]"
                                />
                            </th>
                            <th>
                                <div class="flex items-center md:gap-[0.5vw]">
                                    <span class="capitalize">name</span>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="rotate-180 opacity-50 md:w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                </div>
                            </th>
                            <th>
                                <div class="flex items-center md:gap-[0.5vw]">
                                    <span class="capitalize">type</span>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="rotate-180 opacity-50 md:w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                </div>
                            </th>
                            <th>
                                <div class="flex items-center md:gap-[0.5vw]">
                                    <span class="capitalize">date modified</span>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="rotate-180 opacity-50 md:w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                </div>
                            </th>
                            <th>
                                <div class="flex items-center md:gap-[0.5vw]">
                                    <span class="capitalize">size</span>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                    <button class="btn min-h-full !bg-transparent p-0">
                                        <coreproject-icon-chevron class="rotate-180 opacity-50 md:w-[1vw]"></coreproject-icon-chevron>
                                    </button>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <!-- spacing -->
                    <tbody>
                        <tr>
                            <td class="h-5 md:h-[1vw]" />
                        </tr>
                    </tbody>
                    <!-- spacing -->
                    <tbody></tbody>
                </table>
            </uploads-table>
            <empty-ui class="flex w-full flex-col items-center justify-center md:flex-row md:gap-[2vw]">
                <coreproject-icon-empty class="w-32 stroke-accent stroke-[0.15vw] md:w-[10vw] md:stroke-accent/50"></coreproject-icon-empty>
                <div class="flex flex-col items-center gap-2 md:items-start md:gap-[0.75vw]">
                    <span class="text-base font-semibold leading-none text-accent md:text-[1.4vw]">Empty!</span>
                    <span class="text-sm leading-none text-accent/50 md:text-[1.1vw]">Upload something to make kokoro-chan happy</span>
                </div>
            </empty-ui>
        </uploads>
    </div>
{/if}
