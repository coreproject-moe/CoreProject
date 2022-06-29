import {
    BackgroundImage,
    Badge,
    Box,
    Button,
    Container,
    createStyles,
    ScrollArea,
    Skeleton,
    Space,
    Text,
    Title,
} from '@mantine/core';
import { useMediaQuery } from '@mantine/hooks';
import React, { RefObject, useEffect, useState } from 'react';
import type { Swiper as SwiperType } from 'swiper';

import { Navbar } from '@/components/common/Navbar';

const useStyles = createStyles((theme) => ({
    box: {
        minHeight: '90vh',
        display: 'flex',

        [theme.fn.smallerThan('md')]: {
            minHeight: '30vh',
            maxHeight: '60vh',
        },
    },
    root: {
        flexDirection: 'column',
        backgroundColor: 'black',
        paddingTop: theme.spacing.xl * 2,
        paddingBottom: theme.spacing.xl * 2,
        height: 'inherit',

        boxShadow: `
            inset 0 4px 1800px rgb(7, 5, 25),
            inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7),
            inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)`,

        [theme.fn.smallerThan('md')]: {
            paddingBottom: theme.spacing.xs * 2,

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

interface IProps {
    key?: number;
    animeTitle: string;
    animeSummary: string;
    animeEpisodeCount: number;
    animeStudio: string;
    animeAirTime: string;
    backgroundImage: string;
    backgroundBanner: string;
    swiper: Partial<SwiperType> | null;
    parentRef?: RefObject<HTMLDivElement>;
}

export const MainHero = (props: IProps) => {
    const { classes } = useStyles();

    const [heroBackgroundImage, setHeroBackgroundImage] = useState<string>('');

    const mobile = useMediaQuery('(min-width: 0px) and (max-width: 576px)');
    const tablet = useMediaQuery('(min-width: 577px) and (max-width: 768px)');
    const fullhd = useMediaQuery('(min-width: 769px) and (max-width: 992px)');

    // Use SWR to fetch data from backend
    // Use (props.key) to get id.

    useEffect(() => {
        if (mobile) {
            setHeroBackgroundImage(props.backgroundBanner);
        } else if (tablet) {
            setHeroBackgroundImage(props.backgroundImage);
        } else if (fullhd) {
            setHeroBackgroundImage(props.backgroundImage);
        } else {
            setHeroBackgroundImage(props.backgroundImage); // This is the normal one
        }
    }, [fullhd, tablet, mobile, props.backgroundBanner, props.backgroundImage]);

    const [isLoading, setIsLoading] = useState(true);

    setTimeout(() => {
        if (isLoading) {
            setIsLoading(false);
        }
    }, 400);

    return (
        <Box className={classes.box}>
            <BackgroundImage
                className={classes.root}
                src={heroBackgroundImage}
                style={{
                    display: 'flex', // This is a weird hack to make the items align properly
                }}
            >
                <Navbar />

                <Container size="lg" className={classes.container}>
                    <div className={classes.inner}>
                        <div className={classes.content}>
                            <Title className={classes.title}>
                                {isLoading ? (
                                    <>
                                        <Skeleton
                                            height={20}
                                            width={120}
                                        ></Skeleton>
                                    </>
                                ) : (
                                    <>
                                        <Text
                                            component="span"
                                            size="xl"
                                            weight="bold"
                                            color="yellow"
                                            sx={(theme) => ({
                                                [theme.fn.smallerThan('sm')]: {
                                                    fontSize:
                                                        theme.fontSizes.sm,
                                                },
                                            })}
                                        >
                                            Featured
                                        </Text>
                                    </>
                                )}

                                <Space w="sm" />
                                {isLoading ? (
                                    <>
                                        <Skeleton
                                            height={20}
                                            width={60}
                                        ></Skeleton>
                                    </>
                                ) : (
                                    <>
                                        <div
                                            className={classes.line}
                                            style={{
                                                display: 'inline-block',
                                                width: '60px',
                                                borderTop: '4px solid',
                                                borderRadius: 10,
                                            }}
                                        />
                                    </>
                                )}
                            </Title>
                            <Title order={1}>
                                {isLoading ? (
                                    <>
                                        <Skeleton
                                            mt="lg"
                                            width={180}
                                            height={50}
                                        />
                                    </>
                                ) : (
                                    <>
                                        <Text
                                            size="lg"
                                            color="white"
                                            inherit
                                            sx={(theme) => ({
                                                [theme.fn.smallerThan('sm')]: {
                                                    fontSize: 30, // Fix Me
                                                },
                                            })}
                                        >
                                            {props.animeTitle}
                                        </Text>
                                    </>
                                )}
                            </Title>
                            <Title className={classes.infoContainer}>
                                {isLoading ? (
                                    <>
                                        <Skeleton
                                            mt="lg"
                                            width={270}
                                            height={20}
                                        />
                                    </>
                                ) : (
                                    <>
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
                                            {props.animeEpisodeCount} eps
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
                                            {props.animeAirTime}
                                        </Text>
                                        <Text component="span" color="white">
                                            {props.animeStudio}
                                        </Text>
                                    </>
                                )}
                            </Title>
                            <Space h="md" />
                            <>
                                {isLoading ? (
                                    <>
                                        <Skeleton
                                            mt="sm"
                                            mb="sm"
                                            height={100}
                                        />
                                    </>
                                ) : (
                                    <>
                                        <ScrollArea
                                            style={{ height: 100 }}
                                            onMouseEnter={() => {
                                                props.swiper?.mousewheel?.disable();
                                            }}
                                            onTouchStart={() => {
                                                props.swiper?.allowTouchMove =
                                                    false;
                                            }}
                                            onMouseLeave={() => {
                                                props.swiper?.mousewheel?.enable();
                                            }}
                                            onTouchEnd={() => {
                                                props.swiper?.allowTouchMove =
                                                    true;
                                            }}
                                            offsetScrollbars={true}
                                        >
                                            <Text
                                                color="gray"
                                                sx={() => ({
                                                    whiteSpace: 'pre-line',
                                                })}
                                            >
                                                {props.animeSummary}
                                            </Text>
                                        </ScrollArea>
                                    </>
                                )}
                            </>
                            <Space h="xl" />
                            <div className={classes.tagContainer}>
                                {isLoading ? (
                                    <>
                                        <Skeleton height={24} width="50vw" />
                                    </>
                                ) : (
                                    <>
                                        <Badge
                                            component="span"
                                            size="lg"
                                            radius="sm"
                                            variant="filled"
                                            mr="md"
                                            sx={(theme) => ({
                                                backgroundColor:
                                                    theme.colors.blue[9],
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
                                                backgroundColor:
                                                    theme.colors.blue[9],
                                            })}
                                        >
                                            Slice of Life
                                        </Badge>
                                    </>
                                )}
                            </div>
                            <Space h="xl" />
                            <div className={classes.buttonContainer}>
                                {isLoading ? (
                                    <>
                                        <Skeleton width="60px" height={60} />
                                    </>
                                ) : (
                                    <>
                                        <Button
                                            color="yellow"
                                            sx={(theme) => ({
                                                backgroundColor:
                                                    theme.colors.yellow[9],
                                                height: 60,

                                                [theme.fn.largerThan('sm')]: {
                                                    width: 60,
                                                },
                                            })}
                                            radius="lg"
                                        >
                                            <img
                                                alt=""
                                                src="/icons/play.svg"
                                                width={24}
                                                height={24}
                                            />
                                            <Text color="dark" weight={700}>
                                                Watch
                                            </Text>
                                        </Button>
                                    </>
                                )}
                                {isLoading ? (
                                    <>
                                        <Skeleton
                                            ml="xl"
                                            height={60}
                                            width={120}
                                        />
                                    </>
                                ) : (
                                    <>
                                        <Button
                                            ml="xl"
                                            color="yellow"
                                            variant="outline"
                                            sx={(theme) => ({
                                                borderWidth: 4,
                                                borderColor:
                                                    theme.colors.yellow[9],
                                                height: 60,
                                            })}
                                            radius="lg"
                                            rightIcon={
                                                <img
                                                    alt=""
                                                    src="/icons/chevrons-right.svg"
                                                />
                                            }
                                        >
                                            <Text
                                                weight={700}
                                                size="lg"
                                                color="yellow"
                                            >
                                                Details
                                            </Text>
                                        </Button>
                                    </>
                                )}
                            </div>
                        </div>
                    </div>
                </Container>
            </BackgroundImage>
        </Box>
    );
};
