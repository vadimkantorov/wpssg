# [WIP] Attempt at using WordPress as a Static Site Generator (SSG

```shell
sudo apt install php-cli php-mysql mysql-server

# download https://wp-cli.org/
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

sudo service mysql start
# create user, password, database
sudo mysql <<< "CREATE USER 'wpssguser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'wpssgpass';"
#sudo mysql <<< "CREATE DATABASE wpssgdb; CREATE USER 'wpssguser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'wpssgpass'; GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON wpssgdb.* TO 'wpssguser'@'localhost';"
sudo mysql <<< "SHOW DATABASES; SELECT user FROM mysql.user;"
# test the local connection to the database
sudo mysql --user=wpssguser --password=wpssgpass --database=wpssgdb <<< "SHOW DATABASES"


# https://make.wordpress.org/cli/handbook/how-to/how-to-install/
php ./wp-cli.phar core download --path=./wpssgblog --locale=en_US
php ./wp-cli.phar config create --path=./wpssgblog --locale=en_US --dbuser=wpssguser --dbpass=wpssgpass  --dbname=wpssgdb  --dbhost=127.0.0.1
php ./wp-cli.phar db create --path=./wpssgblog
php ./wp-cli.phar core install --path=./wpssgblog --url=wpssgblog.local --title="WP-CLI" --admin_user=wpcli --admin_password=wpcli --admin_email=info@wp-cli.org
php ./wp-cli.phar server --path=./wpssgblog --host=127.0.0.1 --port=8080
```
