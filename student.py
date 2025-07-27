
studentID: str = ""

def setStudentID(ID: str) -> None:
    """Set the global student ID."""
    global studentID
    studentID = str(ID)

def getStudentID() -> str:
    """Get the global student ID."""
    return studentID