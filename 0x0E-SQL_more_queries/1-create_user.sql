--  creates the MySQL server user user_0d_1
-- Has all privileges & password set to user_0d_1_pwd
CREATE USER IF NOT EXISTS `user_0d_1` IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON * . * TO `user_0d_1`@`localhost`;
