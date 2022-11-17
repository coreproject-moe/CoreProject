import { useState } from 'react';
import {
    createStyles,
    Navbar,
    UnstyledButton,
    Flex,
    Text,
    Space,
} from '@mantine/core';
import { useMantineTheme } from '@mantine/core';

const useStyles = createStyles((theme) => ({
    sideBar: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
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
            div: {
                color: 'transparent',
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
    searchButton: {
        width: 40,
        height: 40,
        borderRadius: theme.radius.md,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: theme.black,
        backgroundColor: theme.colors.yellow[5],

        '&:hover': {
            backgroundColor: theme.colors.yellow[3],
        },
    },
}));

const Icons = {
    start: [
        {
            name: 'AnimeCore',
            icon: require('@static/logos/favicon.svg').default,
        },
    ],
    search: [
        {
            name: 'Search',
            icon: require('@icons/search.svg').default,
        },
    ],
    middle: [
        {
            name: 'Home',
            icon: require('@icons/home.svg').default,
        },
        {
            name: 'Discover',
            icon: require('@icons/explore.svg').default,
        },
        {
            name: 'List',
            icon: require('@icons/list.svg').default,
        },
        {
            name: 'Schedule',
            icon: require('@icons/calendar today.svg').default,
        },
        {
            name: 'Forum',
            icon: require('@icons/forum.svg').default,
        },
    ],
    last: [
        {
            name: 'Settings',
            icon: require('@icons/settings.svg').default,
        },
        {
            name: 'Misc.',
            icon: require('@icons/help outline.svg').default,
        },
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
                    {Icons.start.map((item, index) => {
                        return (
                            <Flex
                                key={index}
                                direction="column"
                                align="center"
                                justify="center"
                            >
                                <item.icon />
                            </Flex>
                        );
                    })}
                </Flex>
                <Flex
                    mih={50}
                    gap="sm"
                    justify="flex-end"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    {Icons.search.map((item, index) => {
                        return (
                            <UnstyledButton
                                key={index}
                                className={classes.searchButton}
                            >
                                <Flex
                                    direction="column"
                                    align="center"
                                    justify="center"
                                >
                                    <item.icon></item.icon>
                                </Flex>
                            </UnstyledButton>
                        );
                    })}
                </Flex>
                <Flex
                    mih={50}
                    gap="sm"
                    justify="flex-end"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    {Icons.middle.map((item, index) => {
                        return (
                            <UnstyledButton
                                key={index}
                                className={classes.mainLink}
                            >
                                <Flex
                                    direction="column"
                                    align="center"
                                    justify="center"
                                >
                                    <Space h="lg" />
                                    <item.icon />
                                    <Text fw={600} fz="sm">
                                        {item.name}
                                    </Text>
                                </Flex>
                            </UnstyledButton>
                        );
                    })}
                </Flex>
                <Flex
                    mih={50}
                    gap="xl"
                    justify="flex-start"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                    mb="xl"
                >
                    {Icons.last.map((item, index) => {
                        return (
                            <UnstyledButton
                                key={index}
                                className={classes.mainLink}
                            >
                                <Flex
                                    direction="column"
                                    align="center"
                                    justify="center"
                                >
                                    <Space h="lg" />
                                    <item.icon />
                                    <Text fw={600} fz="sm">
                                        {item.name}
                                    </Text>
                                </Flex>
                            </UnstyledButton>
                        );
                    })}
                </Flex>
            </Navbar.Section>
        </Navbar>
    );
}
