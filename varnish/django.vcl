vcl 4.1;

backend default {
    .host = "django";
    .port = "8000";
}

# https://stackoverflow.com/q/19996986
sub vcl_recv {  
  # unless sessionid/csrftoken is in the request, don't pass ANY cookies (referral_source, utm, etc)  
  if (req.request == "GET" && (req.url ~ "^/static" || (req.http.cookie !~ "sessionid" && req.http.cookie !~ "csrftoken" && req.http.cookie !~ "AUTHENTICATION"))) {  
    remove req.http.Cookie;  
  }  

    #normalize accept-encoding to account for different browsers  
    if (req.http.Accept-Encoding) {
        if (req.url ~ "\.(jpg|png|gif|gz|tgz|bz2|tbz|mp3|ogg)$") {
            # No point in compressing these
            remove req.http.Accept-Encoding;
        } elsif (req.http.Accept-Encoding ~ "gzip") {
            set req.http.Accept-Encoding = "gzip";
        } elsif (req.http.Accept-Encoding ~ "deflate") {
            set req.http.Accept-Encoding = "deflate";
        } else {
            # unknown algorithm
            remove req.http.Accept-Encoding;
        }
    }  

}  

sub vcl_fetch {  

  # /static and /media files always cached  
  if (req.url ~ "^/static" || req.url ~ "^/media") {  
       unset beresp.http.set-cookie; 
  }

  if (beresp.http.set-cookie !~ "sessionid" && beresp.http.set-cookie !~ "csrftoken" && beresp.http.set-cookie !~ "AUTHENTICATION") {  
    unset beresp.http.set-cookie;
  }

} 