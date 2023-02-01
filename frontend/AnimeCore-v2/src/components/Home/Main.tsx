import AnimeCoreLogo from '@icons/AnimeCoreLogo.svg';
import { createStyles, Flex } from '@mantine/core';

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
export default function Main() {
    const { classes } = useStyles();

    return (
        <>
            <Flex justify="center" direction="column" className={classes.main}>
                {/* Navbar  */}
                <Flex className={classes.mainNavbar}>
                    <AnimeCoreLogo />
                </Flex>

                <Flex className={classes.mainContent}>HEllo</Flex>
            </Flex>
        </>
    );
}
