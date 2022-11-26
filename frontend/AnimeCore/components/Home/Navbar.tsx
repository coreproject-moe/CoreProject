import { useRef, useState } from 'react';
import {
    createStyles,
    Navbar,
    UnstyledButton,
    Flex,
    Text,
    Space,
} from '@mantine/core';
import { useMantineTheme } from '@mantine/core';
import { useSpotlight } from '@mantine/spotlight';
import { useEffect } from 'react';

const useStyles = createStyles((theme) => ({
    hoverDiv: {
        position: 'absolute',
        display: 'flex',
        background: theme.colors.blue[2],
        borderRadius: theme.radius.md,
        height: 54,
        width: 54,
        zIndex: 2,
        opacity: 0,
    },
    nav: {
        backgroundColor: theme.colors.blue[9],
    },
    sideBar: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
    },

    mainLink: {
        zIndex: 1000,
        width: 56,
        height: 54,
        borderRadius: theme.radius.md,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: theme.white,

        '&:hover': {
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
        backgroundColor: theme.colors.blue[1],
        color: theme.black,

        ':before': {
            content: '""',
            zIndex: 100,
            width: 4,
            height: 14,
            backgroundColor: theme.colors.blue[3],
            position: 'absolute',
            borderRadius: theme.radius.md,
            transform: 'translateX(-28.5px)',
        },
        svg: {
            color: theme.black,
        },
        div: {
            color: 'transparent',
        },
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
        transition: `all .2s ease`,

        '&:hover': {
            backgroundColor: theme.colors.yellow[3],
        },
    },

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

const Icons = {
    start: [
        {
            name: 'AnimeCore',
            icon: require('@icons/BlueAnimeLogo.svg').default,
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

const ANIMATION_DURATION = 75;

export default function DoubleNavbar() {
    const { classes, cx } = useStyles();
    const [active, setActive] = useState('Home');
    const theme = useMantineTheme();
    const spotlight = useSpotlight();

    const middleIconContainerDiv = useRef<HTMLDivElement | null>(null);
    const animationItemRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        animationItemRef!.current!.style.transform = `translateY(${
            middleIconContainerDiv!.current?.getBoundingClientRect().top
        }px)`;
    }, [middleIconContainerDiv, animationItemRef]);

    const mouseEnterIcon = (item: React.MouseEvent) => {
        if (animationItemRef.current) {
            const element = item.currentTarget as HTMLDivElement;
            animationItemRef.current.style.transform = `translateY(${Math.round(
                element.getBoundingClientRect().top
            )}px)`;

            const childElement = element.firstChild as SVGElement;
            childElement.style.color = theme.black;
        }
    };

    const mouseLeaveIcon = (item: React.MouseEvent) => {
        if (animationItemRef.current) {
            const element = item.currentTarget as HTMLDivElement;
            element.style.opacity = '1';

            const childElement = element.firstChild as SVGElement;
            childElement.style.color = theme.white;
        }
    };

    const mouseEnterIconParent = (item: React.MouseEvent) => {
        // Maybe fix the animation logic someday
        // If it works dont break it

        animationItemRef!.current!.style.transform = `translateY(${Math.round(
            item.currentTarget.getBoundingClientRect().top
        )}px)`;

        setTimeout(() => {
            animationItemRef!.current!.style.opacity = '1';
            animationItemRef.current!.style.transitionDuration = '150ms';
        }, ANIMATION_DURATION);
    };

    const mouseLeaveIconParent = () =>
        // item: React.MouseEvent
        {
            animationItemRef!.current!.style.opacity = '0';
            setTimeout(() => {
                animationItemRef.current!.style.transitionDuration = '0ms';
            }, ANIMATION_DURATION);
        };

    const mouseLeavesNavElement = () =>
        // item: React.MouseEvent
        {
            animationItemRef!.current!.style.opacity = '0';
        };

    return (
        <Flex onMouseLeave={mouseLeavesNavElement}>
            <Navbar
                className={classes.nav}
                height={'100vh'}
                width={{ md: 100 }}
            >
                <Navbar.Section grow className={classes.sideBar}>
                    <div
                        ref={animationItemRef}
                        className={classes.hoverDiv}
                    ></div>
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
                                    onClick={() => {
                                        spotlight.openSpotlight();
                                    }}
                                >
                                    <Flex
                                        direction="column"
                                        align="center"
                                        justify="center"
                                    >
                                        <item.icon />
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
                        ref={middleIconContainerDiv}
                        onMouseEnter={mouseEnterIconParent}
                        onMouseLeave={mouseLeaveIconParent}
                    >
                        {Icons.middle.map((item, index) => {
                            return (
                                <UnstyledButton
                                    key={index}
                                    className={cx(classes.mainLink, {
                                        [classes.linkActive]:
                                            active === item.name,
                                    })}
                                    onMouseEnter={mouseEnterIcon}
                                    onMouseLeave={mouseLeaveIcon}
                                    onClick={() => setActive(item.name)}
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
                        gap="sm"
                        justify="flex-start"
                        align="center"
                        direction="column"
                        wrap="nowrap"
                        mb="xl"
                        onMouseEnter={mouseEnterIconParent}
                        onMouseLeave={mouseLeaveIconParent}
                    >
                        {Icons.last.map((item, index) => {
                            return (
                                <UnstyledButton
                                    key={index}
                                    className={classes.mainLink}
                                    onMouseEnter={mouseEnterIcon}
                                    onMouseLeave={mouseLeaveIcon}
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
        </Flex>
    );
}
