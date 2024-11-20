from src.service.service_user import ServiceUser

service = ServiceUser()
user_1 = service.add_user("Gildo", "Analista")
user_2 = service.add_user("Vitor", "Analista2")

print(user_1)
print(user_2)

for user in service.store.bd:
    print(user.name, user.job)

print("Cadastrado")
print("---------------")
print("Removido")

service.remove_user("Gildo")

for user in service.store.bd:
    print(user.name, user.job)

print("---------------")
print("Cadastrado Novamente")
service.add_user("Gildo", "Analista")
for user in service.store.bd:
    print(user.name, user.job)
print("---------------")

print("Alterando")
service.update_user("Gildo", "Analista Teste 02")
for user in service.store.bd:
    print(user.name, user.job)
print("---------------")