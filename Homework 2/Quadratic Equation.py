def N_Q_E_solution(b, c):
    print(f"One solution: {-c / b}") 

def Q_E_solution(a, b, c):
    D = b * b - 4 * a * c
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    if D > 0:
        print(f"Disciminant: {D} \nTwo solutions: {x1} {x2}")
    else:
        print(f"Disciminant: {D} \nNo solutions")    

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == b == c == 0:
    print("Non-quadratic equation \nInfinite solutions")
elif a == b == 0:
    print('Non-quadratic equation \nNo Solutions')     
elif a == 0:
    print("Non-quadratic equation")
    N_Q_E_solution(b, c)
else:
    print("Quadratic equation")
    Q_E_solution(a, b, c)
