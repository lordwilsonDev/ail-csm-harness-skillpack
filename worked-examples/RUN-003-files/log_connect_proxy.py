import socket, threading, sys, time, json
LOG = open("proxy.log", "a", buffering=1)
def pump(a, b, cnt, key):
    try:
        while True:
            d = a.recv(65536)
            if not d: break
            cnt[key] += len(d); b.sendall(d)
    except Exception: pass
    finally:
        try: b.shutdown(socket.SHUT_WR)
        except Exception: pass
def handle(c):
    try:
        req = b""
        while b"\r\n\r\n" not in req:
            x = c.recv(4096)
            if not x: return
            req += x
        line = req.split(b"\r\n")[0].decode()
        meth, target, _ = line.split(" ", 2)
        if meth != "CONNECT":
            LOG.write(json.dumps({"t": round(time.time(), 2), "non_connect": line[:120]}) + "\n"); c.sendall(b"HTTP/1.1 405 no\r\n\r\n"); return
        host, port = target.rsplit(":", 1)
        s = socket.create_connection((host, int(port)), timeout=15)
        c.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        cnt = {"up": 0, "down": 0}
        t = threading.Thread(target=pump, args=(c, s, cnt, "up")); t.start()
        pump(s, c, cnt, "down"); t.join()
        LOG.write(json.dumps({"t": round(time.time(), 2), "host": host, "port": port, **cnt}) + "\n")
    except Exception as e:
        LOG.write(json.dumps({"err": str(e)[:80]}) + "\n")
    finally:
        try: c.close()
        except Exception: pass
srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 18080)); srv.listen(50)
while True:
    c, _ = srv.accept(); threading.Thread(target=handle, args=(c,), daemon=True).start()
