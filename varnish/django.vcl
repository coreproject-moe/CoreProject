vcl 4.1;

backend default {
    .host = "django";
    .port = "8000";
}



# https://github.com/nonamenix/django-varnish/blob/3a63f08b0f1d49901cfdfead07565e7b989d4fc8/varnish.vcl
sub vcl_recv {
    unset req.http.Accept-Encoding;
    unset req.http.User-Agent;



    // Session
    if (req.http.Cookie ~ "sessionid") {
        set req.http.x-sessionid = regsub(req.http.Cookie,"^.*?sessionid=([^;]*);*.*$" , "\1");
    }
    // CSRF
    if (req.http.Cookie ~ "csrftoken") {
        set req.http.x-sessionid = regsub(req.http.Cookie,"^.*?csrftoken=([^;]*);*.*$" , "\1");
    }

    // Language
    if (req.http.Cookie ~ "hlang=") {
        set req.http.x-lang = regsub(req.http.Cookie,"^.*?hlang=([^;]*);*.*$" , "\1");
    } else {
        if (req.http.Accept-Language) {
            set req.http.x-lang = req.http.Accept-Language;
        } else {
            set req.http.x-lang = "en";
        }
    }

    // Cleaning
    if (req.http.Cookie == "") {
        unset req.http.Cookie;
    }

}

sub vcl_backend_response {
    set beresp.http.x-url = bereq.url;

    // Allow esi includes for pages
    set beresp.do_esi = true;

    // If no cache
    if (beresp.ttl <= 0s) {
        set beresp.ttl = 10s;
    }

    // Set small cache for 403, 404, 5xx responses
    if (beresp.status == 403 || beresp.status == 404 || beresp.status >= 500) {
    	set beresp.ttl = 3s;
    }

}

sub vcl_deliver {
	unset resp.http.x-url;
}
