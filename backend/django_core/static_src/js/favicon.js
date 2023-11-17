import svg from '../images/favicon/favicon.svg?raw';

let link = document.querySelector("link[rel~='icon']");
if (!link) {
    link = document.createElement('link');
    link.rel = 'shortcut icon';
    document.head.appendChild(link);
}
// https://stackoverflow.com/a/75832198
link.href = `data:image/svg+xml,${svg
    .replace(/\"/g, '%22')
    .replace(/\#/g, '%23')}`;
