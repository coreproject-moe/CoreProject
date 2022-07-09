import {
    Container,
    createStyles,
    Divider,
    Input,
    Text,
    Title,
    SimpleGrid,
    useMantineTheme,
    Badge,
    Group,
} from '@mantine/core';
import React from 'react';

const useStyles = createStyles((theme) => ({
    wrapper: {
        paddingTop: theme.spacing.xl * 3,
        paddingLeft: theme.spacing.xl * 4,
        paddingRight: theme.spacing.xl * 4,

        [theme.fn.smallerThan('md')]: {
            paddingLeft: theme.spacing.sm * 2,
            paddingRight: theme.spacing.sm * 2,
        },
    },

    inner: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
    },

    dots: {
        position: 'absolute',
        color:
            theme.colorScheme === 'dark'
                ? theme.colors.dark[5]
                : theme.colors.gray[1],

        '@media (max-width: 755px)': {
            display: 'none',
        },
    },

    dotsLeft: {
        left: 0,
        top: 0,
    },

    title: {
        textAlign: 'center',
        fontWeight: 800,
        fontSize: 40,
        letterSpacing: -1,
        color: theme.colorScheme === 'dark' ? theme.white : theme.black,
        marginBottom: theme.spacing.xs,
        fontFamily: `Greycliff CF, ${theme.fontFamily}`,

        '@media (max-width: 520px)': {
            fontSize: 28,
            textAlign: 'left',
        },
    },

    description: {
        textAlign: 'center',

        '@media (max-width: 520px)': {
            textAlign: 'left',
            fontSize: theme.fontSizes.md,
        },
    },

    controls: {
        marginTop: theme.spacing.lg,
        display: 'flex',
        justifyContent: 'center',

        '@media (max-width: 520px)': {
            flexDirection: 'column',
        },
    },

    control: {
        '&:not(:first-of-type)': {
            marginLeft: theme.spacing.md,
        },

        '@media (max-width: 520px)': {
            height: 42,
            fontSize: theme.fontSizes.md,

            '&:not(:first-of-type)': {
                marginTop: theme.spacing.md,
                marginLeft: 0,
            },
        },
    },
    badges: {
        cursor: 'pointer',
        textTransform: 'capitalize',
        height: 45,
    },
}));

const GenreSlide = () => {
    const { classes } = useStyles();
    const theme = useMantineTheme();

    return (
        <div className="hero" style={{ backgroundColor: theme.colors.blue[9] }}>
            <Container className={classes.wrapper} size={1400}>
                <div className={classes.inner}>
                    <Input
                        width={600}
                        styles={{
                            wrapper: {
                                width: '80vh',
                            },
                            input: {
                                height: 80,
                                borderRadius: 14,
                                borderColor: '#FF7081',
                                borderWidth: 4,
                                alignSelf: 'center',
                                backgroundColor: 'white',
                            },
                        }}
                        icon={
                            <img
                                src="/icons/search-red.svg"
                                alt=""
                                height={36}
                                width={36}
                            />
                        }
                        variant="unstyled"
                        placeholder="Search for anything"
                        radius="lg"
                        size="xl"
                    />

                    <Divider
                        mt="xl"
                        label={<Text size="sm">or search by genres</Text>}
                        labelPosition="center"
                        size="md"
                        sx={{ width: 300 }}
                    />
                    <SimpleGrid
                        mt="xl"
                        cols={6}
                        spacing={40}
                        sx={{ justifyItems: 'center' }}
                    >
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.blue[4],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Action</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.red[4],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Adventure</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.yellow[6],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Comedy</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.green[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Drama</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.green[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Ecchi</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.blue[4],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Fantasy</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.red[4],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Horror</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.red[3],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Mahou Shoujo</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.orange[3],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Mecha</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.cyan[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Music</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.yellow[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Mystery</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.red[6],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Psychological</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.red[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Romance</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.green[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Sci-Fi</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.yellow[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Slice of Life</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.red[8],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Sports</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.cyan[8],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Supernatural</Text>
                        </Badge>
                        <Badge
                            className={classes.badges}
                            size="xl"
                            sx={(theme) => ({
                                backgroundColor: theme.colors.green[5],
                            })}
                            variant="filled"
                            radius="md"
                        >
                            <Text color={theme.black}>Thriller</Text>
                        </Badge>
                    </SimpleGrid>
                    <Title mt="lg" order={3}>
                        Choose your preferences
                    </Title>
                    <Text align="center" sx={{ maxWidth: 528 }}>
                        Choose some options to customize your experience. You
                        can change them anytime by clicking the profile icon and
                        going to Settings
                    </Text>
                    <Group mt="lg">
                        <Text>Label</Text>
                        <Divider
                            sx={{ height: '24px' }}
                            orientation="vertical"
                        />
                        <Text>Label</Text>
                        <Divider
                            sx={{ height: '24px' }}
                            size="sm"
                            orientation="vertical"
                        />
                        <Text>Label</Text>
                        <Divider
                            sx={{ height: '24px' }}
                            size="md"
                            orientation="vertical"
                        />
                        <Text>Label</Text>
                        <Divider
                            sx={{ height: '24px' }}
                            size="lg"
                            orientation="vertical"
                        />
                        <Text>Label</Text>
                        <Divider
                            sx={{ height: '24px' }}
                            size="xl"
                            orientation="vertical"
                        />
                        <Text>Label</Text>
                    </Group>
                </div>
            </Container>
        </div>
    );
};

export default GenreSlide;
