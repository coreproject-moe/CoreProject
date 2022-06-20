import '../styles/globals.scss';

import { AppProps } from 'next/app';
import Head from 'next/head';
import { MantineProvider } from '@mantine/core';

export default function App(props: AppProps) {
    const { Component, pageProps } = props;

    return (
        <>
            <Head>
                <title>AnimeCore</title>
                <meta
                    name="viewport"
                    content="minimum-scale=1, initial-scale=1, width=device-width"
                />
            </Head>

            <MantineProvider
                withGlobalStyles
                withNormalizeCSS
                theme={{
                    /** Put your mantine theme override here */
                    colorScheme: 'dark',
                    /** Font Family */
                    fontFamily: 'Kokoro',
                    //** Color */
                    colors: {
                        yellow: [
                            '#FFF2CA',
                            '#F5E6B7',
                            '#F8E5AB',
                            '#EEDBA1',
                            '#EDD68D',
                            '#E9CC75',
                            '#F3D36F',
                            '#EEC959',
                            '#FAD050',
                            '#E3BD49',
                        ],
                    },
                }}
            >
                <Component {...pageProps} />
            </MantineProvider>
        </>
    );
}
