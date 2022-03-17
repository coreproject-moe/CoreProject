<script lang="ts" context="module">
    import { animeInfoEndpoint } from "$urls/restEndpoints";
    import type { Load } from "@sveltejs/kit";

    export const load: Load = async ({ params }) => {
        const res = await fetch(`${animeInfoEndpoint}${params?.id}`, {
            method: "GET"
        });
        const data = res.ok && (await res.json());
        return {
            props: {
                animeName: data.anime_name
            }
        };
    };
</script>

<script lang="ts">
    export let animeName: string;
    import { trapFocus } from "$lib/functions/trapFocus";

    import * as yup from "yup";
    import { createForm } from "felte";

    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";

    const SUPPORTED_IMAGE_FORMATS = ["video/mp4", "video/x-matroska"];

    const schema = yup.object({
        episode_name: yup?.string()?.required("Did you enter <b>Episode Name</b>? 🤔"),
        episode_file: yup
            ?.mixed()
            ?.required("<b>Episode</b> please ? 🥺")
            ?.test(
                "fileType",
                `Unsupported <b>File</b> format.
                <br/>
                <b>File</b> must be <b>one of the following</b> :
                <br/>
                <br/>
                <ul>
                    ${SUPPORTED_IMAGE_FORMATS?.map((items) => {
                        return `<li><b>${items}</b></li>`;
                    }).join(" ")}
                </ul>`,
                async (value: File) => {
                    if (value?.size > 0) {
                        return SUPPORTED_IMAGE_FORMATS?.includes(value?.type);
                    }
                    return true;
                }
            ),
        episode_summary: yup?.string()?.required("Please enter the <b>Episode Summary</b>")
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
        onSubmit: async (values) => {
            console.log(values);
        }
    });

    let animePosterSrc = "";
</script>

<form use:trapFocus use:form>
    <div class="columns is-mobile is-centered">
        <div class="column is-narrrow">
            <div class="title is-size-4 has-text-white is-unselectable has-text-centered">
                ⛩️ Upload Episode for {animeName} ⛩️
            </div>
        </div>
    </div>

    <div class="columns is-mobile is-centered">
        <div class="column is-narrow">
            <figure class="image" style="width:12em">
                <input
                    type="file"
                    name="episode_file"
                    class="file-input is-clickable"
                    placeholder="Upload avatar"
                    style="z-index:1000000;"
                    accept="video/mp4,video/x-matroska"
                />
                {#if animePosterSrc}
                    <img src={animePosterSrc} alt="" />
                {:else}
                    <div
                        class="box has-background-black has-text-centered has-text-white has-border-green"
                        style="border-style: dotted;border-width:2px;"
                    >
                        <div class="columns is-flex-direction-column">
                            <div class="column pb-0">
                                <ion-icon name="cloud-upload" class="is-size-3" />
                            </div>
                            <div class="column pt-1">Upload</div>
                        </div>
                    </div>
                {/if}
            </figure>
        </div>
    </div>

    <div class="field is-horizontal py-1">
        <div class="field-label is-normal is-hidden-desktop">
            <div class="label has-text-white is-unselectable">Episode Name :</div>
        </div>
        <div class="field-body">
            <div class="field">
                <p class="control is-expanded has-icons-left">
                    <input
                        type="text"
                        name="episode_name"
                        class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                        placeholder="Episode Name"
                        autocomplete="off"
                    />
                    <span class="icon is-small is-left">
                        <ion-icon class="is-size-4 has-text-white" name="alert-circle-outline" />
                    </span>
                </p>
            </div>
        </div>
    </div>

    <div class="field is-horizontal py-1">
        <div class="field-label is-normal is-hidden-desktop">
            <div class="label has-text-white is-unselectable">Episode Name :</div>
        </div>
        <div class="field-body">
            <div class="field">
                <p class="control is-expanded has-icons-left">
                    <textarea
                        name="episode_summary"
                        class="textarea is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                        placeholder="Episode Summary"
                    />
                </p>
            </div>
        </div>
    </div>

    <div class="columns is-mobile is-centered pt-3">
        <div class="column is-narrow">
            <button
                type="submit"
                class="button is-rounded is-centered has-text-white has-border-gray is-black"
                >Upload</button
            >
        </div>
    </div>
</form>
