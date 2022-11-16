import { useState } from 'react';
import { createStyles, Navbar, UnstyledButton, Flex } from '@mantine/core';
import {
    IconHome2,
    IconGauge,
    IconDeviceDesktopAnalytics,
    IconFingerprint,
    IconCalendarStats,
    IconUser,
    IconSettings,
} from '@tabler/icons';
import { MantineLogo } from '@mantine/ds';
import Link from 'next/link';

const useStyles = createStyles((theme) => ({
    sideBar: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
    },

    main: {
        flex: 1,
        backgroundColor:
            theme.colorScheme === 'dark'
                ? theme.colors.dark[6]
                : theme.colors.gray[0],
    },

    mainLink: {
        width: 44,
        height: 44,
        borderRadius: theme.radius.md,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color:
            theme.colorScheme === 'dark'
                ? theme.colors.dark[0]
                : theme.colors.gray[7],

        '&:hover': {
            backgroundColor:
                theme.colorScheme === 'dark'
                    ? theme.colors.dark[5]
                    : theme.colors.gray[0],
        },
    },

    mainLinkActive: {
        '&, &:hover': {
            backgroundColor: theme.fn.variant({
                variant: 'light',
                color: theme.primaryColor,
            }).background,
            color: theme.fn.variant({
                variant: 'light',
                color: theme.primaryColor,
            }).color,
        },
    },

    title: {
        boxSizing: 'border-box',
        fontFamily: `Greycliff CF, ${theme.fontFamily}`,
        marginBottom: theme.spacing.xl,
        backgroundColor:
            theme.colorScheme === 'dark' ? theme.colors.dark[7] : theme.white,
        padding: theme.spacing.md,
        paddingTop: 18,
        height: 60,
        borderBottom: `1px solid ${
            theme.colorScheme === 'dark'
                ? theme.colors.dark[7]
                : theme.colors.gray[3]
        }`,
    },

    logo: {
        boxSizing: 'border-box',
        width: '100%',
        display: 'flex',
        justifyContent: 'center',
        height: 60,
        paddingTop: theme.spacing.md,
        borderBottom: `1px solid ${
            theme.colorScheme === 'dark'
                ? theme.colors.dark[7]
                : theme.colors.gray[3]
        }`,
        marginBottom: theme.spacing.xl,
    },

    link: {
        boxSizing: 'border-box',
        display: 'block',
        textDecoration: 'none',
        borderTopRightRadius: theme.radius.md,
        borderBottomRightRadius: theme.radius.md,
        color:
            theme.colorScheme === 'dark'
                ? theme.colors.dark[0]
                : theme.colors.gray[7],
        padding: `0 ${theme.spacing.md}px`,
        fontSize: theme.fontSizes.sm,
        marginRight: theme.spacing.md,
        fontWeight: 500,
        height: 44,
        lineHeight: '44px',

        '&:hover': {
            backgroundColor:
                theme.colorScheme === 'dark'
                    ? theme.colors.dark[5]
                    : theme.colors.gray[1],
            color: theme.colorScheme === 'dark' ? theme.white : theme.black,
        },
    },

    linkActive: {
        '&, &:hover': {
            borderLeftColor: theme.fn.variant({
                variant: 'filled',
                color: theme.primaryColor,
            }).background,
            backgroundColor: theme.fn.variant({
                variant: 'filled',
                color: theme.primaryColor,
            }).background,
            color: theme.white,
        },
    },
}));

const mainLinksMockdata = [
    { icon: IconHome2, label: 'Home' },
    { icon: IconGauge, label: 'Dashboard' },
    { icon: IconDeviceDesktopAnalytics, label: 'Analytics' },
    { icon: IconCalendarStats, label: 'Releases' },
    { icon: IconUser, label: 'Account' },
    { icon: IconFingerprint, label: 'Security' },
    { icon: IconSettings, label: 'Settings' },
];

const linksMockdata = [
    'Security',
    'Settings',
    'Dashboard',
    'Releases',
    'Account',
    'Orders',
    'Clients',
    'Databases',
    'Pull Requests',
    'Open Issues',
    'Wiki pages',
];

export default function DoubleNavbar() {
    const { classes, cx } = useStyles();
    const [active, setActive] = useState('Releases');
    const [activeLink, setActiveLink] = useState('Settings');

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
                    HEllo
                </Flex>
                <Flex
                    mih={50}
                    gap="sm"
                    justify="flex-end"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    {mainLinksMockdata.map((link, index) => (
                        <UnstyledButton
                            onClick={() => setActive(link.label)}
                            className={cx(classes.mainLink, {
                                [classes.mainLinkActive]: link.label === active,
                            })}
                            key={index}
                        >
                            <link.icon stroke={1.5} />
                        </UnstyledButton>
                    ))}
                </Flex>
                <Flex
                    mih={50}
                    gap="sm"
                    justify="flex-end"
                    align="center"
                    direction="column"
                    wrap="nowrap"
                >
                    HEllo
                </Flex>
            </Navbar.Section>
        </Navbar>
    );
}
