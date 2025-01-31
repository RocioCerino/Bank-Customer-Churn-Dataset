import pandas as pd
import numpy as np
import pandas_profiling


df = pd.read_csv('Bank Customer Churn Prediction.csv')



df.info()

df["credit_score"].describe()

df["credit_score"].isnull().sum().sum()
type(df["credit_score"])
type(df[["credit_score"]])

df[["credit_score", "age"]].describe()

df2 = df[df["age"] > 35]
df2


profile = pandas_profiling.ProfileReport(df)

profile.to_file("output.html")
tabla = df[["gender", "country"]].value_counts().reset_index()

ver = pd.pivot_table(tabla, index= "gender", columns= "country").reset_index()

df.columns

tabla_ro = pd.pivot_table(df, index="country", columns="tenure" )

ver


ver2 = df.groupby(["gender"]).agg(numero_usuario=('age', 'mean'))
ver2



df2 = df.iloc[:,0:3].copy()
df3 = df.iloc[:,0]

df3["columna"] = 1

df3 = df3.merge(df2, how="left", on = "customer_id")


variables = ['credit_score','balance' ]
agg_d = {i:lambda val: (val == 0).sum() for i in variables}
agg_d
ver2 = df.groupby(["gender"]).agg(agg_d)
ver2

df[df['credit_score'] == 0].shape[0]



df[df['balance'] == 0].shape[0]

# vamos a hace boludeces - limpiar de extremos alguna variable


df2 = df[df["age"] >= np.median(df["age"])]

df2.shape
df.shape

ls = np.mean(df2["age"]) + 2*np.std(df["age"])
li = np.mean(df["age"]) - 2*np.std(df["age"])

df_dep = df[(df.age >= li) & (df.age <= ls)]

df.columns  

ver2 = df.groupby(["gender"]).agg(numero_usuario=('age', 'mean'))
vemos = df.groupby(['country']).agg(edad_media=('age', 'mean'), edad_sd = ('age', 'std'))

variables = ['credit_score','balance' ]
agg_1 = {i:lambda val: val.mean() for i in variables}
agg_2 = {i:lambda val: (val == 0).sum() for i in variables}

ver2 = df.groupby(["gender"]).agg(agg_1, agg_2)

df_ver = df[df['age'] >= 30].groupby('gender').agg(
    # Get max of the duration column for each group
    max_age=('age', max),
    # Get min of the duration column for each group
    min_age=('age', min),
    # Get sum of the duration column for each group
    total_balance=('balance', sum),
    # Apply a lambda to date column
    # num_days=("date", lambda x: (max(x) - min(x)).days)    
)

