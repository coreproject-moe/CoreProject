

export const index = 10;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/upload/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/10.fac42ecb.js","_app/immutable/chunks/scheduler.036c1cd3.js","_app/immutable/chunks/index.a85a8016.js","_app/immutable/chunks/stores.86f882ef.js","_app/immutable/chunks/singletons.bfa8e42f.js","_app/immutable/chunks/index.6af06895.js","_app/immutable/chunks/opengraph.06ca6f5a.js","_app/immutable/chunks/_commonjsHelpers.de833af9.js","_app/immutable/chunks/fish_mapping.f90195d3.js","_app/immutable/chunks/chevron.a814d82e.js","_app/immutable/chunks/spread.8a54911c.js","_app/immutable/chunks/index.0ccf8626.js","_app/immutable/chunks/create-form.903d409a.js","_app/immutable/chunks/ValidationMessage.9e82644f.js","_app/immutable/chunks/ProgressBar.svelte_svelte_type_style_lang.1b3422c6.js","_app/immutable/chunks/focusTrap.f08ca3d9.js","_app/immutable/chunks/index.429bf755.js","_app/immutable/chunks/lodash.c2eb36b1.js","_app/immutable/chunks/each.3d878967.js","_app/immutable/chunks/cross.691f45c6.js","_app/immutable/chunks/edit.31ecb8d7.js","_app/immutable/chunks/search.855d9ab3.js","_app/immutable/chunks/star.24006a02.js"];
export const stylesheets = ["_app/immutable/assets/ProgressBar.4f1e9ba5.css"];
export const fonts = [];
