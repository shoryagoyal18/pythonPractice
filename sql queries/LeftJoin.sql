SELECT students.student_id, students.student_name, courses.course_name
FROM students LEFT JOIN courses 
ON students.course_id = courses.course_id;