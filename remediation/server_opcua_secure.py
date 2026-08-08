from opcua import Server, ua
import time

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/secure/")
server.load_certificate("pki/server_cert.pem")
server.load_private_key("pki/server_key.pem")
server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])

uri = "http://examples.freeopcua.github.io"
idx = server.register_namespace(uri)
objects = server.get_objects_node()
myvar = objects.add_variable(idx, "Temperature", 23.5)
myvar.set_writable()

server.start()
print("Serveur OPC UA DURCI démarré sur opc.tcp://0.0.0.0:4841 (Basic256Sha256 SignAndEncrypt uniquement)")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.stop()
    print("Serveur arrêté.")
