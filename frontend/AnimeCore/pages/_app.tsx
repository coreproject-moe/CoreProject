import { MantineProvider } from '@mantine/core';
import { ModalsProvider } from '@mantine/modals';
import { NotificationsProvider } from '@mantine/notifications';
import { AppProps } from 'next/app';
import Head from 'next/head';
import NextNProgress from 'nextjs-progressbar';
import { SpotlightProvider } from '@mantine/spotlight';
import localFont from '@next/font/local';

const kokoroFont = localFont({
    src: [
        {
            path: '../fonts/Kokoro/Kokoro-SemiBoldItalic.woff2',
        },
        {
            path: '../fonts/Kokoro/Kokoro-SemiBold.woff2',
        },
        {
            path: '../fonts/Kokoro/Kokoro-BoldItalic.woff2',
        },
        {
            path: '../fonts/Kokoro/Kokoro-Italic.woff2',
        },
        {
            path: '../fonts/Kokoro/Kokoro-Bold.woff2',
        },
        {
            path: '../fonts/Kokoro/Kokoro-Regular.woff2',
        },
    ],
    preload: true,
});

const App = (props: AppProps) => {
    const { Component, pageProps } = props;

    return (
        <>
            <Head>
                <title>AnimeCore</title>
                <meta
                    name="viewport"
                    content="minimum-scale=1, initial-scale=1, width=device-width"
                />
                <link rel="icon" href="logos/favicon.svg" />
            </Head>

            <MantineProvider
    withGlobalStyles
    withNormalizeCSS
    theme={{
        /** Put your mantine theme override here */
        colorScheme: 'dark',
        /** Font Family */
        fontFamily: kokoroFont.style.fontFamily,
        /** Heading */
        headings: {
            sizes: {
                h1: { fontSize: 60 },
                h2: { fontSize: 40 },
                h3: { fontSize: 32 },
                h4: { fontSize: 24 },
                h5: { fontSize: 20 },
                h6: { fontSize: 16 },
            },
        },

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
                <ModalsProvider>
                    <SpotlightProvider actions={[]}>
                        <NotificationsProvider position="top-right">
                            <NextNProgress />
                            <Component {...pageProps} />
                        </NotificationsProvider>
                    </SpotlightProvider>
                </ModalsProvider>
            </MantineProvider>
        </>
    );
};

export default App;
