str1 = "a3b3c1"
data = ""
i = 0

while i < len(str1):
    char = str1[i]
    i += 1
    count = 0
    while i < len(str1) and str1[i].isdigit():
        count = count * 10 + int(str1[i])
        i += 1
    data += char * count

print(data)  # Output: "aaabbbcc"


str1="aaabbbc"
data=""
d={}
len1=len(str1)
for i in range(len1):
    if str1[i] not in d:
        d[str1[i]]=1
    else:
         d[str1[i]]+=1
for k,v in d.items():
    data+=f"{k}{v}"
print(data)



a="ammu"
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)


def sev(x):

    t=[0,0,7,'x']
    for i in x:
        if i==t[0]:
            t.pop(0)
    return len(t) ==1
sev([1,7,4,0,5,4,0,8])


def stru(name):
    len1=len(name)
    c=[]
    for i in range(len1):
        if i==0 or i==3:
            c.append(name[i].upper())
        else:
            c.append(name[i])
    return ''.join(c)
    
print(stru('macdonals'))


work_hours=[('alb',1000),('gfg',400),('sas',800)]
def empc(work_hours):
    current_time=0
    empl=""
    for emp,hr in work_hours:
        if hr > current_time:
            current_time=hr
            empl=emp
        else:
            pass
    return (empl,current_time)
empc(work_hours)


for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
            print(i, 'Fizz')
    elif i%5==0:
        print(i ,'Buzz')
    else:
        print(i)


pandas:

d={'k1':[{'nested':['test',['helo']],'amma':[1,2]}]}

d['k1'][0]['nested'][1][0]

d['k1'][0]['amma']


data = {
    'Name': ['John', 'Jane', 'John', 'Alice'],
    'Age': [28, 24, 28, 30],
    'Salary': [50000, 60000, 50000, 75000]
}
df = pd.DataFrame(data)
df
# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Print the DataFrame without duplicates
print("DataFrame without duplicates:")
print(df_no_duplicates)


import pandas as pd

# Create the DataFrame
data = {
    'Name': ['John', 'Jane'],
    'Date': ['2023-01-15', '2023-02-20']
}
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract year and month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Print the DataFrame with extracted year and month
print("DataFrame with Year and Month:")
print(df)



def salary_in_thousand(salary):
    return salary/1000

df['Salaries_thousand']=df['Salary'].apply(salary_in_thousand)
df

data1 = {
    'Name': ['John', 'Jane', 'Alice'],
    'Age': [28, 24, 30]
}
data2 = {
    'Name': ['John', 'Jane', 'Bob'],
    'Salary': [50000, 60000, 45000]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print("first",df2)
df1
cd=pd.merge(df1,df2,on='Name', how='inner')


a=df.groupby('Age')['Salary'].mean()
a

mean_sal=df['Salary'].mean()
df['Salary'].fillna(round(mean_sal),inplace=True)
df


data.sort_values(by='AGE',ascending=False)

print(data['ADDRESS'].value_counts())
print(data[data['AGE'] > 28])
all_cols=data.columns

all_rows=data.values

print(all_rows)

column=[col.strip() for col in all_cols if col.strip().isupper()]
print(column)

print(data.dtypes)
# data=data.astype(str)
print(data.dtypes)
print(len(data))
data.loc[len(data)]=('KIRAN',10,'MAK',1233)
print(data)

data['classs']=[12,8,10]
print(data)
print(data[data['Name']=='jane'])

