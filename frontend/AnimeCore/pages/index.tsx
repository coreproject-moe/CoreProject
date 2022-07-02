import { showNotification } from '@mantine/notifications';
import type { NextPage } from 'next';
import { useEffect, useState } from 'react';
import type { Swiper as SwiperType } from 'swiper';
import {
    Autoplay,
    EffectFade,
    Mousewheel,
    Navigation,
    Pagination as SwiperPagination,
} from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/react';
import { useCountdownTimer } from 'use-countdown-timer';

import { MainHero } from '@/components/swiper/MainHero';

const data = [
    {
        animeStudio: 'Kyoto Animations',
        animeTitle: 'Hyouka',
        animeAirTime: 'Spring 2012',
        animeEpisodeCount: 22,
        animeSummary: `High school freshman Houtarou Oreki has but one goal:High school freshman Houtarou Oreki has but one goal: to lead a gray life while conserving as much energy as he can. Unfortunately, his peaceful days come to an end when his older sister, Tomoe, forces him to save the memberless Classics Club from disbandment.\n\nLuckily, Oreki's predicament seems to be over when he heads to the clubroom and discovers that his fellow first-year, Eru Chitanda, has already become a member. However, despite his obligation being fulfilled, Oreki finds himself entangled by Chitanda's curious and bubbly personality, soon joining the club of his own volition.\n\nHyouka follows the four members of the Classics Club—including Oreki's friends Satoshi Fukube and Mayaka Ibara—as they, driven by Chitanda's insatiable curiosity, solve the trivial yet intriguing mysteries that permeate their daily lives.`,
        backgroundImage: '/images/Hyouka-poster.png',
        backgroundBanner:
            'https://media.kitsu.io/anime/poster_images/6686/large.jpg',
    },
    {
        animeStudio: 'Studio DEEN',
        animeTitle: 'KonoSuba',
        animeAirTime: 'Spring 2012',
        animeEpisodeCount: 10,
        animeSummary: `After dying a laughable and pathetic death on his way back from buying a game, high school student and recluse Kazuma Satou finds himself sitting before a beautiful but obnoxious goddess named Aqua. She provides the NEET with two options: continue on to heaven or reincarnate in every gamer's dream—a real fantasy world! Choosing to start a new life, Kazuma is quickly tasked with defeating a Demon King who is terrorizing villages. But before he goes, he can choose one item of any kind to aid him in his quest, and the future hero selects Aqua. But Kazuma has made a grave mistake—Aqua is completely useless!\n\nUnfortunately, their troubles don't end here; it turns out that living in such a world is far different from how it plays out in a game. Instead of going on a thrilling adventure, the duo must first work to pay for their living expenses. Indeed, their misfortunes have only just begun!`,
        backgroundImage: '/images/Konosuba-poster.jpg',
        backgroundBanner:
            'https://media.kitsu.io/anime/poster_images/10941/large.jpg',
    },
    {
        animeEpisodeCount: 13,
        animeStudio: 'Polygon Pictures',
        animeAirTime: 'Winter 2016',
        animeTitle: 'Ajin',
        animeSummary: `Mysterious immortal humans known as "Ajin" first appeared 17 years ago in Africa. Upon their discovery, they were labeled as a threat to mankind, as they might use their powers for evil and were incapable of being destroyed. Since then, whenever an Ajin is found within society, they are to be arrested and taken into custody immediately.\n\nStudying hard to become a doctor, Kei Nagai is a high schooler who knows very little about Ajin, only having seen them appear in the news every now and then. Students are taught that these creatures are not considered to be human, but Kei doesn't pay much attention in class. As a result, his perilously little grasp on this subject proves to be completely irrelevant when he survives an accident that was supposed to claim his life, signaling his rebirth as an Ajin and the start of his days of torment. However, as he finds himself alone on the run from the entire world, Kei soon realizes that more of his species may be a lot closer than he thinks.`,
        backgroundImage: '/images/Ajin-poster.jpg',
        backgroundBanner:
            'https://media.kitsu.io/anime/poster_images/11368/large.jpg',
    },
];

const Home: NextPage = () => {
    const SWIPER_DELAY = 5 * 1000; // Miliseconds

    const [swiper, setSwiper] = useState<SwiperType | null>(null);
    const [mainHeroSwiper, setMainHeroSwiper] = useState<SwiperType | null>(
        null
    );
    const [sliderProgress, setSliderProgress] = useState<number>(0);

    // Expire after 10 seconds
    const { countdown, start, reset, pause } = useCountdownTimer({
        timer: SWIPER_DELAY,
        interval: 200,
        autostart: true,
        onExpire: () => {
            mainHeroSwiper?.slideNext();
        },
    });
    useEffect(() => {
        const value = Math.round(
            (100 / SWIPER_DELAY) * (SWIPER_DELAY - countdown)
        );
        setSliderProgress(value);
    }, [SWIPER_DELAY, countdown]);

    useEffect(() => {
        setTimeout(() => {
            showNotification({
                title: 'This site is still WIP',
                message: `Thanks for visiting AnimeCore.This site is still a work in-progress,so there's quite a bit of limited functionality.Feel free to check us over at Github - https://github.com/baseplate-admin/coreProject`,
                styles: (theme) => ({
                    root: {
                        '&::before': { backgroundColor: theme.colors.blue[4] },
                    },
                }),
            });
        });
    }, []);

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
                        navigation={{
                            nextEl: '.mainhero__next__el',
                            prevEl: '.mainhero__previous__el',
                        }}
                        pagination={{
                            enabled: true,
                            el: '.swiper__mainhero__pagination',
                        }}
                        onInit={() => {
                            // Start
                            start();
                        }}
                        loop
                        onSwiper={setMainHeroSwiper}
                        onSlideChange={() => {
                            // Restart
                            reset();
                            start();
                        }}
                    >
                        {data.map((item, index) => {
                            return (
                                <>
                                    <SwiperSlide key={index}>
                                        <MainHero
                                            animeTitle={item.animeTitle}
                                            animeSummary={item.animeSummary}
                                            animeEpisodeCount={
                                                item.animeEpisodeCount
                                            }
                                            animeStudio={item.animeStudio}
                                            animeAirTime={item.animeAirTime}
                                            backgroundImage={
                                                item.backgroundImage
                                            }
                                            backgroundBanner={
                                                item.backgroundBanner
                                            }
                                            pause={pause}
                                            start={start}
                                            swiper={swiper}
                                            sliderProgress={sliderProgress}
                                            mainHeroSwiper={mainHeroSwiper}
                                        />
                                    </SwiperSlide>
                                </>
                            );
                        })}
                    </Swiper>
                </SwiperSlide>
                {/* <SwiperSlide>
                    <div className="hero">

                    </div>
                </SwiperSlide> */}
            </Swiper>
        </>
    );
};

export default Home;
