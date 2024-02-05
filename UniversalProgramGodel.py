from sympy import factorint, primerange
from Decoder import *
from UniversalProgram import run_code

def decode_program_number_complete(program_number):
    adjusted_number = program_number + 1    
    factorization = factorint(adjusted_number)
    max_prime_factor = max(factorization.keys(), default=2)
    all_primes = list(primerange(1, max_prime_factor + 1))
    godel_numbers = [0] * len(all_primes)
    for i, prime in enumerate(all_primes):
        if prime in factorization:
            godel_numbers[i] = factorization[prime]
    
    return godel_numbers

def main():
    user_input = input("Please enter your inputs separated by space (x1 x2 ... xm ProgramNumber): ")
    inputs = [int(num) for num in user_input.split()]
    initial_values = inputs[:-1] 
    program_number = inputs[-1]
    line_numbers = decode_program_number_complete(program_number)
    program_lines, max_xz, program_codes= line_numbers_to_davis_language(line_numbers)
    for line in program_lines:
            print(line)
    print(f"Decoded Line numbers for program number {program_number}: {line_numbers}")

    snapshot_len= (2 * max(max_xz, len(initial_values))) + 1
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