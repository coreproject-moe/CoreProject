export const truncate = (str: string, num: number) => {
    if (num > str.length) {
        return str;
    } else {
        str = str.substring(0, num);
        return str + "...";
    }
};
