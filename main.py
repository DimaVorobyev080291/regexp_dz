import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

my_phonebook = []
new_list = []

def collecting_information():
    for i in contacts_list:
        combining_string = " ".join(i[0:3])
        splitting_string = combining_string.split()
        if len(splitting_string) == 3 :
            my_phonebook.append(splitting_string)
        else:
            splitting_string.append('')
            my_phonebook.append(splitting_string)

    for i, l in zip(my_phonebook, contacts_list): 
        i.append(l[3])
        i.append(l[4])

    for i , l in zip(my_phonebook, contacts_list): 
        pattern = re.compile(
            r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
        subst_pattern = r'+7(\2)\3-\4-\5\7\8\9'
        if l[5] != "":
            result = pattern.sub(subst_pattern, l[5])
            i.append(result)
        else:
            i.append('')
    
    for i , l in zip(my_phonebook, contacts_list): 
        i.append(l[6])   
    return my_phonebook

def duplicates_combining():
    for column in my_phonebook[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in my_phonebook:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]

    for contact in my_phonebook:
        if contact not in new_list:
            new_list.append(contact)
    return new_list

if __name__ == '__main__':
    collecting_information()
    duplicates_combining()
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)