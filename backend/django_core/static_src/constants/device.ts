export const DEVICE_STATE = {
    Mobile: "mobile",
    Tablet: "tablet",
    Desktop: "desktop",
} as const;

export type DeviceStateType = typeof DEVICE_STATE[keyof typeof DEVICE_STATE];