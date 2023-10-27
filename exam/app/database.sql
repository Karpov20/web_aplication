-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_2065_exam_py
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('bda417c8b88e');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_genre`
--

DROP TABLE IF EXISTS `book_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_genre` (
  `book.id` int(11) DEFAULT NULL,
  `genre.id` int(11) DEFAULT NULL,
  KEY `fk_book_genre_book.id_books` (`book.id`),
  KEY `fk_book_genre_genre.id_genres` (`genre.id`),
  CONSTRAINT `fk_book_genre_book.id_books` FOREIGN KEY (`book.id`) REFERENCES `books` (`id`),
  CONSTRAINT `fk_book_genre_genre.id_genres` FOREIGN KEY (`genre.id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_genre`
--

LOCK TABLES `book_genre` WRITE;
/*!40000 ALTER TABLE `book_genre` DISABLE KEYS */;
INSERT INTO `book_genre` VALUES (1,1),(2,2),(2,6),(3,1),(4,1),(5,1),(7,1),(9,5);
/*!40000 ALTER TABLE `book_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `short_desc` text NOT NULL,
  `created_at` varchar(4) NOT NULL,
  `publishing_house` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `volume` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  `background_image_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_books_background_image_id_images` (`background_image_id`),
  CONSTRAINT `fk_books_background_image_id_images` FOREIGN KEY (`background_image_id`) REFERENCES `images` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'Капитанская дочка','<p><em>История любви Петра Гринева и Марии Мироновой, главных героев \"Капитанской дочки\", вплетена в ход действий восстания Емельяна Пугачева. \"Не приведи бог видеть русский бунт, бессмысленный и беспощадный!\" - писал А. Пушкин, потрясенный жестокостью крестьянского мятежа, произошедшего летом 1831 года, в одной из глав \"Капитанской дочки\". Изучение материалов дела Ем. Пугачева, поездки по местам событий помогли сформироваться замыслу исторического романа.\n\"Капитанская дочка\" и \" История Пугачева\" А. Пушкина включены в данную книгу.</em></p>','2020','Эксмо','А.С. Пушкин',320,29,6,'6efb104f-685b-4ae6-b40f-a02144c96220'),(2,'Секрет еловых писем','<p><em>Жизнь кота-детектива не так-то легка. Вместо того чтобы наслаждаться безмятежным сном и отменными деликатесами, Уинстону приходится расследовать новое запутанное преступление. В этот раз случилось невероятное: одноклассницу его подруги Киры Эмилию похитили — и это в самый разгар репетиций школьного спектакля, в котором девочка играла главную роль! Теперь преступник требует выкуп! Детям и дворовым кошкам придётся объединиться, чтобы вывести злоумышленника на чистую воду.</em></p>\n<p><em>Серия-бестселлер! Книги о коте Уинстоне помогли уже сотне тысяч детей полюбить чтение! Вместе с Уинстоном и его друзьями читатель переживёт захватывающие приключения и спасёт одну очень вредную девочку от похитителей. Будет суперинтересно!\nКот Уинстон наверняка станет любимцем и настоящим другом вашего ребёнка. Ведь он такой обаятельный!\nИстория написана с юмором и дарит хорошее настроение.</em></p>','2022','Эксмо','Фрауке Шойнеманн',352,10,2,'e0a022b7-bf26-40cc-a938-701cdaf54289'),(3,'Портрет Дориана Грея','<p>\"Портрет Дориана Грея\" — самое знаменитое произведение Оскара Уайльда, единственный его роман, вызвавший в свое время шквал негативных оценок и тем не менее имевший невероятный успех.\nГлавный герой романа, красавец Дориан, — фигура двойственная, неоднозначная. Тонкий эстет и романтик становится безжалостным преступником. Попытка сохранить свою необычайную красоту и молодость оборачивается провалом. Вместо героя стареет его портрет — но это не может продолжаться вечно, и смерть Дориана расставляет все по своим местам.\nРоман Оскара Уайльда продолжает быть очень актуальным и сегодня — разве погоня за вечной молодостью порой не оборачивается потерей своего истинного лица?</p>','2021','Эксмо','Оскар Уайльд',320,4,1,'67180a26-d50f-4402-8d8d-9f28c3a2c023'),(4,'Гроза. Бесприданница','<p>&lt;p&gt;В сборник вошли две, наверное, самые знаменитые пьесы Островского – «Гроза» (1859 г.) и «Бесприданница» (1878 г.). В обеих пьесах описывается трагическая судьба их героинь. Две разбитые жизни. Два пылких сердца. Две пронзительные истории любви. И две попытки вырваться из замкнутого круга. Во времена Островского «Гроза» произвела эффект разорвавшейся бомбы, не случайно критик Добролюбов назвал ее героиню «лучом света в темном царстве».\nНесмотря на то, что времена поменялись, пьесы не теряют своей актуальности. Потому что ханжество, показная добродетель, эгоизм и себялюбие всегда будут противостоять искренним чувствам и настоящим порывам души.&lt;/p&gt;</p>','2022','ACT','Александр Островский ',224,20,4,'3795d3a8-5172-40d9-81a5-7c2d43d3ff62'),(5,' Обломов ','<p>Иван Гончаров — один из самых крупных писателей-реалистов золотого века русской литературы. Роман «Обломов» — часть знаменитой «трилогии о русской жизни», куда также вошли «Обыкновенная история» и «Обрыв».</p>','2022','ACT','Иван Гончаров',640,9,2,'f4aaf8e0-3bda-447f-9e12-12445acc5154'),(7,'Война и мир','<p>\"Война и мир\" - это эпический роман Льва Толстого, написанный в XIX веке. Книга охватывает широкий период истории России, начиная с французского нашествия под предводительством Наполеона и заканчивая войной 1812 года и битвой при Бородино. Она рассказывает о судьбах нескольких аристократических семей, освещая их жизни, любовные и семейные отношения, а также их взаимодействие с историческими событиями. \"Война и мир\" известен своими глубокими размышлениями об истории, философии, и человеческой природе. Это одно из самых величественных произведений мировой литературы, олицетворяющее русский реалистический роман.</p>','1865','Русский вестник','Лев Толстой',1300,5,1,'7ba27404-e451-4c9c-ac4d-bcf4c869963f'),(9,'Убить пересмешника','<p>&lt;p&gt;&lt;p&gt;\"Убить пересмешника\" - это роман американской писательницы Харпер Ли, опубликованный в 1960 году. Книга рассказывает о событиях, развивающихся в американском городке Мейкомб, Алабама, в 1930-х годах. Главной героиней является Жан Луиза Финч, рассказчица и дочь адвоката Аттикуса Финча.&lt;/p&gt;\n&lt;p&gt;История книги фокусируется на событиях, связанных с расовой несправедливостью и неравенством, а также на судебном процессе, в котором Аттикус Финч представляет чернокожего мужчину, обвиняемого в изнасиловании белой женщины. Роман исследует темы предвзятости, невиновности, справедливости и морали.&lt;/p&gt;\n&lt;p&gt;\"Убить пересмешника\" является классическим произведением американской литературы и получило множество наград и признаний за свое влияние на обсуждение социальных и расовых вопросов в Соединенных Штатах.&lt;/p&gt;&lt;/p&gt;</p>','1960','АСТ','Харпер Ли',350,0,0,'7fd1d566-0505-4e9e-9298-8f3aee433458');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_genres_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (2,'Детектив'),(6,'Детская литература'),(8,'История'),(1,'Классика'),(7,'Приключения'),(5,'Роман'),(4,'Фантастика'),(3,'Фэнтези');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_images_md5_hash` (`md5_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES ('35f3ff07-db50-44d5-81c6-5d700060dc42','2023-10-22_180904.png','image/png','837cf0c4792507459bc8f0541b049ea4','2023-10-25 23:59:11'),('3795d3a8-5172-40d9-81a5-7c2d43d3ff62','a7e47ca8-6e88-4523-af25-cd412abd32fd.jpg','image/jpeg','7feea5cd960af2458e89c36784ce3b9f','2023-10-03 18:24:30'),('430f164b-3c04-492d-9e45-34e11d6bff27','2023-10-22_181354.png','image/png','ef8f20f74d1abad0e2017542a8de270b','2023-10-25 23:58:56'),('67180a26-d50f-4402-8d8d-9f28c3a2c023','2592760-1.jpg','image/jpeg','3d9f709710f998dbe76e9712d62d8b13','2023-10-03 18:21:26'),('6efb104f-685b-4ae6-b40f-a02144c96220','2810820.jpg','image/jpeg','a636f3666d5f0072b19c8df20ed373c7','2023-10-01 22:12:37'),('7ba27404-e451-4c9c-ac4d-bcf4c869963f','6cb4524f-768f-4426-8615-df727a2701d9.jpg','image/jpeg','b6d29147bdd9e621ec15d89cb62ea066','2023-10-25 19:42:45'),('7fd1d566-0505-4e9e-9298-8f3aee433458','1235648.jpg','image/jpeg','d0d7d1d96f62471a9f11bd9ebb17ab30','2023-10-25 23:58:05'),('a63f282e-4087-45fa-85a0-096002438ad3','jpg','image/jpeg','d122adea412e8148bfe6b163876170b6','2023-10-25 23:56:47'),('e0a022b7-bf26-40cc-a938-701cdaf54289','a7e47ca8-6e88-4523-af25-cd412abd32fd.jpg','image/jpeg','55b4b7c37533c312e112ce56826402b9','2023-10-03 18:17:29'),('f4aaf8e0-3bda-447f-9e12-12445acc5154','2931599.jpg','image/jpeg','871ecfc8fb78b704577c06fb09a1c9ad','2023-10-03 18:27:13');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reviews_book_id_books` (`book_id`),
  KEY `fk_reviews_user_id_users` (`user_id`),
  CONSTRAINT `fk_reviews_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `fk_reviews_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,5,'<p>Отличное произведение!</p>','2023-10-01 22:13:54',1,1),(2,4,'<p><em>Хорошо</em></p>','2023-10-01 22:26:39',1,2),(3,5,'<p>Отлично!!</p>','2023-10-01 22:27:25',1,3),(4,5,'<p>Прекрасная книга!</p>','2023-10-01 22:28:14',1,4),(5,5,'<p>Обязательно к прочтению!</p>','2023-10-01 22:29:02',1,5),(6,5,'<p>Удивительное произведение</p>','2023-10-01 22:29:45',1,6),(7,5,'<p><strong>Good</strong></p>','2023-10-03 19:51:28',2,3),(8,4,'<p><em>Хорошо</em></p>','2023-10-03 20:00:00',3,3),(9,5,'<p>\"Обломов\" Ивана Гончарова - это литературное произведение, которое многие рассматривают как классику русской литературы и одну из важнейших работ XIX века. Книга представляет собой глубокий психологический портрет главного героя, Ильи Ильича Обломова, и одновременно яркую критику российской общественной жизни в то время.</p>\n<p>Илья Обломов - символ инерции, бездействия и апатии. Его леность и нежелание встать с дивана стали классическими образами литературы. Через историю Обломова, Гончаров выражает свое видение российской интеллигенции и общества, которое могло бы быть более активным, но увлекается бесплодными размышлениями и пустыми мечтами.</p>\n<p>Однако, в \"Обломове\" также содержится глубокая грусть и сочувствие к своему герою. Гончаров описывает его внутренние переживания, его мечты и желания, которые он так и не смог осуществить из-за своей апатии.</p>\n<p>Книга \"Обломов\" - это не только литературная критика, но и глубокое психологическое исследование человеческой натуры. Она позволяет читателям задуматься о собственных ценностях, действиях и жизненном выборе. Гончаров создал произведение, которое остается актуальным и вдохновляющим для размышлений о человеческой судьбе.</p>','2023-10-25 20:10:10',5,2),(12,5,'<p>jghgkj</p>','2023-10-27 13:29:38',4,4),(15,5,'<p>великолепная книга</p>','2023-10-27 13:36:50',7,4),(16,5,'<ul>\n<li>&gt; Прекрасная работа</li>\n</ul>','2023-10-27 13:55:04',4,1),(17,4,'<p><strong><em>понравилось</em></strong></p>','2023-10-27 14:46:04',5,1);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Администратор','суперпользователь, имеет полный доступ к системе, в том числе к созданию и удалению книг'),(2,'Модератор','может редактировать данные книг и производить модерацию рецензий'),(3,'Пользователь','может оставлять рецензии');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_users_login` (`login`),
  KEY `fk_users_role_id_roles` (`role_id`),
  CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','pbkdf2:sha256:260000$DaerA5lap669F7gw$57439f1d503139a5a7533feec155c5bc3b2b9aabcbcee4ae39ffcc94f0c8bbbf','Иванов','Иван',NULL,'2023-10-01 21:35:56',1),(2,'user','pbkdf2:sha256:260000$DaerA5lap669F7gw$57439f1d503139a5a7533feec155c5bc3b2b9aabcbcee4ae39ffcc94f0c8bbbf','Карпов','Александр',NULL,'2023-10-01 22:24:09',2),(3,'user2','pbkdf2:sha256:260000$DaerA5lap669F7gw$57439f1d503139a5a7533feec155c5bc3b2b9aabcbcee4ae39ffcc94f0c8bbbf','Паров','Олег',NULL,'2023-10-01 22:24:35',3),(4,'user3','pbkdf2:sha256:260000$DaerA5lap669F7gw$57439f1d503139a5a7533feec155c5bc3b2b9aabcbcee4ae39ffcc94f0c8bbbf','Павлов','Андрей',NULL,'2023-10-01 22:25:37',3),(5,'user4','pbkdf2:sha256:260000$DaerA5lap669F7gw$57439f1d503139a5a7533feec155c5bc3b2b9aabcbcee4ae39ffcc94f0c8bbbf','Лозовой','Артем',NULL,'2023-10-01 22:25:37',3),(6,'user5','pbkdf2:sha256:260000$DaerA5lap669F7gw$57439f1d503139a5a7533feec155c5bc3b2b9aabcbcee4ae39ffcc94f0c8bbbf','Лебеда','Вячеслав',NULL,'2023-10-01 22:25:37',3);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-27 15:54:31
