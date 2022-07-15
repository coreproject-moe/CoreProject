import { Progress } from '@mantine/core';
import {
    forwardRef,
    ForwardRefRenderFunction,
    memo,
    useImperativeHandle,
    useState,
} from 'react';
import { useTimer } from 'react-timer-hook';
import { useSwiper } from 'swiper/react';

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

    const [countdown, setCountdown] = useState<number>(0);

    let timeObject = new Date(Date.now() + SWIPER_DELAY);
    const { seconds, isRunning, start, pause, resume, restart } = useTimer({
        expiryTimestamp: timeObject,
        autoStart: true,
        onExpire: () => {
            swiper.slideNext();
        },
    });

    useImperativeHandle(ref, () => ({
        pause: async () => {
            pause();
        },
        start: async () => {
            isRunning ? resume() : start();
        },
        reset: async () => {
            restart(timeObject, true);
        },
    }));

    return (
        <Progress
            aria-label="Next slide progress"
            sx={() => ({ width: 100 })}
            mr="xl"
            color="yellow"
            value={(SWIPER_DELAY - seconds * 1000) / 100}
        />
    );
};

export default memo(forwardRef(MainHeroProgress));
