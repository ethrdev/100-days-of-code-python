## =====================================================
##             Demo: Grading Program
## =====================================================

# Dieses Programm konvertiert Schülerprüfungswerte (student_scores) in Bewertungskategorien.
# Es nutzt ein dictionary, bei dem die Schlüssel die Namen der Schüler und die Werte deren Punktzahlen sind.
# Ziel ist es, am Ende ein neues dictionary 'student_grades' zu erhalten, in dem jedem Schüler die entsprechende Note zugewiesen wird.

## =====================================================
##             Scoring-Kriterien
## =====================================================

# Bewertungsmaßstab:
# Punktzahlen 91 - 100: "Outstanding"
# Punktzahlen 81 - 90: "Exceeds Expectations"
# Punktzahlen 71 - 80: "Acceptable"
# Punktzahlen 70 oder niedriger: "Fail"


# Definition des dictionaries 'student_scores' mit den Prüfungswerten der Schüler.
student_scores = {
    "Harry": 88,
    "Ron": 79,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

# student_grades = ["Outstanding", "Exceeds Expectations", "Acceptable", "Fail"]

# Initialisierung des leeren dictionaries 'student_grades', das später die Noten der Schüler enthalten wird.
student_grades = {}

# Kopieren der originalen Punktzahlen aus 'student_scores' in 'student_grades' zur späteren Umwandlung.
for key in student_scores:
    student_grades[key] = student_scores[key]

# Durchlaufen des dictionaries 'student_grades' zur Umwandlung der Punktzahlen in Noten basierend auf den Scoring-Kriterien.
for key in student_grades:
    print(student_grades[key])  # Ausgabe der aktuellen Punktzahl zur Überprüfung
    if student_grades[key] >= 91:
        student_grades[key] = "Outstanding"  # Zuweisung "Outstanding" für Punktzahlen 91-100
    elif student_grades[key] >= 81 and student_grades[key] <= 90:
        student_grades[key] = "Exceeds Expectations"  # Zuweisung "Exceeds Expectations" für Punktzahlen 81-90
    elif student_grades[key] >= 71 and student_grades[key] <= 80:
        student_grades[key] = "Acceptable"  # Zuweisung "Acceptable" für Punktzahlen 71-80
    else:
        student_grades[key] = "Fail"  # Zuweisung "Fail" für Punktzahlen 70 oder weniger
         
# Ausgabe des finalen dictionaries 'student_grades' mit den zugewiesenen Noten für jeden Schüler.
print(student_grades)
