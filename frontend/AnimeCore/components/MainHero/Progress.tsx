import { Progress } from '@mantine/core';
import { forwardRef, memo, useEffect, useImperativeHandle } from 'react';
import { useSwiper } from 'swiper/react';
import { useCountdownTimer } from 'use-countdown-timer';

const MainHeroProgress = forwardRef(function MainHeroProgress(props, ref) {
    const SWIPER_DELAY = 10 * 1000;
    const swiper = useSwiper();

    const { countdown, start, reset, pause } = useCountdownTimer({
        timer: SWIPER_DELAY,
        interval: 400,
        autostart: true,
        onExpire: () => {
            swiper?.slideNext();
        },
    });

    useEffect(() => {
        reset();
    }, [reset]);

    useImperativeHandle(ref, () => ({
        pause: async () => {
            pause();
        },
        start: async () => {
            start();
        },

        reset: async () => {
            reset();
        },
    }));

    return (
        <Progress
            sx={() => ({ width: 100 })}
            mr="xl"
            color="yellow"
            value={(100 / SWIPER_DELAY) * (SWIPER_DELAY - countdown)}
        />
    );
});

export default memo(MainHeroProgress);
