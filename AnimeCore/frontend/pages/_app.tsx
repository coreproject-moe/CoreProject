import 'styles/globals.scss';
import Head from 'next/head';
import type { AppProps } from 'next/app';

function MyApp({ Component, pageProps }: AppProps) {
    return (
        <>
            <Head>
                <title>AnimeCore</title>
            </Head>
            <Component {...pageProps} />
        </>
    );
}

export default MyApp;
