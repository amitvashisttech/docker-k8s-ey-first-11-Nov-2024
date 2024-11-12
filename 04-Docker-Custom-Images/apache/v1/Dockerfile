# Base Image 
FROM ubuntu:noble

# Owner of the Image 
MAINTAINER Amit Vashist <amitvashist7@outlook.com>

# Update APT Repo 
RUN apt-get update 

# Install Apache2 Packages from APT Default Repo 
RUN apt-get install apache2 -y 

# Execute the Service 
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND" ]
