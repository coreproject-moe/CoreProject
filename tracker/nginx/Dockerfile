FROM nginx:1.23-alpine

# Copy configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80
EXPOSE 5000/udp

# Health check (optional)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]