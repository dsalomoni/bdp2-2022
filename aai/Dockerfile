FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y apache2 libapache2-mod-auth-openidc
COPY index.html /var/www/html/
COPY default.conf /etc/apache2/sites-enabled/000-default.conf
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]