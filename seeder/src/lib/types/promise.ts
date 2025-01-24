export type PromiseMethods<T> = {
    [K in keyof T]: T[K] extends (...args: infer A) => infer R
        ? (...args: A) => Promise<Awaited<R>>
        : never;
};
