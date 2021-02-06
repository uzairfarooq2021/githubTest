import traceback
import pandas as pd
try:
    import os
    os.chdir(r'D:\OneDrive\Data Science and Machine Learning\Projects\Proj014_Tax-to-GDP')

    df01 = pd.read_excel('Tax-to-GDP.xlsx')
    df02 = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_tax_revenue_to_GDP_ratio')
    print(df01)
    print(df02)

    output_excel = pd.ExcelWriter('WikiTable.xlsx', datetime_format = 'dd-mmm-yyyy', date_format = 'dd-mmm-yyyy')
    df02[6].to_excel(output_excel)
    output_excel.save()

    input('Press enter to exit')
except Exception as err:
    traceback.print_tb(err.__traceback__)
    print(err)
    print(err.__class__.__name__)
    input('press any key')
