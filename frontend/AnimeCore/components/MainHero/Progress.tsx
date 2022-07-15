import { Progress } from '@mantine/core';
import {
    forwardRef,
    ForwardRefRenderFunction,
    memo,
    useEffect,
    useImperativeHandle,
} from 'react';
import { useSwiper } from 'swiper/react';
import { useCountdownTimer } from 'use-countdown-timer';

// Thanks Stackoverflow
// https://stackoverflow.com/questions/62210286/declare-type-with-react-useimperativehandle

type MainHeroProgressProps = {};

type MainHeroProgressHandle = {
    pause: () => Promise<void>;
    start: () => Promise<void>;
    reset: () => Promise<void>;
};

const MainHeroProgress: ForwardRefRenderFunction<
    MainHeroProgressHandle,
    MainHeroProgressProps
> = (props, ref) => {
    const SWIPER_DELAY = 10 * 1000;
    const swiper = useSwiper();

    const { countdown, isRunning, start, reset, pause } = useCountdownTimer({
        timer: SWIPER_DELAY,
        interval: 800,
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
            setTimeout(() => {
                pause();
            }, 100);
        },
        start: async () => {
            setTimeout(() => {
                if (isRunning) {
                    return;
                }
                start();
            }, 1000);
        },

        reset: async () => {
            reset();
        },
    }));

    return (
        <Progress
            aria-label="Next slide progress"
            sx={() => ({ width: 100 })}
            mr="xl"
            color="yellow"
            value={(100 / SWIPER_DELAY) * (SWIPER_DELAY - countdown)}
        />
    );
};

export default memo(forwardRef(MainHeroProgress));
