class Table:
    def __init__(self):
        self.Tables = {}

    def createTables(self):
        self.studentTable()

    def studentTable(self):
        self.Tables['students'] = (
            "  CREATE TABLE `students` ("
            " `id` INT(11) NOT NULL AUTO_INCREMENT,"
            " `name` VARCHAR(255) NOT NULL,"
            " `class` VARCHAR(255) NOT NULL,"
            " `math` TINYINT(1) NOT NULL,"
            " `english` TINYINT(1) NOT NULL,"
            " `bangla` TINYINT(1) NOT NULL,"
            " `marks` INT(11) NOT NULL,"
            " `mathDays` INT(11) NOT NULL,"
            " `englishDays` INT(11) NOT NULL,"
            " `banglaDays` INT(11) NOT NULL,"
            " `earnings` INT(11) NOT NULL,"
            " `status` TINYINT(1) NOT NULL,"
            " `created` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB"
        )