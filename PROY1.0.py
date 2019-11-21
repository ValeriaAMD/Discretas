booleanos = [False, True]

# Tabla de verdad de or

print('P\tQ\tP or Q')
print('-'*22)
for P in booleanos:
    for Q in booleanos:
        print(P, Q, P or Q )

print

# Tabla de verdad de and

print('P\tQ\tP and Q')
print('-'*22)
for P in booleanos:
    for Q in booleanos:
        print(P, Q, P and Q )
        
print

# Tabla de verdad de not

print('P\tnot P')
print('-'*13)
for P in booleanos:
    print(P, not P)

print

# Tabla de verdad de ^

print('P\tQ\tP ^ Q')
print('-'*21)
for P in booleanos:
    for Q in booleanos:
        print(P, Q, P ^ Q)
        
print

