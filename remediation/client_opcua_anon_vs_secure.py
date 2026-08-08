from opcua import Client

url = "opc.tcp://127.0.0.1:4841/freeopcua/server/secure/"
client = Client(url)
try:
    client.connect()
    print("[ANOMALIE] Connexion anonyme acceptée par le serveur durci !")
    client.disconnect()
except Exception as e:
    print(f"[OPC UA durci] Connexion anonyme REJETÉE comme attendu : {type(e).__name__}: {e}")
