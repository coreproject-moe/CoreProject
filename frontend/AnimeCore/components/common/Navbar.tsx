import { createStyles, Grid } from '@mantine/core';

const useStyles = createStyles((theme) => ({
    grid: {
        paddingLeft: theme.spacing.xl * 3,
        paddingRight: theme.spacing.xl * 2,
    },
    profile: {
        display: 'flex',
        justifyContent: 'flex-end',
    },
    avatar: {
        cursor: 'pointer',
    },
    logo: {
        display: 'flex',
        justifyContent: 'center',
    },

    search: {
        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
}));

export const Navbar = () => {
    const { classes } = useStyles();
    return (
        <Grid justify="space-between" className={classes.grid} grow>
            <Grid.Col span={4}>
                <img
                    className={classes.search}
                    alt=""
                    src="/icons/search.svg"
                    width={30}
                    height={30}
                />
            </Grid.Col>
            <Grid.Col span={4} className={classes.logo}>
                <img
                    alt=""
                    src="/logos/animecore_logo.svg"
                    width={158}
                    height={22}
                />
            </Grid.Col>
            <Grid.Col span={4} className={classes.profile}>
                <img
                    className={classes.avatar}
                    alt=""
                    src="/images/placeholder.png"
                    width={50}
                    height={50}
                />
            </Grid.Col>
        </Grid>
    );
};
