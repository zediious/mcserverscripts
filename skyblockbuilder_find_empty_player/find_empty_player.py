import python_nbt.nbt

nbtfile = python_nbt.nbt.read_from_nbt_file('skyblock_builder.dat')
found = 0

def check_metainformation():
    counter = 0
    global found
    for player in nbtfile['data']['MetaInformation']:
        counter += 1
        if player['Player'][1] == 0:
            print('A player UUID is empty, deleting entry.')
            del nbtfile['data']['MetaInformation'][counter]
            found = found + 1
        
def check_islands():
    counter = 0
    global found
    for island in nbtfile['data']['Islands']:
        counter += 1
        for player in island['Players']:
            if player['Player'] == 0:
                print('Found an empty player on an island, deleting empty player.')
                del nbtfile['data']['Islands'][island]['Players'][counter]
                found = found + 1

def main():

    check_metainformation()
    check_islands()
    
    print('Found: ' + str(found))
    
    if found > 0:
        print ('Operation complete, saving NBT.')
        python_nbt.nbt.write_to_nbt_file('skyblock_builder.dat', nbtfile)
        
    else:
        print ('Operation complete with no changes made.')


if __name__ == '__main__':
	main()