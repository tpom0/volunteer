#######################
# Very important...
#   
# Get python 2.7 (the latest version should be fine)
# Create a python 2.7 virtualenv
# Activate that virtualenv
# pip install -r requirements.txt to install the necessary Django packages
#
########################

## change date options in html fil
edit TPOM/TPOM/templates/schedule html in your favorite text editor  
change the dates in the option fields
NOTE: it is important to follow the format in the value="YYYY-MM-DD" element of the option tag

<select class="select form-control" id="date_selector">
    <option value="2019-02-21" selected="selected">Thursday - February 21st, 2019</option>
    <option value="2019-02-22">Friday - February 22nd, 2019</option>
    <option value="2019-02-23">Saturday - February 23rd, 2019</option>
</select>

## run the app
activte the python virtual environment  
then start the app and run it in the background  
source VirtualEnvs_python/TPOM_env/bin/activate  
cd TPOM/  
nohup python manage.py runserver &  


## accessing the app in the browser
go to http://127.0.0.1:8000/admin/
username: admin
password: TPOM

## update shift data with csv file  
1. get spreadsheet file from MCM  
2. open in your spreadsheet app (Excel, or similar)  
3. save as .csv file in the top level TPOM directory   
python import_shifts.py mcm_shifts_file.csv


## Windows setup hints
1. get python 2.7 (get the latest python 2.7 version)
2. get a python "virtualenv"
3. activate python virtualenv
4. pip install -r requirements.txt . (this is the requirements.txt in the TPOM directory, so make sure you are in the TPOM directory for this to work)
5. then do the "run the app" steps above
