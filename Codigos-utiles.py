import pandas as pd
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
