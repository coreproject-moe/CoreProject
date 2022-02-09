import { baseUrl } from './baseUrl';

/*
    User login endpoint
    Example = 127.0.0.1:8000/authentication/login/
*/
export const loginPageUrl = `${baseUrl}/authentication/login/`;

/*
    User login endpoint
    Example = 127.0.0.1:8000/authentication/logout/
*/
export const logoutPageUrl = `${baseUrl}/authentication/logout/`;

/*
    User Signup endpoint
    Example = http://127.0.0.1:8000/authentication/register/
*/

export const signupPageUrl = `${baseUrl}/authentication/register/`;

/* 
    User Edit Info Page
    Example = http://127.0.0.1:8000/user/edit_info/
*/
export const userEditInfoPageUrl = `${baseUrl}/user/edit_info/`;
