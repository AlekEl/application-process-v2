import database_common


@database_common.connection_handler
def get_mentors_and_school(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country 
                    FROM mentors
                    INNER JOIN schools ON mentors.city = schools.city
                    ORDER BY mentors.id;
                   """)
    mentors_and_school = cursor.fetchall()
    return mentors_and_school


@database_common.connection_handler
def get_mentors_all_schools(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country 
                    FROM mentors
                    RIGHT JOIN schools ON mentors.city = schools.city
                    ORDER BY mentors.id;
                   """)
    mentors_all_schools = cursor.fetchall()
    return mentors_all_schools


@database_common.connection_handler
def get_mentors_by_country(cursor):
    cursor.execute("""
                    SELECT schools.country, COUNT(mentors) AS Mentors
                    FROM schools
                    INNER JOIN mentors ON schools.city = mentors.city
                    GROUP BY schools.country
                    ORDER BY schools.country;
                   """)
    mentors_by_country = cursor.fetchall()
    return mentors_by_country


@database_common.connection_handler
def get_contacts(cursor):
    cursor.execute("""
                    SELECT schools.name, mentors.first_name, mentors.last_name
                    FROM schools
                    INNER JOIN mentors ON mentors.id = schools.contact_person
                    ORDER BY schools.name                    
                   """)
    contacts_data = cursor.fetchall()
    return contacts_data


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
