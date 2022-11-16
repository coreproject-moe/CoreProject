import { createGetInitialProps } from '@mantine/next';
import Document, { Head, Html, Main, NextScript } from 'next/document';
import Script from 'next/script';

const getInitialProps = createGetInitialProps();

export default class _Document extends Document {
    static getInitialProps = getInitialProps;

    render() {
        return (
            <Html>
                <Head>
                    <Script id="django" strategy="beforeInteractive">{`
                        window.CSRFTOKEN = '{{ csrf_token }}';
                    `}</Script>
                </Head>

                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}
