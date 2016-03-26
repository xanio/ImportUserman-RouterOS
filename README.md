# ImportUserman-RouterOS
Python application for create a script RouterOS file for import user into user-manager from a csv file

Application for import user into user-manager from a CSV File. 
The Application create a output script for RouterOS 6.X

            Ex. CSV File:
            "Login","Passowd"
            "user1","pass1"
            "user2","pass2"
            ...

positional arguments:

+ **FileCsv**      - First Argument is infile.csv
+ **OutFile**      - Second Argument is outfile.rsc
+ **ProfileName**  - Third Argument is Profile Name
  
#Usage
```bash
./ImportUser.py file.csv script.rsc 30h
```
