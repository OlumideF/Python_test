import os
import csv
import pandas as fr

from glob import glob

def openfile():
    old = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\TPython\\2R.txt'

    new = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\TPython\\cerd.txt'

    # open new text file
    with open(old, 'r') as oldfile:
        with open(new, 'w') as newfile:
            old_file = oldfile.readlines()
            newfile.writelines(old_file[141:167])

    file_dir = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd0.csv'

    with open(new, 'r') as new_file:
        with open(file_dir, 'w') as file_line:

            for lines in new_file:
                if lines.strip():
                    col = lines.split()
                    file_line.writelines(col[0] + '\n')

    file_dir1 = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd1.csv'

    with open(new, 'r') as new_file1:
        with open(file_dir1, 'w') as file_line1:

            for lines1 in new_file1:
                if lines1.strip():
                    col1 = lines1.split()
                    file_line1.writelines(col1[1] + '\n')

    file_dir2 = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd8.csv'

    with open(new, 'r') as new_file2:
        with open(file_dir2, 'w') as file_line2:

            for lines2 in new_file2:
                if lines2.strip():
                    col2 = lines2.split()
                    file_line2.writelines(col2[8] + '\n')

    file_dir3 = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd9.csv'

    with open(new, 'r') as new_file3:
        with open(file_dir3, 'w') as file_line3:

            for lines3 in new_file3:
                if lines3.strip():
                    col3 = lines3.split()
                    file_line3.writelines(col3[9] + '\n')

    file_dir4 = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd10.csv'

    with open(new, 'r') as new_file4:
        with open(file_dir4, 'w') as file_line4:

            for lines4 in new_file4:
                if lines4.strip():
                    col4 = lines4.split()
                    file_line4.writelines(col4[10] + '\n')

    file_dir5 = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd11.csv'

    with open(new, 'r') as new_file5:
        with open(file_dir5, 'w') as file_line5:

            for lines5 in new_file5:
                if lines5.strip():
                    col5 = lines5.split()
                    file_line5.writelines(col5[11] + '\n')

    file_dir6 = 'C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore\\cerd12.csv'

    with open(new, 'r') as new_file6:
        with open(file_dir6, 'w') as file_line6:

            for lines6 in new_file6:
                if lines6.strip():
                    col6 = lines6.split()
                    file_line6.writelines(col6[12] + '\n')


openfile()


def mergefile(a = "C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Explore", b = "C:\\Users\\Olumide-Swift\\OneDrive\\Training on Python CERD\\Final\\cerdresult.csv"):
    os.chdir(a)
    filelist = glob("*.csv")
    dfile = []

    columnNames = ["Atomic No", "Symbols", " Conc PPM", " %Stat Error", "Present", "LOD PPM", "Tit Error"]
    for filename in filelist:
        print(filename)
        df = fr.read_csv(filename, header=None)

        dfile.append(df)

    concaDf = fr.concat(dfile, axis=1)
    concaDf.columns = columnNames
    concaDf.to_csv(b, index=None)


mergefile()