
def clean_student_marks(path: str) -> str:
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