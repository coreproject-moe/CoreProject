const isProd = process.env.NODE_ENV === 'production';
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    productionBrowserSourceMaps: true,
    /* https://nextjs.org/docs/api-reference/next.config.js/basepath */
    basePath: '',
    /* https://nextjs.org/docs/api-reference/next.config.js/trailing-slash */
    trailingSlash: true,
    /* https://nextjs.org/docs/api-reference/next.config.js/build-indicator*/
    devIndicators: {
        buildActivityPosition: 'bottom-right',
    },

    env: {
        // https://nextjs.org/docs/api-reference/next.config.js/cdn-support-with-asset-prefix
        // This is stupid. But i dont have any better way.
        // B
        assetPrefix: '/',
    },
    /**
     *
     * @param {import('webpack').Configuration} config
     * @param {import('next/dist/server/config-shared').WebpackConfigContext} context
     * @returns {import('webpack').Configuration}
     */
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
