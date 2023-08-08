# Use an official NGINX image as the base image
FROM nginx

# Remove the default NGINX configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom NGINX configuration file
COPY default.conf /etc/nginx/conf.d/