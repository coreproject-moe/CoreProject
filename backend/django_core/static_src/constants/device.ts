function getDevice(): {
    IS_MOBILE: boolean;
    IS_TABLET: boolean;
    IS_DESKTOP: boolean;
} {
    let screenWidth = typeof window !== "undefined" ? window.innerWidth : 0;

    return {
        IS_MOBILE: screenWidth < 768,
        IS_TABLET: screenWidth >= 768 && screenWidth < 1024,
        IS_DESKTOP: screenWidth >= 1024,
    };
};

export const { IS_MOBILE, IS_TABLET, IS_DESKTOP} = getDevice();