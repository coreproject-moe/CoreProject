<script lang="ts">
    import { cn } from "$functions/classname";
    import * as _ from "lodash-es";
    type Tree = {
        class: string;
        child?: Tree[];
    };

    export let tree_branch: Tree[] = [
        {
            class: "md:h-[0.75vw] md:w-[10vw]",
            child: [
                {
                    class: "md:h-[2vw] md:w-[20vw] md:rounded-[0.5vw]",
                    child: [
                        {
                            class: "md:h-[0.75vw] md:w-[10vw]",
                            child: []
                        }
                    ]
                }
            ]
        },
        {
            class: "md:h-[0.75vw] md:w-[10vw]",
            child: [
                {
                    class: "md:h-[2vw] md:w-[20vw] md:rounded-[0.5vw]",
                    child: [
                        {
                            class: "md:h-[0.75vw] md:w-[10vw]",
                            child: [
                                {
                                    class: "md:h-[0.75vw] md:w-[10vw]",
                                    child: []
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            class: "md:h-[0.75vw] md:w-[10vw]",
            child: [
                {
                    class: "md:h-[2vw] md:w-[20vw] md:rounded-[0.5vw]",
                    child: [
                        {
                            class: "md:h-[0.75vw] md:w-[10vw]",
                            child: [
                                {
                                    class: "md:h-[0.75vw] md:w-[10vw]",
                                    child: []
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            class: "md:h-[0.75vw] md:w-[10vw]",
            child: [
                {
                    class: "md:h-[2vw] md:w-[20vw] md:rounded-[0.5vw]",
                    child: [
                        {
                            class: "md:h-[0.75vw] md:w-[10vw]",
                            child: [
                                {
                                    class: "md:h-[0.75vw] md:w-[10vw]",
                                    child: []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ];
</script>

{#each tree_branch as tree}
    <div class="flex w-full md:gap-[0.75vw]">
        <div class="flex flex-col items-center md:gap-[1vw]">
            <div class="skeleton shrink-0 rounded-full bg-neutral md:h-[2vw] md:w-[2vw]" />
            <div class="h-full bg-neutral md:w-[0.25vw]" />
        </div>
        <div class="flex w-full flex-col md:gap-[1vw]">
            <div class="flex flex-col md:gap-[0.25vw]">
                <div class="skeleton bg-neutral md:h-[0.75vw] md:w-[3vw]" />
                <div class="skeleton bg-neutral md:h-[0.5vw] md:w-[2vw]" />
            </div>
            <div class={cn(tree.class, "skeleton bg-neutral")} />
            <div class="flex md:gap-[0.5vw]">
                <div class="skeleton rounded-full bg-neutral md:h-[0.5vw] md:w-[2vw]" />
                <div class="skeleton rounded-full bg-neutral md:h-[0.5vw] md:w-[2vw]" />
            </div>
            {#if tree.child && !_.isEmpty(tree.child)}
                <svelte:self tree_branch={tree.child} />
            {/if}
        </div>
    </div>
{/each}
