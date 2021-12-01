"""
Louie regular
Duckworth steward
Launchpad McQuack pilot
Scrooge McDuck vip
"""

# pilot, vip, regular, steward

arr = ['Louie regular', 'Duckworth steward', 'Launchpad McQuack pilot',
       'Scrooge McDuck vip']


def staff_sort(names):

    weight = {
        'pilot': 0.4,
        'vip': 0.3,
        'regular': 0.2,
        'steward': 0.1
    }

    return sorted(arr, key=lambda x: weight.get(x.split()[-1]),
                  reverse=True)


print(staff_sort(arr))
