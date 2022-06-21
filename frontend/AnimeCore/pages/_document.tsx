import Document, { Head, Html, Main, NextScript } from 'next/document';
import Script from 'next/script';

export default class _Document extends Document {
    render() {
        return (
            <Html>
                <Head>
                    <link rel="icon" href="/logos/favicon.svg" />
                    <meta name="darkreader" content="NO-DARKREADER-PLUGIN" />
                    <Script src="https://cdn.jsdelivr.net/npm/no-darkreader@1.0.3/nodarkreader.min.js" />
                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}
