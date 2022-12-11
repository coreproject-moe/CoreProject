import { browser } from '$app/environment';

export class UrlMaps {
	private django = browser ? window?.django : undefined;

	private get is_django_used_for_rendering() {
		if (!this.django) {
			return undefined;
		}
		if (this.django.DEBUG == `{{ debug|yesno:'true,false' }}`) {
			return false;
		} else if (this.django.DEBUG == 'true' || this.django.DEBUG == 'false') {
			return true;
		} else {
			return null;
		}
	}
	private get api_root() {
		return this.is_django_used_for_rendering ? '' : 'http://127.0.0.1:8003';
	}

	public get signup_url() {
		if (this.is_django_used_for_rendering) {
			return this.api_root + window?.django.URLS.SIGNUP;
		} else {
			return this.api_root + '/api/v1/user/sign_up';
		}
	}
}
