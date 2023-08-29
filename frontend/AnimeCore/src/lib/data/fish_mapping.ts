export const fish_mapping: Array<{
    image: { src: string; alt: string; class?: string };
    class?: string;
    gradient: { mobile: string; desktop: string; class?: string };
    position: Array<"left" | "right">;
}> = [
    {
        image: {
            src: "/images/characters/eliane/eliane.png",
            alt: "Elaine"
        },
        gradient: {
            class: "h-[50dvh] w-[100dvw] md:h-[40dvw] md:w-[calc(100%*2)]",
            mobile: "radial-gradient(50dvh circle at center, rgba(218, 202, 207, 0.25) 0%, transparent 50%)",
            desktop: "radial-gradient(40dvw circle at center, rgba(218, 202, 207, 0.25) 0%, transparent 50%)"
        },
        position: ["left", "right"]
    },
    {
        image: {
            src: "/images/characters/ichigo/ichigo.png",
            alt: "Ichigo",
            class: "ml-auto"
        },
        class: "items-end",
        gradient: {
            class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
            mobile: "radial-gradient(45dvh circle at center, rgba(137, 155, 206, 0.25) 0%, transparent 50%)",
            desktop: "radial-gradient(45dvw circle at center, rgba(137, 155, 206, 0.25) 0%, transparent 50%)"
        },
        position: ["right"]
    },
    {
        image: {
            src: "/images/characters/sasha/sasha.png",
            alt: "Sasha"
        },
        gradient: {
            class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
            mobile: "radial-gradient(50dvh circle at center, rgba(181, 124, 82, 0.25) 0%, transparent 50%)",
            desktop: "radial-gradient(45dvw circle at center, rgba(181, 124, 82, 0.25) 0%, transparent 50%)"
        },
        position: ["left", "right"]
    },
    {
        // credit:'https://www.reddit.com/r/AnimeGirls/comments/pyil5n/my_girl_exy_in_a_plugsuit/',
        image: {
            src: "/images/characters/exy/exy.png",
            alt: "Exy"
        },

        gradient: {
            class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
            mobile: "radial-gradient(50dvh circle at center, rgba(243, 243, 243, 0.25) 0%, transparent 50%)",
            desktop: "radial-gradient(45dvw circle at center, rgba(243, 243, 243, 0.25) 0%, transparent 50%)"
        },
        position: ["left", "right"]
    },
    {
        image: {
            src: "/images/characters/futaba/futaba.png",
            alt: "Futaba"
        },
        gradient: {
            class: "h-[50dvh] w-[100dvw] md:h-[50dvw] md:w-[calc(100%*2)]",
            mobile: "radial-gradient(50dvh circle at center, rgba(171, 143, 125, 0.3) 0%, transparent 50%)",
            desktop: "radial-gradient(45dvw circle at center, rgba(171, 143, 125, 0.6) 0%, transparent 50%)"
        },
        position: ["right", "left"]
    },
    {
        image: {
            src: "/images/characters/eliane/eliane_2.png",
            alt: "Elaine"
        },
        gradient: {
            class: "h-[50dvh] w-[100dvw] md:h-[40dvw] md:w-[calc(100%*2)]",
            mobile: "radial-gradient(50dvh circle at center, rgba(231, 220, 221, 0.2) 0%, transparent 50%)",
            desktop: "radial-gradient(40dvw circle at center, rgba(231, 220, 221, 0.25) 0%, transparent 50%)"
        },
        position: ["left", "right"]
    }
];
