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
def get_applicants(cursor):
    cursor.execute("""
                    SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                    FROM applicants
                    INNER JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                    WHERE applicants_mentors.creation_date > '2016-01-01'
                    ORDER BY applicants_mentors.creation_date DESC;
                   """)
    applicants_data = cursor.fetchall()
    return applicants_data


@database_common.connection_handler
def get_applicants_and_mentors(cursor):
    cursor.execute("""
                    SELECT applicants.first_name AS applicant, applicants.application_code, mentors.first_name, mentors.last_name  
                    FROM applicants
                    LEFT JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                    LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id
                   """)
    applicants_and_mentors = cursor.fetchall()
    return applicants_and_mentors
