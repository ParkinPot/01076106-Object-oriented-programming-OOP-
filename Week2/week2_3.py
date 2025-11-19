def add_score(subject_score, subject, score):
    if subject != "" and score >= 0: 
        subject_score[subject] = score
    return subject_score

def calc_average_score(score_list):
    size = len(score_list)
    total_score = sum(score_list)
    if size > 0:
        average = total_score / size
        return average
    else:
        return 0

value = input()

try:
    dict_part, subject_score_part, score_part = value.split(" | ")
    subject_score = eval(dict_part)  
    subject = subject_score_part.strip("'")
    score = int(score_part.strip())

    updated_subject_score = add_score(subject_score, subject, score)
    
    score_list = list(updated_subject_score.values())
    average_score = calc_average_score(score_list)

    output = f"{updated_subject_score}, Average score: {average_score:.2f}"
except ValueError:  
    output = "Invalid"

print(output)

