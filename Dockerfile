FROM python:3.4

#RUN groupadd -r django && useradd -r -g django django

WORKDIR /project

RUN apt-get update \
&& apt-get install apache2 -y\
&& apt-get install libapache2-mod-wsgi-py3 -y \
&& apt-get install sudo -y \
&& apt-get install git-core -y \
&& a2enmod wsgi \
&& git config --global user.name = "container" \
&& git config --global user.email = "teamdk@dk.com"


COPY dkpay.conf /etc/apache2/sites-available/
RUN a2dissite 000-default.conf
RUN a2ensite dkpay.conf

COPY project /project
RUN pip install -r requirements.txt

EXPOSE 8000 80
#USER django

CMD apache2ctl -D FOREGROUND

#CMD ["/bin/bash"]
