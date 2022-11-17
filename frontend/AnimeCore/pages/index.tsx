import { useState } from 'react';
import {
    createStyles,
    Navbar,
    UnstyledButton,
    Flex,
    Text,
} from '@mantine/core';
import { useMantineTheme } from '@mantine/core';
import Logo from '@static/logos/favicon.svg';

import HelpOutline from '@static/icons/help outline.svg';
import AnimeCoreLogo from '@static/logos/favicon.svg';

const useStyles = createStyles((theme) => ({
    sideBar: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
    },

    main: {
        flex: 1,
        backgroundColor: theme.colors.gray[0],
    },

    mainLink: {
        width: 56,
        height: 54,
        borderRadius: theme.radius.md,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: theme.white,

        '&:hover': {
            backgroundColor: theme.colors.blue[2],
            color: theme.colors.blue[2],

            svg: {
                color: theme.black,
            },
        },
    },

    mainLinkActive: {
        '&, &:hover': {
            backgroundColor: theme.colors.blue[6],
        },
    },

    link: {
        boxSizing: 'border-box',
        display: 'block',
        textDecoration: 'none',
        borderTopRightRadius: theme.radius.md,
        borderBottomRightRadius: theme.radius.md,
        color: theme.colors.gray[7],
        padding: `0 ${theme.spacing.md}px`,
        fontSize: theme.fontSizes.sm,
        marginRight: theme.spacing.md,
        fontWeight: 500,
        height: 44,
        lineHeight: '44px',

        '&:hover': {
            backgroundColor: theme.colors.gray[1],
            color: theme.black,
        },
    },

    linkActive: {
        '&, &:hover': {},
    },
}));

const Icons = {
    start: [{ name: 'AnimeCore', icon: AnimeCoreLogo }],
    middle: [],
    last: [
        {
            name: 'Settings',
            icon: require('@static/icons/settings.svg').default,
        },
        { name: 'Misc.', icon: import('@static/icons/help outline.svg') },
    ],
};

export default function DoubleNavbar() {
    const { classes, cx } = useStyles();
    const [active, setActive] = useState('Releases');
    const [activeLink, setActiveLink] = useState('Settings');
    const theme = useMantineTheme();

    return (
        <Navbar height={'100vh'} width={{ md: 100 }}>
            <Navbar.Section grow className={classes.sideBar}>
                <Flex
                    mih={50}
                    gap="sm"
                    justify="flex-end"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    <Logo />
                </Flex>
                <Flex
                    mih={50}
                    gap="sm"
                    justify="flex-end"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    pass
                </Flex>
                <Flex
                    mih={50}
                    gap="xl"
                    justify="flex-start"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    {Icons.start.map((item, key) => {
                        return (
                            <>
                                <UnstyledButton className={classes.mainLink}>
                                    <Flex
                                        direction="column"
                                        align="center"
                                        justify="center"
                                        gap={4}
                                        key={key}
                                    >
                                        <item.icon />
                                        <Text fw={600} fz="sm">
                                            {item.name}
                                        </Text>
                                    </Flex>
                                </UnstyledButton>
                            </>
                        );
                    })}
                </Flex>
            </Navbar.Section>
        </Navbar>
    );
}
