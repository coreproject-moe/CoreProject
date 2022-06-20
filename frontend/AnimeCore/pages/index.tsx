import type { NextPage } from 'next';
import { MainHero } from '../components/swiper/MainHero';
import { Swiper, SwiperSlide } from 'swiper/react';
import {
    Autoplay,
    EffectFade,
    Mousewheel,
    Navigation,
    Pagination as SwiperPagination,
} from 'swiper';
import { Grid, Title, Text, Button } from '@mantine/core';

const Home: NextPage = () => {
    return (
        <>
            <Swiper
                speed={600}
                spaceBetween={0}
                direction="vertical"
                slidesPerView="auto"
                modules={[Mousewheel]}
                mousewheel={{ sensitivity: 0.001 }}
                simulateTouch={false}
            >
                <SwiperSlide>
                    <Swiper
                        modules={[
                            EffectFade,
                            Autoplay,
                            Navigation,
                            SwiperPagination,
                        ]}
                        autoplay={{
                            delay: 10 * 1000, // 10 secs ( 1000 to convert it to ms )
                        }}
                        navigation={{
                            nextEl: '.mainhero__next__el',
                            prevEl: '.mainhero__previous__el',
                        }}
                        pagination={{
                            enabled: true,
                            el: '.swiper__mainhero__pagination',
                        }}
                        effect="fade"
                        direction="horizontal"
                    >
                        {Array(10)
                            .fill(1)
                            .map((el, i) => {
                                return (
                                    <SwiperSlide key={i}>
                                        <MainHero backgroundImage="/images/Hyouka-poster.png" />
                                    </SwiperSlide>
                                );
                            })}
                    </Swiper>
                </SwiperSlide>
            </Swiper>
            <Title
                sx={(theme) => ({
                    minHeight: '9vh',
                    backgroundColor: 'rgb(7, 5, 25)',
                    display: 'flex',

                    [theme.fn.smallerThan('md')]: {
                        minHeight: '0vh',
                        display: 'none',
                    },
                })}
            >
                <Grid
                    sx={() => ({
                        width: '100%',
                    })}
                >
                    <Grid.Col
                        span={3}
                        offset={3}
                        sx={() => ({
                            display: 'flex',
                            justifyContent: 'flex-end',
                            alignItems: 'center',
                        })}
                    >
                        <div className="swiper__mainhero__pagination"></div>
                        <Button
                            color="yellow"
                            radius="lg"
                            size="sm"
                            sx={() => ({
                                height: 62,
                                width: 62,
                            })}
                        >
                            <img src="/icons/play.svg" width={24} height={24} />
                        </Button>
                    </Grid.Col>
                    <Grid.Col
                        span={3}
                        offset={3}
                        sx={() => ({
                            display: 'flex',
                            justifyContent: 'flex-end',
                            alignItems: 'center',
                        })}
                    >
                        <img width={24} height={24} src="/icons/mouse.svg" />
                        <Text px="xl" color="white">
                            scroll below
                        </Text>
                    </Grid.Col>
                </Grid>
            </Title>
        </>
    );
};

export default Home;
