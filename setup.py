import csv

def read_setup(f):

    with open(f) as file:
        reader = csv.reader(file)
        setup = []
        for row in reader:
            setup.append(row)
    output = {}
    for i in setup: # for line in csv, sort by flag, add corresponding keys
        # Key = Val(s):
        # Profile1 = n[(Register, Value)]
        # Profile1bit = n[(Register, Bit, Bool)]
        # Wheel = Float circumference in mm
        # Battery = SeriesInt, ParallelInt, TotalAhFloat
        try:
            if i[0][0] == '#':
                pass
            elif i[0] == 'profile1':
                if 'profile1' in output:
                    output['profile1'].append((i[1].strip(), float(i[2])))
                elif not 'profile1' in output:
                    output['profile1'] = [(i[1].strip(), float(i[2]))]
            elif i[0] == 'profile2':
                if 'profile2' in output:
                    output['profile2'].append((i[1].strip(), float(i[2])))
                elif not 'profile2' in output:
                    output['profile2'] = [(i[1].strip(), float(i[2]))]
            elif i[0] == 'profile3':
                if 'profile3' in output:
                    output['profile3'].append((i[1].strip(), float(i[2])))
                elif not 'profile3' in output:
                    output['profile3'] = [(i[1].strip(), float(i[2]))]
            elif i[0] == 'profile1bit':
                if 'profile1bit' in output:
                    output['profile1bit'].append((i[1].strip(), int(i[2]), bool(int(i[3]))))
                elif not 'profile1bit' in output:
                    output['profile1bit'] = [(i[1].strip(), int(i[2]), bool(int(i[3])))]
            elif i[0] == 'profile2bit':
                if 'profile2bit' in output:
                    output['profile2bit'].append((i[1].strip(), int(i[2]), bool(int(i[3]))))
                elif not 'profile2bit' in output:
                    output['profile2bit'] = [(i[1].strip(), int(i[2]), bool(int(i[3])))]
            elif i[0] == 'profile3bit':
                if 'profile3bit' in output:
                    output['profile3bit'].append((i[1].strip(), int(i[2]), bool(int(i[3]))))
                elif not 'profile3bit' in output:
                    output['profile3bit'] = [(i[1].strip(), int(i[2]), bool(int(i[3])))]
            elif i[0] == 'wheel' or i[0] == 'whl':
                output['wheel'] = float(i[1])
            elif i[0] == 'battery' or i[0] == 'batt':
                output['battery'] = (int(i[1]), int(i[2]), float(i[3]))
            elif i[0] == 'controllerport' or i[0] == 'cpt' or i[0] == 'bacport':
                output['cpt'] = i[1].strip()
            elif i[0] == 'bmsport' or i[0] == 'bpt':
                output['bpt'] = i[1].strip()
            elif i[0] == 'units':
                output['units'] = i[1].strip()
            elif i[0] == 'pin':
                output['pin'] = i[1].strip()
            elif i[0] == 'gpioprofiles':
                output['gpioprofile'] = True
        except IndexError:
            pass
    return output
