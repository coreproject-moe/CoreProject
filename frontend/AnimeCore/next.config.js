const isProd = process.env.NODE_ENV === 'production';
/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    productionBrowserSourceMaps: true,
    // https://nextjs.org/docs/api-reference/next.config.js/cdn-support-with-asset-prefix
    assetPrefix: isProd ? '/static' : undefined,
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
        config.module.rules.push({
            test: /\.(woff(2)?|ttf)(\?v=\d+\.\d+\.\d+)?$/,
            use: [
                {
                    loader: 'file-loader',
                    options: {
                        name: '[name].[ext]',
                        outputPath: 'fonts/',
                    },
                },
            ],
        });
        return config;
    },
};

module.exports = nextConfig;
