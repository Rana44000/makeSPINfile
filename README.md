# makeSPINfile
code to make SPIN file using CHG file

Reads CHG file for structure information, grid dimensions, and extracts the second set of spin density data. 

Outputs this information into new file SPIN.vasp with the same format as CHG file.

The default input file is the CHG file but user can choose a different file using -chg

Vesta example using SiH3

CHG:


<img width="459" height="413" alt="image" src="https://github.com/user-attachments/assets/8735db82-358c-4ac0-989e-4e9113c79258" />


SPIN:


<img width="723" height="608" alt="image" src="https://github.com/user-attachments/assets/8458995e-09db-43e3-8517-9e0e1895e366" />
