import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if len(distinct) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    return pd.DataFrame({'SecondHighestSalary': [distinct.iloc[1]]})
