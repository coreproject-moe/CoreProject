import type { NextPage } from 'next';
import { MainHero } from '../components/swiper/MainHero';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, EffectFade, Mousewheel, Navigation } from 'swiper';

const Home: NextPage = () => {
    return (
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
                    modules={[EffectFade, Autoplay, Navigation]}
                    navigation={{
                        nextEl: '.mainhero__next__el',
                        prevEl: '.mainhero__previous__el',
                    }}
                    effect="fade"
                    direction="horizontal"
                    simulateTouch={false}
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
    );
};

export default Home;
