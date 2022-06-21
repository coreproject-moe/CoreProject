import Document, { Head, Html, Main, NextScript } from 'next/document';
import 'no-darkreader';

export default class _Document extends Document {
    render() {
        return (
            <Html>
                <Head>
                    <link rel="icon" href="/logos/favicon.svg" />
                    <meta name="darkreader" content="NO-DARKREADER-PLUGIN" />
                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}
