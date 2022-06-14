import React from 'react';
import { createStyles, Container, Title, Text, Button } from '@mantine/core';
import { Navbar } from '../common/Navbar';
import { useMediaQuery } from '@mantine/hooks';

const useStyles = createStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: '#11284b',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        paddingTop: theme.spacing.xl * 2,
        paddingBottom: theme.spacing.xl * 2,
        minHeight: '100vh',
        boxShadow: `
            inset 0 4px 1800px rgb(7, 5, 25),
            inset 0 -40vh 140px 2px rgba(7, 5, 25, 0.9),
            inset 0 -15vh 140px 2px rgba(7, 5, 25, 0.7),
            inset 0 -5vh 140px 2px rgba(7, 5, 25, 0.4),
            inset 0 -2vh 140px 2px rgba(7, 5, 25, 0.2)`,

        [theme.fn.smallerThan('md')]: {
            minHeight: '60vh',
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
            paddingLeft: theme.spacing.xl * 2,
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
        color: theme.white,
        fontWeight: 900,
        lineHeight: 1.05,
        maxWidth: 500,
        fontSize: 48,

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
}));

export const MainHero = ({ backgroundImage = '', backgroundBanner = '' }) => {
    const { classes } = useStyles();
    const mobile = useMediaQuery('(min-width: 500px)');

    return (
        <div
            className={classes.root}
            style={{
                backgroundImage: `url('${backgroundImage}')`,
            }}
        >
            <Navbar />

            <Container size="lg" className={classes.container}>
                <div className={classes.inner}>
                    <div className={classes.content}>
                        <Title className={classes.title}>
                            A{' '}
                            <Text
                                component="span"
                                inherit
                                variant="gradient"
                                gradient={{ from: 'pink', to: 'yellow' }}
                            >
                                fully featured
                            </Text>{' '}
                            React components library
                        </Title>

                        <Text className={classes.description} mt={30}>
                            Build fully functional accessible web applications
                            with ease – Mantine includes more than 100
                            customizable components and hooks to cover you in
                            any situation
                        </Text>

                        <Button
                            variant="gradient"
                            gradient={{ from: 'pink', to: 'yellow' }}
                            size="xl"
                            className={classes.control}
                            mt={40}
                        >
                            Get started
                        </Button>
                    </div>
                </div>
            </Container>
        </div>
    );
};
