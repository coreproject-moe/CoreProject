import Document, { Head, Html, Main, NextScript } from 'next/document';

export default class _Document extends Document {
    render() {
        return (
            <Html>
                <Head>
                    <link rel="icon" href="/logos/favicon.svg" />
                    <meta
                        name="viewport"
                        content="width=device-width, initial-scale=1.0"
                    />
                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}
