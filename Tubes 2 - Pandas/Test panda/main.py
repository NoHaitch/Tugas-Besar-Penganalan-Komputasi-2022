import pandas as pd
data = pd.read_csv("D:\\data\Education\\A MAHASISWA ITB\\Pengkom\\AA Tubes 2\\Test panda\\adult.csv", usecols=[0,3,4,8,9,14])
# not data is seperated by ", " not pure coma seperated variable , key is already fix no need space 
print(data)

# Age ------------------------
sum_age = 0
for i in range(len(data["Age"])):
    sum_age += data["Age"][i] 
avrg_age = int(sum_age/len(data["Age"]))
print(f"Avarage age: {avrg_age}")

# Education ------------------------
sum_edu = 0
for i in range(len(data["Edunum"])):
    sum_edu += data["Edunum"][i] 
avrg_edu = int(sum_edu/len(data["Edunum"]))
print(f"Avarage education number: {avrg_edu}")

# Income rasio
count_male, count_female = 0,0
count_male_incomeover50, count_male_incomebelow50, count_female_incomeover50, count_female_incomebelow50 = 0,0,0,0
for i in range(len(data["Sex"])):
    if(data["Sex"][i] == " Male"):
        count_male += 1
        if(data["Income"][i] == " >50K"):
            count_male_incomeover50 += 1
        else:
            count_male_incomebelow50 += 1
    else:
        count_female += 1
        if(data["Income"][i] == " >50K"):
            count_female_incomeover50 += 1
        else:
            count_female_incomebelow50 += 1
#print(count_male,count_male_incomebelow50,count_male_incomeover50,sep=" - ")
#print(count_female,count_female_incomebelow50,count_female_incomeover50,sep=" - ")
rasio_income_male = count_male_incomeover50 / count_male * 100
rasio_income_female = count_female_incomeover50 / count_female * 100
print("\n~ Correlation Sex to Income")
print(f"Male rasio to have >50k income: {rasio_income_male:0.2f}%")
print(f"Female rasio to have >50k income: {rasio_income_female:0.2f}%")
if(rasio_income_male-rasio_income_female <= 2.5):
    print("Thus female and female have around the same likely to get higher income")
elif(rasio_income_male > rasio_income_female):
    print("Thus female is more likely to get higher income than female")
else:
    print("Thus female is more likely to get higher income than male")

print("\n~ Correlation Educationn to Income")
edunum = dict()
rasio_edunum = dict()
for i in range(len(data["Edunum"])):
    if(int(data["Edunum"][i]) in edunum):
        if(data["Income"][i] == " >50K"):
            edunum[int(data["Edunum"][i])][0] += 1
        else:
            edunum[int(data["Edunum"][i])][1] += 1  
    else:
        edunum[int(data["Edunum"][i])] = [0,0]
        rasio_edunum[int(data["Edunum"][i])] = 0
        if(data["Income"][i] == " >50K"):
            edunum[int(data["Edunum"][i])][0] += 1
        else:
            edunum[int(data["Edunum"][i])][1] += 1  
for i in edunum:
    rasio_edunum[i] = edunum[i][0]/(edunum[i][0]+edunum[i][1]) * 100
rasio_edunum = dict(sorted(rasio_edunum.items(), key=lambda item:item[0],reverse=True))
print("Education number with rasio to have >50K income")
for i in rasio_edunum:
    print(f"{i} : {rasio_edunum[i]:0.2f}%")
cek_rasio_edunumtoincome = len(rasio_edunum)//2
now,before,count = -1,-1,0
for i in rasio_edunum:
    if(now == -1):
        now = rasio_edunum[i]
        continue
    before = now
    now = rasio_edunum[i]
    if(now < before):
        count += 1
if(count >= cek_rasio_edunumtoincome):
    print("Thus Higher education have higher chances to get higher income")
else:
    print("Thus Higher education don't have higher chances to get higher income")
