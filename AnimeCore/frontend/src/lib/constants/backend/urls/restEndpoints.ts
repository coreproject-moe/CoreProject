import { baseUrl } from "./baseUrl";

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
export const userInfoUrl = `${baseUrl}/api/v1/user/info/`;

/*
    Capture Endpoint (JSON)
    Example = http://127.0.0.1:8000/api/v1/register/

*/
export const registerEndpoint = `${baseUrl}/api/v1/user/register/`;

/*
    Anime Info Endpoint (JSON)
    Example = http://127.0.0.1:8000/api/v1/upload/anime/1/    
*/
export const animeInfoEndpoint = `${baseUrl}/api/v1/upload/anime/`;

/*
    Anime Info Endpoint (JSON)
    Example = http://127.0.0.1:8000/api/v1/upload/anime/random
        Query = Limit  
*/
export const randomAnimeInfoEndpoint = `${baseUrl}/api/v1/upload/anime/random/`;
