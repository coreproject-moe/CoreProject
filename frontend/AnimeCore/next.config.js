/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    experimental: {
        runtime: 'nodejs',
        serverComponents: true,
    },
};

module.exports = nextConfig;
