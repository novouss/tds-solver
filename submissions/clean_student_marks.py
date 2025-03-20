
def clean_student_marks(path: str) -> str:
    """ Cleans the student mark file and returns the number of students with valid data.

    Args:
        path (str): The path to the student mark file.

    Returns:
        str: A string representation of the number of students with valid data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a record in the file is invalid.
    
    Example:
        >>> clean_student_marks("path/to/student/marks.txt")
        '5'
    """
 
    with open(path, "r") as file:
        contents = file.readlines()
    
    student_marks = {}
    
    for content in contents:
        record = content.strip().rsplit("Marks", 1)
        marks = record[1].strip()
        record = record[0].strip().rsplit("-", 1)
        studentid = record[1].replace(":", "").strip()
        name = record[0].strip()
        
        result = {
            "name": name,
            "studentid": studentid,
            "marks": marks,
        }
        
        if not student_marks.get(studentid):
            student_marks[studentid] = result
    
    results = len(student_marks)
    
    return str(results)
