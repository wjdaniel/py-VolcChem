
import os
import pandas as pd

def excelLoad(sheetNum):
    tempDir=os.getcwd()
    dataFile='%s\\data\\masterFile.xlsx' % tempDir
    tempFile=pd.read_excel(dataFile, sheet_name=sheetNum-1,header=0)
    outFile=tempFile.fillna(0)
    return outFile

    
