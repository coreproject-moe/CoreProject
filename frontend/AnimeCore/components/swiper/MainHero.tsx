import React, { useEffect, useState } from 'react';
import {
    createStyles,
    Container,
    Title,
    Text,
    Space,
    Badge,
    Button,
} from '@mantine/core';
import { Navbar } from '../common/Navbar';
import { useMediaQuery } from '@mantine/hooks';
import * as voca from 'voca';

const useStyles = createStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: 'black',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        paddingTop: theme.spacing.xl * 2,
        paddingBottom: theme.spacing.xl * 2,
        minHeight: '90vh',
        boxShadow: `
            inset 0 4px 1800px rgb(7, 5, 25),
            inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7),
            inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)`,

        [theme.fn.smallerThan('md')]: {
            minHeight: '30vh',
            maxHeight: '60vh',
            boxShadow: `
                inset 0px -30px 12px -2px rgba(7, 5, 25, 0.95),
                inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.8),
                inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)`,
        },
    },

    inner: {
        display: 'flex',

        [theme.fn.smallerThan('md')]: {
            flexDirection: 'column',
        },
    },

    image: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
    container: {
        marginTop: 'auto',
        marginLeft: 0,
        paddingLeft: theme.spacing.xl * 4,

        [theme.fn.smallerThan('md')]: {
            paddingLeft: theme.spacing.sm * 2,
            paddingRight: theme.spacing.sm * 2,
        },
    },
    content: {
        paddingTop: theme.spacing.xl * 2,
        paddingBottom: theme.spacing.xl * 2,
        marginRight: theme.spacing.xl * 3,

        [theme.fn.smallerThan('md')]: {
            marginRight: 0,
        },
    },

    title: {
        fontWeight: 900,
        lineHeight: 1.05,
        maxWidth: 500,
        fontSize: 48,
        display: 'flex',
        alignItems: 'center',

        [theme.fn.smallerThan('md')]: {
            maxWidth: '100%',
            fontSize: 34,
            lineHeight: 1.15,
        },
    },

    description: {
        color: theme.white,
        opacity: 0.75,
        maxWidth: 500,

        [theme.fn.smallerThan('md')]: {
            maxWidth: '100%',
        },
    },

    control: {
        paddingLeft: 50,
        paddingRight: 50,
        fontFamily: `Greycliff CF, ${theme.fontFamily}`,
        fontSize: 22,

        [theme.fn.smallerThan('md')]: {
            width: '100%',
        },
    },

    line: {
        color: theme.colors.yellow[6],
    },

    info: {
        ':after': {
            content: '" ▪ "',
        },
    },
    buttonContainer: {
        display: 'flex',
    },
    tagContainer: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
    infoContainer: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
}));

export const MainHero = ({ backgroundImage = '', backgroundBanner = '' }) => {
    const { classes } = useStyles();
    const [wordCount, setWordCount] = useState(0);

    const mobile = useMediaQuery('(min-width: 576px)');
    const tablet = useMediaQuery('(min-width: 768px)');
    const fullhd = useMediaQuery('(min-width: 992px)');

    useEffect(() => {
        if (fullhd) {
            setWordCount(500);
        } else if (tablet) {
            setWordCount(350);
        } else if (mobile) {
            setWordCount(100);
        }
    }, [fullhd, tablet, mobile]);

    return (
        <div
            className={classes.root}
            style={{
                backgroundImage: `url('${
                    mobile ? backgroundBanner : backgroundImage
                }')`,
            }}
        >
            <Navbar />

            <Container size="lg" className={classes.container}>
                <div className={classes.inner}>
                    <div className={classes.content}>
                        <Title className={classes.title}>
                            <Text
                                component="span"
                                size="xl"
                                weight="bold"
                                color="yellow"
                            >
                                Featured
                            </Text>
                            <Space w="sm" />
                            <div
                                className={classes.line}
                                style={{
                                    display: 'inline-block',
                                    width: '60px',
                                    borderTop: '4px solid',
                                    borderRadius: 10,
                                }}
                            />
                        </Title>
                        <Title order={1}>
                            <Text color="white" inherit>
                                Hyouka
                            </Text>
                        </Title>
                        <Title className={classes.infoContainer}>
                            <Text
                                className={classes.info}
                                component="span"
                                color="white"
                            >
                                TV
                            </Text>
                            <Text
                                className={classes.info}
                                component="span"
                                color="white"
                            >
                                22 eps
                            </Text>
                            <Text
                                className={classes.info}
                                component="span"
                                color="white"
                            >
                                Completed
                            </Text>
                            <Text
                                className={classes.info}
                                component="span"
                                color="white"
                            >
                                Spring 2012
                            </Text>
                            <Text component="span" color="white">
                                Kyoto Animations
                            </Text>
                        </Title>
                        <Space h="md" />
                        <>
                            <Text color="gray">
                                {voca.truncate(
                                    `Energy-conservative high school student Houtarou Oreki ends up with more than he bargained for when he signs up for the Classic Literature Club at his sister's behest—especially when he realizes how deep-rooted the club's history really is. Begrudgingly, Oreki is dragged into an...`,
                                    wordCount
                                )}
                            </Text>
                        </>
                        <Space h="xl" />
                        <div className={classes.tagContainer}>
                            <Badge
                                component="span"
                                size="lg"
                                radius="sm"
                                variant="filled"
                                mr="md"
                                sx={(theme) => ({
                                    backgroundColor: theme.colors.blue[9],
                                })}
                            >
                                Mystery
                            </Badge>
                            <Badge
                                component="span"
                                size="lg"
                                radius="sm"
                                variant="filled"
                                mr="md"
                                sx={(theme) => ({
                                    backgroundColor: theme.colors.blue[9],
                                })}
                            >
                                Slice of Life
                            </Badge>
                        </div>
                        <Space h="xl" />
                        <div className={classes.buttonContainer}>
                            <Button
                                sx={(theme) => ({
                                    backgroundColor: theme.colors.yellow[9],
                                    height: 60,

                                    [theme.fn.largerThan('sm')]: { width: 60 },
                                })}
                                radius="lg"
                            >
                                <img
                                    src="/icons/play.svg"
                                    width={24}
                                    height={24}
                                />
                                <Text color="dark" weight={700}>
                                    Watch
                                </Text>
                            </Button>
                            <Button
                                ml="xl"
                                color="yellow"
                                variant="outline"
                                sx={(theme) => ({
                                    borderWidth: 4,
                                    height: 60,
                                    borderColor: theme.colors.yellow[9],
                                })}
                                radius="lg"
                                rightIcon={
                                    <img src="/icons/chevrons-right.svg" />
                                }
                            >
                                <Text weight={700} size="lg" color="yellow">
                                    Details
                                </Text>
                            </Button>
                        </div>
                    </div>
                </div>
            </Container>
        </div>
    );
};
