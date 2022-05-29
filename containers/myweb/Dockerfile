FROM ubuntu
RUN apt update
RUN apt install -y apache2
# note that the next line has a mistake
COPY index.html /vvar/www/html/
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]