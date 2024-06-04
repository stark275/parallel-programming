FROM mysql:8.0-debian

RUN rm -rf /var/lib/mysql
RUN mkdir /var/lib/mysql

# Définir lower_case_table_names=1
RUN echo "[mysqld]" >> /etc/mysql/my.cnf
RUN echo "lower_case_table_names=1" >> /etc/mysql/my.cnf
RUN echo "bind-address = 0.0.0.0" >> /etc/mysql/my.cnf


RUN mysqld --defaults-file=/etc/mysql/my.cnf --initialize --lower_case_table_names=1 --user=mysql --console

# Exécuter mysqld
CMD ["mysqld"]

EXPOSE 3306