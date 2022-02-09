import { baseUrl } from './baseUrl';

/*
    Avatar endpoint
    Example = http://127.0.0.1:8000/api/v1/avatar/1/
*/
export const avatarUrl = `${baseUrl}/api/v1/avatar`;

/* 
    Token obtain endpoint
    Example = http://127.0.0.1:8000/api/v1/token/
*/
export const tokenObtainUrl = `${baseUrl}/api/v1/token/`;

/* 
    Token refresh endpoint
    Example = http://127.0.0.1:8000/api/v1/token/refresh/
*/
export const tokenRefreshUrl = `${baseUrl}/api/v1/token/refresh/`;

/* 
    Token blacklist endpoint
    Example = http://127.0.0.1:8000/api/v1/token/blacklist/
*/
export const tokenBlacklistUrl = `${baseUrl}/api/v1/token/blacklist/`;

/*
    User Info endpoint (JSON)
    Example = http://127.0.0.1:8000/api/v1/users/info/
*/
export const userInfoUrl = `${baseUrl}/api/v1/users/info/`;
