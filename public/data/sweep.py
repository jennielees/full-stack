import csv

from datetime import datetime, timedelta

def tomorrow_day():
    now = datetime.now()
    one_day = timedelta(days=1)
    return (now + one_day).strftime("%a")


def block_check(start, finish, house):

    # print "Checking if {} is within {}-{}".format(house, start, finish)

    start = int(start)
    finish = int(finish)

    if start < house < finish:
        return True
    else:
        return False


def swept_on_day(street_name, house_number, day_name):

    with open('sweep.csv') as f:

        reader = csv.DictReader(f)

        for row in reader:

            street = row['CORRIDOR']

            if street.lower() == street_name.lower():
                # We have a match!

                # Which side of the road does this row refer to?
                right_or_left = row['CNNRIGHTLE']

                # Check if we are on the right block
                if right_or_left == 'R':
                    sweep_from = row['RT_FADD']
                    sweep_to   = row['RT_TOADD']
                else:
                    sweep_from = row['LF_FADD']
                    sweep_to   = row['LF_TOADD']

                my_block = block_check(sweep_from, sweep_to, house_number)

                if my_block:

                    day = row['WEEKDAY']
                    if day == day_name:
                        # It is swept today. We can return now.
                        return True

    return False

def main():

    now = datetime.now()
    now_day = now.strftime("%a")

    # Correct for 'Tue' vs 'Tues'
    if now_day == 'Tue':
        now_day = 'Tues'

    # We put now_day in an argument so it is easier to test out
    # this function.

    result = swept_on_day("Vesta St", 33, now_day)
    print "If today is Thursday, this should be True: {}".format(result)

    result = swept_on_day("Coral Rd", 87, now_day)
    print "If today is Thursday, this should be False: {}".format(result)

    tomorrow = tomorrow_day()
    if tomorrow == 'Tue':
        tomorrow = 'Tues'

    result = swept_on_day("Dukes Ct", 77, tomorrow)
    print "If tomorrow is Friday, this should be True: {}".format(result)

    result = swept_on_day("Fanning Way", 60, tomorrow)
    print "If today is Friday, this should be False: {}".format(result)


if __name__=="__main__":
    main()