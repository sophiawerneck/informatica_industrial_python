# Objetos imutáveis

# nome (variável)  | objeto
a = 3
b = a

print("Valor: ", a)
print("Identificador de a: ", id(a)) #id identifica o objeto 3
print("Identificador de b antes da mudança: ", id(b))
b = 4
print("Identificador de b após a mudança: ", id(b))

a += 3  #cria um objeto 6 e o a aponta para esse valor, pq o valor 3 é imutável

print("Valor: ", a)
print("Identificador: ", id(a))

a = "Informática"

# Objetos mutáveis
# nome (variável)  | objeto
a = [1, 2, 3]  #identificador do a não muda
b = a
b.append(4)
print("Valor: ", a)
print("Identificador: ", id(a))
print("Identificador: ", id(b))

a.append(5)
print("Valor: ", a)
print("Identificador: ", id(a))


