export class UrlMaps {
    public DOMAIN = 'https://backend.coreproject.moe';
    private BASE_URL = this.DOMAIN + '/api/v1';

    public anime = () => {
        return `${this.BASE_URL}/anime`;
    };

    public id = (id: number | string) => {
        return `${this.BASE_URL}/anime/${id}`;
    };

    public mal_id = (id: number | string) => {
        return `${this.BASE_URL}/anime?mal_id=${id}`;
    };

    public kitsu_id = (id: number | string) => {
        return `${this.BASE_URL}/anime?kitsu_id=${id}`;
    };

    public anilist_id = (id: number | string) => {
        return `${this.BASE_URL}/anime?anilist_id=${id}`;
    };

    public genre = (id: number | string) => {
        return `${this.BASE_URL}/anime/${id}/genres`;
    };

    public episode = (id: number | string) => {
        return `${this.BASE_URL}/anime/${id}/episodes`;
    };

    public episode_number = (
        anime_id: number | string,
        episode_number: number | string
    ) => {
        return `${this.BASE_URL}/anime/${anime_id}/episodes/${episode_number}`;
    };

    public get media_url() {
        return `${this.DOMAIN}/media`;
    }

    public user_info = () => {
        return `${this.BASE_URL}/user/`;
    };

    public signup = () => {
        return `${this.BASE_URL}/user/signup`;
    };

    public login = () => {
        return `${this.BASE_URL}/user/login`;
    };

    public username_validity = () => {
        return `${this.BASE_URL}/user/username_validity`;
    };

    // Feeds
    public anime_feed = () => {
        return `${this.DOMAIN}/feed/anime/`;
    };
    public character_feed = () => {
        return `${this.DOMAIN}/feed/character/`;
    };
    public staff_feed = () => {
        return `${this.DOMAIN}/feed/staff/`;
    };
    public producer_feed = () => {
        return `${this.DOMAIN}/feed/producer/`;
    };
}
