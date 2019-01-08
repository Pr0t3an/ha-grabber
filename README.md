# ha-grabber
Grab Hybrid Analysis JSON file once per day(built inscheduler) - maintains json useful for SIEM integration - outputs to new file each time, will add append options maybe at some stage if the need arises

----------------------------------------------

clone repo / pip install -r requirements.txt

sample usage (outputs to specified dir daily @ 21:35
python3 ha-grabber.py -o /ha-tool/ -t 21:35

------------------------------------

usage: ha-grabber.py [-h] [-o DIR] [-t TOD]


Grab JSON file from Hybrid Analysis Once per Day..suggested usage nohup
python3 ha-grabber.py -o /path/to -t 12:00 &

optional arguments:
  -h, --help         show this help message and exit

  -o DIR, --dir DIR  PST input file

  -t TOD, --tod TOD  time of day to run: format hh:mm


