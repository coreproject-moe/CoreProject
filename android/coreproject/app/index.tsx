import { View, Text } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import React from 'react';

export default function App() {
    return (
        <SafeAreaProvider>
            <StatusBar style="auto" />
            <View className="flex items-center h-screen justify-center bg-white">
                <Text className="text-2xl">Yo my man Hello world</Text>
            </View>
        </SafeAreaProvider>
    );
}
