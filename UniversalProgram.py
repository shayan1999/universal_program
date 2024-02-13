from Decoder import *
from SnapshotHandler import check_line

def output_maker(snapshot):
    y= snapshot[0]
    otherValues= snapshot[1:]
    x_data= []
    z_data= []
    for i in range(len(otherValues)):
        if(i%2==0):
            z_data.append(otherValues[i])
        else:
            x_data.append(otherValues[i])
    result= z_data + x_data 
    result.append(y)
    result = ' '.join(map(str, result))
    return result

def run_code(snapshot, program_codes):
    line_number= 0
    print(line_number+1, output_maker(snapshot))
    while(line_number <len(program_codes) and len(program_codes)!=0):
        snapshot, line_number=check_line(code=program_codes, snapshot=snapshot, line_number=line_number)
        if(line_number+1<=len(program_codes)):
            print(line_number+1, output_maker(snapshot))

def main():
    # input_str = input("Please give me line code numbers separated by space: ")
    input_str = input()
    line_numbers = [int(num) for num in input_str.split()]
    # initial_str =input("Please enter your inputs separated by space (x1 x2 ... xm): ")
    initial_str =input()
    initial_values= [int(initial_str) for initial_str in initial_str.split()]
    program_lines, max_xz, program_codes= line_numbers_to_davis_language(line_numbers)
    
    # for line in program_lines:
    #         print(line)

    snapshot_len= max(max_xz, 2*len(initial_values)-1) +1
    snapshot=[]
    for i in range(snapshot_len):
        if(i%2 == 0):
            snapshot.append(0)
        else:
            if(i//2 < len(initial_values)):
                snapshot.append(initial_values[i // 2])
            else:
                snapshot.append(0)
    run_code(snapshot= snapshot, program_codes= program_codes)

if __name__ == "__main__":
    main()