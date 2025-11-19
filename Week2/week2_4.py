def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}
    subject_score[student][subject] = score

    if int(score) < 0:
        return "Invalid"
    return calc_average_score(subject_score, student, subject)

def calc_average_score(subject_score, student, subject):
    total_dist = {}
    for j in subject_score:
        num = 0
        total = 0
        for i in subject_score[j]:
            total += int(subject_score[j][i])
            num += 1
        total = total/num
        if j not in total_dist:
            total_dist[j] = {}
            total_dist[j] = str("%0.2f" % total)

    ans = str(subject_score)
    ans += str(", Average score: ")
    ans += str(total_dist)
    return ans

def preparing(data_in):
    try:
        parts = [p.strip() for p in data_in.split(" | ")]
        data_dict = eval(parts[0])
        data_id = parts[1].strip("''")
        data_property = parts[2].strip("''")
        data_value = parts[3].strip("''")
        data_value = data_value.strip("''")
        data_value = int(data_value)

        if int(data_id) <= 0 and data_dict == {} or not(data_property):
            return "Invalid"

        return add_score(data_dict,data_id,data_property,data_value)
    except:
        return "Invalid"


x = input()
print(preparing(x))