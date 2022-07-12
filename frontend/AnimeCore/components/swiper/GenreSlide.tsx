import {
    Badge,
    Container,
    createStyles,
    Divider,
    Group,
    Input,
    SimpleGrid,
    Text,
    Title,
    useMantineTheme,
} from '@mantine/core';
import { memo } from 'react';

const useStyles = createStyles((theme) => ({
    root: {
        minHeight: '100vh',

        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },

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

    const badgeData = [
        { name: 'Action', color: theme.colors.blue[4] },
        { name: 'Adventure', color: theme.colors.red[4] },
        { name: 'Comedy', color: theme.colors.yellow[6] },
        { name: 'Drama', color: theme.colors.green[5] },
        { name: 'Ecchi', color: theme.colors.green[5] },
        { name: 'Fantasy', color: theme.colors.blue[4] },
        { name: 'Horror', color: theme.colors.red[4] },
        { name: 'Mahou Shoujo', color: theme.colors.red[3] },
        { name: 'Mecha', color: theme.colors.orange[3] },
        { name: 'Music', color: theme.colors.cyan[5] },
        { name: 'Mystery', color: theme.colors.yellow[5] },
        { name: 'Psychological', color: theme.colors.red[6] },
        { name: 'Romance', color: theme.colors.red[5] },
        { name: 'Sci-Fi', color: theme.colors.green[5] },
        { name: 'Slice of Life', color: theme.colors.yellow[5] },
        { name: 'Sports', color: theme.colors.red[8] },
        { name: 'Supernatural', color: theme.colors.cyan[8] },
        { name: 'Thriller', color: theme.colors.green[5] },
    ];

    return (
        <div
            className={classes.root}
            style={{ backgroundColor: theme.colors.blue[9] }}
        >
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
                                color: theme.black,
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
                        {badgeData.map((item, index) => {
                            return (
                                <Badge
                                    key={index}
                                    className={classes.badges}
                                    size="xl"
                                    style={{
                                        backgroundColor: item.color,
                                    }}
                                    variant="filled"
                                    radius="md"
                                >
                                    <Text color={theme.black}>{item.name}</Text>
                                </Badge>
                            );
                        })}
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

export default memo(GenreSlide);
