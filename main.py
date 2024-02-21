import define
from IPython.display import display

df = define.load_data("data.csv")

summary = define.table(df)

display(summary)
