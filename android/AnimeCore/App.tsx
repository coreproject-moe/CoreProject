import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Text, View } from 'react-native';
import { useFonts } from 'expo-font';

export default function App() {
    const [loaded] = useFonts({
        Montserrat: require('@/assets/fonts/Kokoro/Kokoro-Regular.woff2'),
    });

    if (!loaded) {
        return null;
    }
    return (
        <View className="h-full flex items-center justify-center bg-white">
            <Text>Open up App.js to start working on your app!</Text>
            <StatusBar style="auto" />
        </View>
    );
}
