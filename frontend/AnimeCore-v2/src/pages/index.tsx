import { Flex } from '@mantine/core';
import dynamic from 'next/dynamic';

const Navbar = dynamic(import('@components/Home/Navbar'));
const Main = dynamic(import('@components/Home/Main'));

export default function DoubleNavbar() {
    return (
        <Flex>
            <Navbar />
            {/* Main Contents */}
            <Main />
        </Flex>
    );
}
