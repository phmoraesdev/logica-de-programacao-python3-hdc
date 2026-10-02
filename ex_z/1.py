# You are given an integer N where 0 <= N <= 100, followed by another line of input 
# which has a word W with length L where 1 <= L <= 50. Your task is to print N lines with 
# the word W. The lines of your output should not have any trailing or leading spaces.
# Your output lines should not have any trailing or leading whitespace

n = int(input(""))
w = (input("")).strip()

for i in range(n):
    print(w)