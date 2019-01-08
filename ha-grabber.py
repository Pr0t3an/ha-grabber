import urllib.request
import json
import time, sys
import calendar
import argparse
import os, re
try:
    import schedule
except ImportError:
    print("[*] Install schedule from requirements")
    sys.exit(1)

outpath=""
ops ="w"

def getmedata():
    url = 'https://www.hybrid-analysis.com/feed?json'
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    f = urllib.request.urlopen(req)
    jdr = json.loads((f.read().decode('utf-8')))
    return jdr


def kickeroffer():
    print("running")
    sup = calendar.timegm(time.gmtime())
    outpath2 = os.path.join(outpath, 'hybridanalysis_' + str(sup) + '.log' )
    jsondata = getmedata()
    with open(outpath2, ops) as f:
        json.dump(jsondata, f)


def loopymcloop(ttime):
    schedule.every().day.at(ttime).do(kickeroffer)
    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    """Run main function."""
    parser = argparse.ArgumentParser(description='Grab JSON file from Hybrid Analysis Once per Day..suggested usage nohup python3 ha-grabber.py -o /path/to -t 12:00 &')
    parser.add_argument('-o', '--dir', help='PST input file')
    parser.add_argument('-t', '--tod', help='time of day to run: format hh:mm')
    # parser.add_argument('-a', '--append', help='Append or Overwrite file', action='store_false')
    args, _ = parser.parse_known_args()
    pattern = re.compile("([2][0-3]|[0-1][0-9]):[0-5][0-9]")
    if os.path.isdir(args.dir):
        outpath=args.dir
    else:
        print("[*] Install schedule from requirements")
        sys.exit(1)
    if pattern.match(args.tod):
        ttime = args.tod
    else:
        print("[*] Check time format matches hh:mm")
        sys.exit(1)
    #if args.append:
    #    ops="r+"
    #else:
    #    ops="w"
    loopymcloop(ttime)


if __name__ == "__main__":
    main()
