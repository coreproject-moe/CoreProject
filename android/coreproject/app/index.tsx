import { View, Text } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';

SplashScreen.preventAutoHideAsync();

export default function App() {
    const [fontsLoaded] = useFonts({
        Kokoro: require('../assets/fonts/Kokoro/Kokoro-Regular.otf'),
    });
    const onLayoutRootView = React.useCallback(async () => {
        if (fontsLoaded) {
            await SplashScreen.hideAsync();
        }
    }, [fontsLoaded]);

    if (!fontsLoaded) {
        return null;
    }
    return (
        <SafeAreaProvider onLayout={onLayoutRootView}>
            <StatusBar style="auto" />
            <View className="flex items-center h-screen justify-center bg-white">
                <Text className="text-2xl">Yo my mfan Hello world</Text>
            </View>
        </SafeAreaProvider>
    );
}
