#coding:utf-8

string1 = raw_input("Please enter a word:")

string2 = string1[::-1]

if string2 == string1:
    print "%r is a Palindrome." % string2
else:
    print "%r is not a Palindrome." % string2
