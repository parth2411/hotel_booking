import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='booking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #with connection.cursor() as cursor:
        # Create a new record
#        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
#    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `customer` WHERE `fname`=%s"
        cursor.execute(sql, ('Akash',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()


















