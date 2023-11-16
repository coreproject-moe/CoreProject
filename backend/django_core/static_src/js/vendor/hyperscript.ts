import _hyperscript from 'hyperscript.org';

_hyperscript.processNode(document.body);

document.body.addEventListener('fetch:beforeRequest', (event: any) => {
    event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
});
