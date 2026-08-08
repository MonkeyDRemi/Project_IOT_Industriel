from opcua import Client, ua
from opcua.crypto.security_policies import SecurityPolicyBasic256Sha256

url = "opc.tcp://127.0.0.1:4841/freeopcua/server/secure/"
client = Client(url)
client.set_security(
    SecurityPolicyBasic256Sha256,
    "pki/client_cert.pem",
    "pki/client_key.pem",
    mode=ua.MessageSecurityMode.SignAndEncrypt,
)
try:
    client.connect()
    print("[OPC UA sécurisé] Connecté (canal chiffré + authentifié par certificat).")
    root = client.get_root_node()
    var = root.get_child(["0:Objects", "2:Temperature"])
    value = var.get_value()
    print(f"[OPC UA sécurisé] Valeur de Temperature : {value}")
finally:
    client.disconnect()
    print("[OPC UA sécurisé] Déconnecté.")
