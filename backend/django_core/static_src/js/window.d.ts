import { ZxcvbnResult } from '@zxcvbn-ts/core';
import { Timer as EasyTimer } from 'easytimer.js';

declare global {
    interface Window {
        get_password_strength: (password: string) => ZxcvbnResult;
    }
    interface Window {
        timer: EasyTimer;
    }
}
