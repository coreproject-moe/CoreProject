/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    productionBrowserSourceMaps: true,
    // https://nextjs.org/docs/api-reference/next.config.js/cdn-support-with-asset-prefix
    assetPrefix: '/static',
    /* https://nextjs.org/docs/api-reference/next.config.js/basepath */
    basePath: '/animecore',
    /* https://nextjs.org/docs/api-reference/next.config.js/trailing-slash */
    trailingSlash: true,
    /* https://nextjs.org/docs/api-reference/next.config.js/build-indicator*/
    devIndicators: {
        buildActivityPosition: 'bottom-right',
    },
    webpack: (config) => {
        config.module.rules.push({
            test: /\.svg$/i,
            issuer: /\.[jt]sx?$/,
            use: ['@svgr/webpack'],
        });

        return config;
    },
};

module.exports = nextConfig;
