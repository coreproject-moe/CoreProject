import { ZxcvbnResult } from '@zxcvbn-ts/core';
import { Timer as EasyTimer } from 'easytimer.js';
import _hyperscript from 'hyperscript.org';

declare global {
    interface Window {
        get_password_strength: (password: string) => ZxcvbnResult;
        timer: EasyTimer;
        _hyperscript: typeof _hyperscript;
        csrfmiddlewaretoken: string;
        urls: {
            partials: {
                partial_markdown_endpoint: string;
            };
        };
    }
}
