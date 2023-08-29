

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.a62f5b4f.js","_app/immutable/chunks/scheduler.036c1cd3.js","_app/immutable/chunks/index.a85a8016.js","_app/immutable/chunks/stores.86f882ef.js","_app/immutable/chunks/singletons.bfa8e42f.js","_app/immutable/chunks/index.6af06895.js"];
export const stylesheets = [];
export const fonts = [];
