# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, raw_input().split())
terms = map(str, raw_input().split())
sum = 0
op = "+"
for term in terms:
    if not term in ("+", "-"):
        if op == "+":
            sum += eval(term)
        else:
            sum -= eval(term)
    else:
        op = term

print(sum == k)
