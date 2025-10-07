

Start the broker
```bash
podman run -p 1883:1883 -v ./mosquitto.conf:/mosquitto/config/mosquitto.conf docker.io/eclipse-mosquitto:2.0.18
```

Subscribe
```bash
mosquitto_sub -h localhost -t test/#
```

Publish
```bash
 mosquitto_pub -h 127.0.0.1 -p 1883 -t test/b -m "Test message"
```