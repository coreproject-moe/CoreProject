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
import { Grid, Title, Text } from '@mantine/core';

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
                            delay: 10 * 1000, // 10 secs
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
                                        <MainHero
                                            key={i}
                                            backgroundImage="/images/Hyouka-poster.png"
                                            backgroundBanner="https://media.kitsu.io/anime/poster_images/6686/large.jpg"
                                        />
                                    </SwiperSlide>
                                );
                            })}
                    </Swiper>
                </SwiperSlide>
            </Swiper>
            <Title
                sx={() => ({
                    minHeight: '9vh',
                    backgroundColor: 'rgb(7, 5, 25)',
                    display: 'flex',
                })}
            >
                <Grid
                    grow
                    sx={() => ({
                        width: '100%',
                    })}
                >
                    <Grid.Col
                        span={3}
                        sx={(theme) => ({
                            display: 'grid',
                            justifyContent: 'flex-end',
                            alignItems: 'center',

                            [theme.fn.smallerThan('md')]: {
                                justifyContent: 'center',
                            },
                        })}
                    >
                        <div className="swiper__mainhero__pagination"></div>
                    </Grid.Col>
                    <Grid.Col
                        span={1}
                        sx={(theme) => ({
                            display: 'flex',
                            justifyContent: 'flex-end',
                            alignItems: 'center',

                            [theme.fn.smallerThan('md')]: {
                                display: 'none',
                            },
                        })}
                    >
                        <img width={24} height={24} src="/icons/mouse.svg" />
                        <Text px="xl" color="gray">
                            scroll below
                        </Text>
                    </Grid.Col>
                </Grid>
            </Title>
        </>
    );
};

export default Home;
