module.exports = function (api) {
    api.cache(true);
    return {
        presets: ['babel-preset-expo'],
        plugins: [
            ['nativewind/babel'],
            [
                'babel-plugin-tsconfig-paths',
                {
                    relative: true,
                    extensions: [
                        '.js',
                        '.jsx',
                        '.ts',
                        '.tsx',
                        '.es',
                        '.es6',
                        '.mjs',
                    ],
                    rootDir: '.',
                    tsconfig: 'tsconfig.json',
                    transformFunctions: [
                        'require',
                        'require.resolve',
                        'System.import',
                        'jest.genMockFromModule',
                        'jest.mock',
                        'jest.unmock',
                        'jest.doMock',
                        'jest.dontMock',
                        'jest.setMock',
                        'require.requireActual',
                        'require.requireMock',
                    ],
                },
            ],
        ],
    };
};
