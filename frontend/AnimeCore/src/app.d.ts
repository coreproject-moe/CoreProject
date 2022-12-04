/// <reference types="@sveltejs/kit" />
/// <reference types="svelte-gestures" />

// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
// and what to do when importing types
declare namespace App {
    // interface Locals {}
    // interface Platform {}
    interface Session {
        authenticated: boolean;
    }
    // interface Stuff {}
}

interface Window {
    django: {
        MEDIA_URL: string;
        CSRFTOKEN: string;
    };
}
