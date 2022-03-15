<script lang="ts">
    import * as yup from "yup";
    import { createForm } from "felte";
    import { onDestroy } from "svelte";
    import tippy, { animateFill, type Instance } from "tippy.js";

    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";

    import { browser } from "$app/env";
    import { userInfo } from "$store/users";

    import { trapFocus } from "$lib/functions/trapFocus";
    import { projectName } from "$lib/constants/frontend/project";

    // let animePoster: File;
    let animePosterSrc = "";

    let tippyJsAnimePoster: HTMLElement & { _tippy?: Instance };
    let tippyJsUploadElement: HTMLElement & { _tippy?: Instance };

    $: {
        if (browser) {
            if (animePosterSrc) {
                tippy(tippyJsAnimePoster, {
                    content: "Anime Poster",
                    theme: "black",
                    showOnCreate: true,
                    trigger: "manual",
                    delay: 50,
                    hideOnClick: false,
                    animateFill: true,
                    plugins: [animateFill]
                });
            }

            if (tippyJsUploadElement) {
                if (!$userInfo?.is_staff) {
                    tippy(tippyJsUploadElement, {
                        content: `<center>You are not a <b>Staff</b>😕${
                            $userInfo?.is_superuser ? "not a <b>SuperUser</b>" : ""
                        }</center>But do see how we handle the upload.🧐`,
                        theme: "black",
                        allowHTML: true,
                        animateFill: true,
                        plugins: [animateFill]
                    });
                } else {
                    tippyJsUploadElement?._tippy?.destroy();
                }
            }
        }
    }
    onDestroy(async () => {
        // Cleanup
        tippyJsAnimePoster?._tippy?.destroy();
        tippyJsUploadElement?._tippy?.destroy();
    });

    const SUPPORTED_IMAGE_FORMATS = ["image/jpg", "image/jpeg", "image/gif", "image/png"];

    const schema = yup.object({
        anime_name: yup?.string()?.required("Did you enter <b>Anime Name</b>? 🤔"),
        anime_poster: yup
            ?.mixed()
            ?.required("<b>Anime Poster</b> please ? 🥺")
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
            )
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

    const handleImageInput = (e: Event) => {
        const target = e?.target as HTMLInputElement;
        const file = target.files instanceof FileList ? target.files[0] : null;
        tippyJsAnimePoster?._tippy?.destroy();

        if (file) {
            const reader = new FileReader();
            reader.onload = async function () {
                let dataURL = reader.result as string;
                animePosterSrc = dataURL;
            };
            reader.readAsDataURL(file);
        }
    };
</script>

<svelte:head>
    <title>Upload Anime | {projectName}</title>
</svelte:head>

<form use:trapFocus use:form>
    <div class="columns is-mobile is-centered">
        <div class="column is-narrrow">
            <div class="title is-size-4 has-text-white is-unselectable has-text-centered">
                ⛩️ Upload Anime ⛩️
            </div>
        </div>
    </div>

    <div class="columns is-mobile is-centered">
        <div class="column is-narrow">
            <figure class="image" style="width:12em" bind:this={tippyJsAnimePoster}>
                <input
                    type="file"
                    name="anime_poster"
                    class="file-input is-clickable"
                    placeholder="Upload avatar"
                    style="z-index:1000000;"
                    accept="image/*"
                    on:input={handleImageInput}
                />
                {#if animePosterSrc}
                    <img src={animePosterSrc} alt="" />
                {:else}
                    <div
                        class="box has-background-black has-text-centered has-text-white"
                        style="border:2px dotted springgreen"
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
            <div class="label has-text-white is-unselectable">Anime Name :</div>
        </div>
        <div class="field-body">
            <div class="field">
                <p class="control is-expanded has-icons-left">
                    <input
                        type="text"
                        name="anime_name"
                        class="input is-font-face-ubuntu has-text-white has-background-black has-border-gray"
                        placeholder="Anime Name"
                        autocomplete="off"
                    />
                    <span class="icon is-small is-left">
                        <ion-icon class="is-size-4 has-text-white" name="alert-circle-outline" />
                    </span>
                </p>
            </div>
        </div>
    </div>

  

    <div class="columns is-mobile is-centered pt-3">
        <div class="column is-narrow">
            <button
                type="submit"
                bind:this={tippyJsUploadElement}
                class="button is-rounded is-centered has-text-white has-border-gray is-black"
                >Upload</button
            >
        </div>
    </div>
</form>
