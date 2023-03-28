import './globals.css';
import localFont from 'next/font/local';

const Kokoro = localFont({
    src: [
        {
            path: '../fonts/Kokoro/Kokoro-Regular.woff2',
            weight: '400',
            style: 'normal',
        },
        {
            path: '../fonts/Kokoro/Kokoro-Italic.woff2',
            weight: '400',
            style: 'italic',
        },
        {
            path: '../fonts/Kokoro/Kokoro-Bold.woff2',
            weight: '700',
            style: 'normal',
        },
        {
            path: '../fonts/Kokoro/Kokoro-BoldItalic.woff2',
            weight: '700',
            style: 'italic',
        },
        {
            path: '../fonts/Kokoro/Kokoro-SemiBold.woff2',
            weight: '600',
            style: 'bold',
        },
        {
            path: '../fonts/Kokoro/Kokoro-SemiBoldItalic.woff2',
            weight: '600',
            style: 'italic',
        },
    ],
    variable: '--font-kokoro',
});

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="en" className={`${Kokoro.variable} font-sans`}>
            <body>{children}</body>
        </html>
    );
}
