# this class implements functions that count the number of times a certain letter occurs in a string passed in by a user
class DNAparser:

    # when class is initialised, it takes a string passed in by the user, and sets a counter for each of the letters to be counted
    def __init__(self, dna_string):
        self.dna_string = dna_string.upper()
        self.a_counter = 0
        self.c_counter = 0
        self.g_counter = 0
        self.t_counter = 0

    # function to count the number of A's in the string
    def a_count(self):
        for i in self.dna_string:
            if i == 'A':
                self.a_counter += 1
        return self.a_counter

    # function to count the number of C's in the string
    def c_count(self):
        for i in self.dna_string:
            if i == 'C':
                self.c_counter += 1
        return self.c_counter

    # function to count the number of G's in the string
    def g_count(self):
        for i in self.dna_string:
            if i == 'G':
                self.g_counter += 1
        return self.g_counter

    # function to count the number of T's in the string
    def t_count(self):
        for i in self.dna_string:
            if i == 'T':
                self.t_counter += 1
        return self.t_counter

    # function to display the number of A's, C's, G's, and T's, respectively
    def total_count(self):
        print(self.a_counter, self.c_counter, self.g_counter, self.t_counter)