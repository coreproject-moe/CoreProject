// https://youmightnotneed.com/lodash#uniqBy
const uniqBy = (arr: Array<any>, iteratee: any) => {
    if (typeof iteratee === "string") {
        const prop = iteratee;
        iteratee = (item) => item[prop];
    }

    return arr.filter((x, i, self) => i === self.findIndex((y) => iteratee(x) === iteratee(y)));
};
