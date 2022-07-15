import { createStyles, Grid } from '@mantine/core';
import { memo } from 'react';

const useStyles = createStyles((theme) => ({
    grid: {
        paddingLeft: theme.spacing.xl * 3,
        paddingRight: theme.spacing.xl * 2,

        [theme.fn.smallerThan('md')]: {
            paddingLeft: theme.spacing.sm * 2,
            paddingRight: theme.spacing.sm * 2,
        },
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
        display: 'flex',
        alignItems: 'center',

        [theme.fn.smallerThan('md')]: {
            display: 'none',
        },
    },
}));

const Navbar = () => {
    const { classes } = useStyles();

    return (
        <Grid justify="space-between" className={classes.grid} grow>
            <Grid.Col span={4} className={classes.search}>
                <img alt="" src="/icons/search.svg" width={30} height={30} />
            </Grid.Col>
            <Grid.Col span={4} className={classes.logo}>
                <img
                    alt=""
                    src={'/logos/animecore_logo.svg'}
                    width={158}
                    height={22}
                />
                <img
                    style={{
                        transform: 'translateY(5px)',
                        color: '#AFAFAF',
                    }}
                    alt=""
                    src="/icons/chevron-down.svg"
                    width={20}
                    height={20}
                />
            </Grid.Col>
            <Grid.Col span={4} className={classes.profile}>
                <img
                    className={classes.avatar}
                    alt=""
                    src="/images/(Avatar)-placeholder.png"
                    width={50}
                    height={50}
                />
            </Grid.Col>
        </Grid>
    );
};
export default memo(Navbar);
