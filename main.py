from csv import reader

def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    list=[]
    for i in file_name:
        list.append(i[3])
    return list
file_name=open('data.csv')
r=reader(file_name,delimiter=',')
print(get_country_column(file_name=r))
