import redis

r = redis.Redis(
    host='redis-11037.c280.us-central1-2.gce.redns.redis-cloud.com',
    port=11037,
    decode_responses=True,
    username="default",
    password="krewkgFxukPnveGxrFQNscISVC1uNFXg",
)

success = r.set('foo', 'bar')

# Obtener todos los campos del cliente "client:5"
cliente = r.hgetall('client:+17135550105')

# Mostrar los resultados
if cliente:
    print("Detalles del cliente 5:")
    for campo, valor in cliente.items():
        print(f"{campo}: {valor}")
else:
    print("Cliente no encontrado.")

# Set value of a hash
r.hset('client:+17135550105', 'recall_communicated', 'yes')