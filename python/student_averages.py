if __name__ == "__main__":

numberOfStudents, numberOfSubjects = map(int, input().split())

scores = []
for s in range(numberOfStudents):
    scores.append([])

for i in range(numberOfSubjects):
    subjectScores = input().split()
    for j in range(len(subjectScores)):
        scores[j].append(subjectScores[j])

for student in scores:
    sum = 0.0
    avg = 0.0
    if len(student) > 0:
        for subject in student:
            sum += float(subject)
        avg = sum / len(student)
    print(avg)
