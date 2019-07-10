import csv
def write_group_to_csv(data,filename,encoding='utf-8'):
    with open(filename, 'w', encoding='cp1251', errors='replace', newline='') as csvfile:
        fieldnames=['id','first_name','last_name','sex','bdate','city','country','mobile_phone','home_phone','skype','twitter','instagram','photo_200_orig','university_name','faculty_name','graduation','education_form','education_status','schools_name','schools_year_from','schools_year_to','relatives']
        writer=csv.DictWriter(csvfile,delimiter=',',fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        print('Data about group is written in',filename)
     csvfile.close

write_group_to_csv(G_idd,'123.csv')