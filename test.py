import pandas as pd
Data=[
  {"name":"sunny","age":28,"city":"bhopal"},
  {"name":"sudhanshu","age":33,"city":"Delhi"},
  {"name":"krish","age":35,"city":"bengalore"},
  {"name":"vikas","age":29,"city":"pune"}
]

Data = pd.DataFrame(Data)

Data.to_csv("data/data.csv",index=False)