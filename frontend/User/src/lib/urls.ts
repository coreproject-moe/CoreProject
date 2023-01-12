export class UrlMaps {
	private get api_root() {
		return process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:8000' : '';
	}

	public get signup_url() {
		return this.api_root + '/api/v1/user/sign_up';
	}

	public get login_url() {
		return this.api_root + '/api/v1/user/login';
	}
}
