import database_common


@database_common.connection_handler
def get_mentor_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY last_name;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nick_names(cursor):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    ORDER BY nick_name;
                   """)
    nicknames = cursor.fetchall()
    return nicknames


@database_common.connection_handler
def get_carol(cursor):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number  FROM applicants
                    WHERE first_name = 'Carol'
                   """)
    carol_data = cursor.fetchall()
    return carol_data


@database_common.connection_handler
def get_hat_girl(cursor):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number  FROM applicants
                    WHERE email LIKE '%@adipiscingenimmi.edu'
                   """)
    carol_data = cursor.fetchall()
    return carol_data


@database_common.connection_handler
def add_marcus(cursor):
    cursor.execute("""
                    INSERT INTO applicants
                      (first_name, last_name, phone_number, email, application_code)
                    SELECT 'Marcus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823
                    WHERE NOT EXISTS (
                        SELECT application_code FROM applicants WHERE application_code = 54823
                                     );
                   """)


@database_common.connection_handler
def get_marcus(cursor):
    cursor.execute("""
                    SELECT 
                      first_name, 
                      last_name, 
                      phone_number, 
                      email, 
                      application_code  
                    FROM applicants
                    WHERE application_code = 54823
                   """)
    marcus = cursor.fetchall()
    return marcus


@database_common.connection_handler
def update_jemima(cursor):
    cursor.execute("""
                    UPDATE applicants
                    SET phone_number = '003670/223-7459'
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman'
                   """)


@database_common.connection_handler
def get_jemima_number(cursor):
    cursor.execute("""
                    SELECT phone_number
                    FROM applicants
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman'
                   """)
    jemima = cursor.fetchall()
    return jemima


@database_common.connection_handler
def delete_mauriseu(cursor):
    cursor.execute("""
                    DELETE FROM applicants
                    WHERE email LIKE '%@mauriseu.net'
                   """)
