module.exports = function (api) {
    api.cache(true);
    return {
        presets: ['babel-preset-expo'],
        plugins: [
            '@babel/plugin-proposal-export-namespace-from',
            'react-native-reanimated/plugin',
            'nativewind/babel', // Nativewind
            require.resolve('expo-router/babel'),
        ],
    };
};
