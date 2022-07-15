import Document, { Head, Html, Main, NextScript } from 'next/document';

export default class _Document extends Document {
    render() {
        return (
            <Html
                lang="en"
                style={{
                    backgroundColor: 'black',
                }}
            >
                <Head>
                    <link rel="icon" href="/logos/favicon.svg" />

                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}
