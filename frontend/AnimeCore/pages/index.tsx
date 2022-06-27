import type { NextPage } from 'next';
import { MainHero } from '../components/swiper/MainHero';
import type { Swiper as SwiperType } from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/react';
import {
    Autoplay,
    EffectFade,
    Mousewheel,
    Navigation,
    Pagination as SwiperPagination,
} from 'swiper';
import { Progress, Grid, Title, Text, ActionIcon } from '@mantine/core';
import { useState } from 'react';

const Home: NextPage = () => {
    const [swiper, setSwiper] = useState<SwiperType | null>(null);
    const [mainHeroSwiper, setMainHeroSwiper] = useState<SwiperType | null>(
        null
    );
    const [mainHeroSwiperActiveIndex, setMainHeroSwiperActiveIndex] =
        useState<number>(0);

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
                onSwiper={setSwiper}
            >
                <SwiperSlide>
                    <Swiper
                        modules={[
                            EffectFade,
                            Autoplay,
                            Navigation,
                            SwiperPagination,
                        ]}
                        effect="fade"
                        direction="horizontal"
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
                        onSwiper={setMainHeroSwiper}
                        onSlideChange={(swiper) => {
                            setMainHeroSwiperActiveIndex(swiper.realIndex);
                        }}
                    >
                        {Array(10)
                            .fill(1)
                            .map((el, i) => {
                                return (
                                    <SwiperSlide key={i}>
                                        <MainHero
                                            key={i}
                                            swiper={swiper}
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
                    minHeight: '10vh',
                    backgroundColor: 'rgb(7, 5, 25)',
                    display: 'flex',
                })}
            >
                <Grid
                    grow
                    justify="space-between"
                    align="center"
                    sx={() => ({
                        height: '100%',
                        width: '100%',
                    })}
                >
                    <Grid.Col
                        span={4}
                        sx={(theme) => ({
                            [theme.fn.smallerThan('md')]: {
                                display: 'none',
                            },
                        })}
                    />
                    <Grid.Col
                        span={4}
                        sx={() => ({
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            height: '10vh',
                            flexDirection: 'row',
                        })}
                    >
                        <Progress
                            sx={() => ({ width: 100 })}
                            color="yellow"
                            value={
                                (100 / (mainHeroSwiper?.slides?.length ?? 0) +
                                    1) *
                                mainHeroSwiperActiveIndex
                            }
                        />
                        <div
                            style={{
                                display: 'flex',
                                justifyContent: 'center',
                                width: 270,
                            }}
                            className="swiper__mainhero__pagination"
                        ></div>
                        <ActionIcon
                            color="yellow"
                            size="lg"
                            radius="xl"
                            variant="filled"
                            onClick={() => {
                                mainHeroSwiper?.slidePrev();
                            }}
                        >
                            <img src="icons/chevron-left-black.svg" />
                        </ActionIcon>
                        <ActionIcon
                            color="yellow"
                            size="lg"
                            radius="xl"
                            variant="filled"
                            ml="xl"
                            onClick={() => {
                                mainHeroSwiper?.slideNext();
                            }}
                        >
                            <img src="icons/chevron-right-black.svg" />
                        </ActionIcon>
                    </Grid.Col>
                    <Grid.Col
                        span={4}
                        sx={(theme) => ({
                            display: 'flex',
                            justifyContent: 'flex-end',

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
