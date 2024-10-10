# Primer of running WordPress as a Static Site Generator (SSG) with Markdown content
Please see [`.github/workflows/publish.yml`](.github/workflows/publish.yml) for the code

Currently uses:
- https://github.com/dirtsimple/postmark for Markdown import
- https://github.com/elementor/wp2static for static website crawling

# WordPress SQL schema
```sql
PRAGMA synchronous = OFF;
PRAGMA journal_mode = DELETE;
BEGIN TRANSACTION;
CREATE TABLE `wp_commentmeta` (
  `meta_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `comment_id` integer  NOT NULL DEFAULT '0'
,  `meta_key` varchar(255) DEFAULT NULL
,  `meta_value` longtext COLLATE BINARY
);
CREATE TABLE `wp_comments` (
  `comment_ID` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `comment_post_ID` integer  NOT NULL DEFAULT '0'
,  `comment_author` tinytext NOT NULL
,  `comment_author_email` varchar(100) NOT NULL DEFAULT ''
,  `comment_author_url` varchar(200) NOT NULL DEFAULT ''
,  `comment_author_IP` varchar(100) NOT NULL DEFAULT ''
,  `comment_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `comment_date_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `comment_content` text NOT NULL
,  `comment_karma` integer NOT NULL DEFAULT '0'
,  `comment_approved` varchar(20) NOT NULL DEFAULT '1'
,  `comment_agent` varchar(255) NOT NULL DEFAULT ''
,  `comment_type` varchar(20) NOT NULL DEFAULT 'comment'
,  `comment_parent` integer  NOT NULL DEFAULT '0'
,  `user_id` integer  NOT NULL DEFAULT '0'
);
CREATE TABLE `wp_links` (
  `link_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `link_url` varchar(255) NOT NULL DEFAULT ''
,  `link_name` varchar(255) NOT NULL DEFAULT ''
,  `link_image` varchar(255) NOT NULL DEFAULT ''
,  `link_target` varchar(25) NOT NULL DEFAULT ''
,  `link_description` varchar(255) NOT NULL DEFAULT ''
,  `link_visible` varchar(20) NOT NULL DEFAULT 'Y'
,  `link_owner` integer  NOT NULL DEFAULT '1'
,  `link_rating` integer NOT NULL DEFAULT '0'
,  `link_updated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `link_rel` varchar(255) NOT NULL DEFAULT ''
,  `link_notes` mediumtext NOT NULL
,  `link_rss` varchar(255) NOT NULL DEFAULT ''
);
CREATE TABLE `wp_options` (
  `option_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `option_name` varchar(191) NOT NULL DEFAULT ''
,  `option_value` longtext NOT NULL
,  `autoload` varchar(20) NOT NULL DEFAULT 'yes'
,  UNIQUE (`option_name`)
);
CREATE TABLE `wp_postmeta` (
  `meta_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `post_id` integer  NOT NULL DEFAULT '0'
,  `meta_key` varchar(255) DEFAULT NULL
,  `meta_value` longtext COLLATE BINARY
);
CREATE TABLE `wp_posts` (
  `ID` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `post_author` integer  NOT NULL DEFAULT '0'
,  `post_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `post_date_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `post_content` longtext NOT NULL
,  `post_title` text NOT NULL
,  `post_excerpt` text NOT NULL
,  `post_status` varchar(20) NOT NULL DEFAULT 'publish'
,  `comment_status` varchar(20) NOT NULL DEFAULT 'open'
,  `ping_status` varchar(20) NOT NULL DEFAULT 'open'
,  `post_password` varchar(255) NOT NULL DEFAULT ''
,  `post_name` varchar(200) NOT NULL DEFAULT ''
,  `to_ping` text NOT NULL
,  `pinged` text NOT NULL
,  `post_modified` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `post_modified_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `post_content_filtered` longtext NOT NULL
,  `post_parent` integer  NOT NULL DEFAULT '0'
,  `guid` varchar(255) NOT NULL DEFAULT ''
,  `menu_order` integer NOT NULL DEFAULT '0'
,  `post_type` varchar(20) NOT NULL DEFAULT 'post'
,  `post_mime_type` varchar(100) NOT NULL DEFAULT ''
,  `comment_count` integer NOT NULL DEFAULT '0'
);
CREATE TABLE `wp_term_relationships` (
  `object_id` integer  NOT NULL DEFAULT '0'
,  `term_taxonomy_id` integer  NOT NULL DEFAULT '0'
,  `term_order` integer NOT NULL DEFAULT '0'
,  PRIMARY KEY (`object_id`,`term_taxonomy_id`)
);
CREATE TABLE `wp_term_taxonomy` (
  `term_taxonomy_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `term_id` integer  NOT NULL DEFAULT '0'
,  `taxonomy` varchar(32) NOT NULL DEFAULT ''
,  `description` longtext NOT NULL
,  `parent` integer  NOT NULL DEFAULT '0'
,  `count` integer NOT NULL DEFAULT '0'
,  UNIQUE (`term_id`,`taxonomy`)
);
CREATE TABLE `wp_termmeta` (
  `meta_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `term_id` integer  NOT NULL DEFAULT '0'
,  `meta_key` varchar(255) DEFAULT NULL
,  `meta_value` longtext COLLATE BINARY
);
CREATE TABLE `wp_terms` (
  `term_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `name` varchar(200) NOT NULL DEFAULT ''
,  `slug` varchar(200) NOT NULL DEFAULT ''
,  `term_group` integer NOT NULL DEFAULT '0'
);
CREATE TABLE `wp_usermeta` (
  `umeta_id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `user_id` integer  NOT NULL DEFAULT '0'
,  `meta_key` varchar(255) DEFAULT NULL
,  `meta_value` longtext COLLATE BINARY
);
CREATE TABLE `wp_users` (
  `ID` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `user_login` varchar(60) NOT NULL DEFAULT ''
,  `user_pass` varchar(255) NOT NULL DEFAULT ''
,  `user_nicename` varchar(50) NOT NULL DEFAULT ''
,  `user_email` varchar(100) NOT NULL DEFAULT ''
,  `user_url` varchar(100) NOT NULL DEFAULT ''
,  `user_registered` datetime NOT NULL DEFAULT '0000-00-00 00:00:00'
,  `user_activation_key` varchar(255) NOT NULL DEFAULT ''
,  `user_status` integer NOT NULL DEFAULT '0'
,  `display_name` varchar(250) NOT NULL DEFAULT ''
);
CREATE INDEX "idx_wp_users_user_login_key" ON "wp_users" (`user_login`);
CREATE INDEX "idx_wp_users_user_nicename" ON "wp_users" (`user_nicename`);
CREATE INDEX "idx_wp_users_user_email" ON "wp_users" (`user_email`);
CREATE INDEX "idx_wp_posts_post_name" ON "wp_posts" (`post_name`);
CREATE INDEX "idx_wp_posts_type_status_date" ON "wp_posts" (`post_type`,`post_status`,`post_date`,`ID`);
CREATE INDEX "idx_wp_posts_post_parent" ON "wp_posts" (`post_parent`);
CREATE INDEX "idx_wp_posts_post_author" ON "wp_posts" (`post_author`);
CREATE INDEX "idx_wp_links_link_visible" ON "wp_links" (`link_visible`);
CREATE INDEX "idx_wp_options_autoload" ON "wp_options" (`autoload`);
CREATE INDEX "idx_wp_term_taxonomy_taxonomy" ON "wp_term_taxonomy" (`taxonomy`);
CREATE INDEX "idx_wp_term_relationships_term_taxonomy_id" ON "wp_term_relationships" (`term_taxonomy_id`);
CREATE INDEX "idx_wp_commentmeta_comment_id" ON "wp_commentmeta" (`comment_id`);
CREATE INDEX "idx_wp_commentmeta_meta_key" ON "wp_commentmeta" (`meta_key`);
CREATE INDEX "idx_wp_usermeta_user_id" ON "wp_usermeta" (`user_id`);
CREATE INDEX "idx_wp_usermeta_meta_key" ON "wp_usermeta" (`meta_key`);
CREATE INDEX "idx_wp_terms_slug" ON "wp_terms" (`slug`);
CREATE INDEX "idx_wp_terms_name" ON "wp_terms" (`name`);
CREATE INDEX "idx_wp_comments_comment_post_ID" ON "wp_comments" (`comment_post_ID`);
CREATE INDEX "idx_wp_comments_comment_approved_date_gmt" ON "wp_comments" (`comment_approved`,`comment_date_gmt`);
CREATE INDEX "idx_wp_comments_comment_date_gmt" ON "wp_comments" (`comment_date_gmt`);
CREATE INDEX "idx_wp_comments_comment_parent" ON "wp_comments" (`comment_parent`);
CREATE INDEX "idx_wp_comments_comment_author_email" ON "wp_comments" (`comment_author_email`);
CREATE INDEX "idx_wp_termmeta_term_id" ON "wp_termmeta" (`term_id`);
CREATE INDEX "idx_wp_termmeta_meta_key" ON "wp_termmeta" (`meta_key`);
CREATE INDEX "idx_wp_postmeta_post_id" ON "wp_postmeta" (`post_id`);
CREATE INDEX "idx_wp_postmeta_meta_key" ON "wp_postmeta" (`meta_key`);
END TRANSACTION;
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
- https://www.gloomycorner.com/publishing-posts-to-a-wordpress-site-with-markdown/
- https://github.com/joshcanhelp/wordpress-to-markdown
- https://github.com/gloomic/wp-cli-markdown-post
- https://stackoverflow.com/questions/18671/quick-easy-way-to-migrate-sqlite3-to-mysql
- https://te-st.org/2023/09/01/kind-wordpress/
- https://kndwp.org/
- https://wp2static.com/developers/wp-cli/

- https://github.com/wp-cli/wp-cli/issues/6000
- https://github.com/wp-cli/wp-cli/issues/6001
- https://sqlite.org/forum/forumpost/fa6fd7b3ae
- https://github.com/WordPress/wordpress-develop/pull/3220
- https://github.com/WordPress/sqlite-database-integration/pull/157
- https://bugs.mysql.com/bug.php?id=65941
- https://gist.github.com/esperlu/943776

- https://github.com/jekyll/minima/tree/demo-site
- https://stackoverflow.com/questions/18772504/wp-insert-post-error-content-title-and-excerpt-are-empty
- https://github.com/dirtsimple/postmark/issues/4
