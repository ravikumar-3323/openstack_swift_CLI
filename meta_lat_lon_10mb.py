import subprocess

lat = 1.0
lon = 0.0
for i in range(1,15):
    if i<=5:

        headers = ['-H', 'X-Object-Meta-Latitude:' + str(lat), '-H', 'X-Object-Meta-Longitude:' + str(lon), '-H', 'X-Object-Meta-Streetname:'+ 'Hinjewadi Phase1']
        object_name = f'10MB/object_{i}.bin'
        subprocess.call(['swift', 'post'] + headers + ['demo_container1', object_name])
    elif i>5 and i<=10:
        headers = ['-H', 'X-Object-Meta-Latitude:' + str(lat), '-H', 'X-Object-Meta-Longitude:' + str(lon), '-H', 'X-Object-Meta-Streetname:'+ 'Hinjewadi Phase2']
        object_name = f'10MB/object_{i}.bin'
        subprocess.call(['swift', 'post'] + headers + ['demo_container1', object_name])
    else:
        headers = ['-H', 'X-Object-Meta-Latitude:' + str(lat), '-H', 'X-Object-Meta-Longitude:' + str(lon), '-H', 'X-Object-Meta-Streetname:'+ 'Hinjewadi Phase3']
        object_name = f'10MB/object_{i}.bin'
        subprocess.call(['swift', 'post'] + headers + ['demo_container1', object_name])


    lon += 0.20
    lat += 0.20
