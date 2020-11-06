# DNAparser class imported as parent class
from dna_parser import DNAparser

# dna created as an instance of DNAparser class, and user is prompted to pass in a string
dna = DNAparser(input("Please enter your DNA string: "))

print(f"number of A's: {dna.a_count()}") # prints out number of A's in the string
print(f"Number of C's: {dna.c_count()}") # prints out number of C's in the string
print(f"Number of G's: {dna.g_count()}") # prints out number of G's in the string
print(f"Number of T's: {dna.t_count()}") # prints out number of T's in the string

dna.total_count()