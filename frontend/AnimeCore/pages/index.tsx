import { createStyles, Flex } from '@mantine/core';
import AnimeCoreLogo from '@icons/AnimeCoreLogo.svg';
import Navbar from '@components/Home/Navbar';

const useStyles = createStyles((theme) => ({
    main: {
        width: '100%',
    },

    mainNavbar: {
        height: 80,
        width: '100%',
        alignItems: 'center',
        alignSelf: 'flex-start',
        justifyContent: 'center',
    },
    mainContent: {
        flex: 100,
    },
}));

export default function DoubleNavbar() {
    const { classes } = useStyles();

    return (
        <Flex>
            <Navbar />
            {/* Main Contents */}
            <Flex justify="center" direction="column" className={classes.main}>
                <Flex className={classes.mainNavbar}>
                    <AnimeCoreLogo />
                </Flex>
                <Flex className={classes.mainContent}>HEllo</Flex>
            </Flex>
        </Flex>
    );
}
