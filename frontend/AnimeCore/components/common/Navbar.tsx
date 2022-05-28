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
}));

export const Navbar = () => {
    const { classes } = useStyles();
    return (
        <Grid justify="space-between" className={classes.grid}>
            <Grid.Col span={4}>
                <img
                    alt=""
                    src="/logos/animecore_logo.svg"
                    width={164}
                    height={25}
                />
            </Grid.Col>
            <Grid.Col span={4} className={classes.profile}>
                <img
                    className={classes.avatar}
                    alt=""
                    src="/images/placeholder.png"
                    width={60}
                    height={60}
                />
            </Grid.Col>
        </Grid>
    );
};
