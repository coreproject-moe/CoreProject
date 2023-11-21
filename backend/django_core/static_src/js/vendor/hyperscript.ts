import _hyperscript from 'hyperscript.org';

declare global {
    interface Window {
        _hyperscript: typeof _hyperscript;
    }
}

_hyperscript.browserInit();
_hyperscript.processNode(document.body);
window._hyperscript = _hyperscript;
