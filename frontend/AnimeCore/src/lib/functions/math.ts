export const round_to_nearest_zero_point_five = (rating: number): number => {
    return Number((Math.round(rating * 2) / 2).toFixed(1));
};
