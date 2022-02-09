// Main endpoint url
export const baseUrl = 'http://127.0.0.1:8000';

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

/*
    User login endpoint
    Example = 127.0.0.1:8000/authentication/login/
*/
export const loginUrl = `${baseUrl}/authentication/login/`;

/*
    User login endpoint
    Example = 127.0.0.1:8000/authentication/logout/
*/
export const logoutUrl = `${baseUrl}/authentication/logout/`;

/*
    User Signup endpoint
    Example = http://127.0.0.1:8000/authentication/register/
*/

export const signupUrl = `${baseUrl}/authentication/register/`;

/* 
    User Edit Info Page
    Example = http://127.0.0.1:8000/user/edit_info/
*/
export const userEditInfoUrl = `${baseUrl}/user/edit_info/`;
