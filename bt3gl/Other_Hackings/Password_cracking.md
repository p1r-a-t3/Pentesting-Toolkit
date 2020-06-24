# Password

## Brute-force password cracking with Hydra

1. Download [Hydra](https://www.thc.org/thc-hydra/) and install it:

```bash
$ ./configure
$ make
$ make install
```

2. Check with Burp what's the auth type (e.g. use FoxyProxy to proxy to localhost:8080 so burp can intercept it).

2. Run hydra with wordlists (and username lists). Example:

```bash
$ hydra -l <username> -P <password-list> -V <server> <service>
```
