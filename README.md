# [WIP] Attempt at using WordPress as a Static Site Generator (SSG)

```shell
sudo apt install php-cli php-mysql php-dom mysql-server sqlite3

# download https://wp-cli.org/
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

sudo service mysql start
# create user and password
sudo mysql <<< "CREATE USER 'wpssguser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'wpssgpass';"
# test the local connection to the database
sudo mysql <<< "SHOW DATABASES; SELECT user FROM mysql.user;"
sudo mysql --user=wpssguser --password=wpssgpass --database=wpssgdb <<< "SHOW DATABASES"


# https://make.wordpress.org/cli/handbook/how-to/how-to-install/
php ./wp-cli.phar core download --locale=en_US #  --skip-content --force
php ./wp-cli.phar config create --locale=en_US --dbuser=wpssguser --dbpass=wpssgpass  --dbname=wpssgdb  --dbhost=127.0.0.1
php ./wp-cli.phar db create   
php ./wp-cli.phar core install --url=localhost:8080 --title=wpcli --admin_user=wpcli --admin_password=wpcli --admin_email=info@wp-cli.org
php wp-cli.phar option set permalink_structure '/%year%-%monthnum%-%day%-%postname%/'

# download and unpack theme
php ./wp-cli.phar theme install --activate https://knd.te-st.ru/kandinsky.zip

php ./wp-cli.phar server --host=localhost --port=8080
open http://127.0.0.1:8080

php wp-cli.phar post list --post_type=page --field=url
php wp-cli.phar post list --post_type=post --field=url
# wget --recursive --html-extension http://localhost:8080
# wget -P wpssgmirror -nd --mirror --convert-links --adjust-extension --page-requisites  --no-parent  --restrict-file-names=ascii,windows http://localhost:8080


curl -O -L https://github.com/elementor/wp2static/archive/refs/tags/7.2.tar.gz
mkdir -p wp-content/plugins/wp2static # php wp-cli.phar plugin path
tar -xf 7.2.tar.gz -C wp-content/plugins/wp2static --strip-components=1
cd wp-content/plugins/wp2static
curl -o composer.phar https://getcomposer.org/installer
php composer.phar install
php composer.phar update
php composer.phar install --quiet --no-dev --optimize-autoloader
cd ../../../
php wp-cli.phar plugin activate wp2static
php wp-cli.phar wp2static options set deploymentURL http://localhost:8080/
php wp-cli.phar wp2static detect
php wp-cli.phar wp2static crawl
php wp-cli.phar wp2static post_process
open wp-content/uploads/wp2static-processed-site/index.html
```

```shell
# uploads, but depends on Apache?
mkdir ./wp-content/uploads
#chgrp web ./wp-content/uploads/
chmod 775 ./wp-content/uploads/

php ./wp-cli.phar export --filename_format=exportWXR.xml
sudo mysqldump --skip-extended-insert --no-data --compact wpssgdb --result-file=wpssgdbddl.sql
sudo mysqldump --skip-extended-insert --no-create-info --compact wpssgdb --result-file=wpssgdata.sql
sudo mysqldump --xml --skip-extended-insert --no-create-info --compact wpssgdb wp_options --result-file=wpssgopts.xml
git clone https://github.com/dumblob/mysql2sqlite 
awk -f mysql2sqlite/mysql2sqlite wpssgddl.sql | sed s'/PRAGMA journal_mode = MEMORY/PRAGMA journal_mode = DELETE/' > wpssgddlsqlite.sql
python wpssgdata.py wpssgsqlite.db wpssgddlsqlite.sql wpssgdata.sql
# use https://sqlitebrowser.org/ to inspect wpssgdata.db

```

# References
- https://make.wordpress.org/core/2023/04/19/status-update-on-the-sqlite-project/
- https://github.com/WordPress/wordpress-develop/pull/3220
- https://core.trac.wordpress.org/ticket/57793
- https://wordpress.org/plugins/sqlite-database-integration/
- https://wp2static.com/developers/wp-cli/
- https://github.com/dirtsimple/postmark
- https://www.digitalocean.com/community/tutorials/how-to-use-wp-cli-to-manage-your-wordpress-site-from-the-command-line
- https://blog.hubspot.com/website/backup-wordpress-site-using-cpanel
- https://simplystatic.com
- https://kinsta.com/blog/wp-cli/
- https://leonstafford.wordpress.com/wordpress-static-html-output-plugin
- https://localwp.com/
