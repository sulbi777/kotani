FROM nginx:1.23.1-alpine
RUN rm -rf /usr/share/nginx/html/*
# Dalam skenario riil, copy file build SPA Anda kemari

RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx/conf.d
USER nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
