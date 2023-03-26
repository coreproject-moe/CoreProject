import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Text, View, SafeAreaView } from 'react-native';
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';

SplashScreen.preventAutoHideAsync();

export default function App() {
    const [fontsLoaded] = useFonts({
        Kokoro: require('./assets/fonts/Kokoro/Kokoro-Regular.otf'),
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
        <SafeAreaView onLayout={onLayoutRootView}>
            <StatusBar style="auto" />

            <View className="h-full flex items-center justify-center text-2xl bg-white">
                <Text>Hi i am working on android app</Text>
            </View>
        </SafeAreaView>
    );
}
