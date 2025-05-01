import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // images: { unoptimized: true },
  output: "standalone",
  productionBrowserSourceMaps: true,
  experimental: {
    // reactCompiler: true,
  },
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/i,
      use: ["@svgr/webpack"],
    });

    return config;
  },
  turbopack: {
    rules: {
      "*.svg": {
        loaders: ["@svgr/webpack"],
        as: "*.ts",
      },
    },
  },
};

export default nextConfig;
