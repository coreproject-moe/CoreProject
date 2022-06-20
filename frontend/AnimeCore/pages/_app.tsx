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
                        blue: [
                            '#F0EEFF',
                            '#DCD9F7',
                            '#AAA4E2',
                            '#7569E1',
                            '#4133BA',
                            '#3325BO',
                            '#2D209B',
                            '#23197D',
                            '#100D33',
                            '#070519',
                        ],
                    },
                }}
            >
                <Component {...pageProps} />
            </MantineProvider>
        </>
    );
}
