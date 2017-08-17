### Description

Notes on creating jwt for use with the heketi vagrant standalone demo


### Usage
Update create_jwt for the endpoint, or go to To Do

```
./create_jwt.py
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTUwMjkxNDk3MywicXNoIjoiYzE2MmFjYzkwMjQyNzIxMjBiYWNmZmY3NzA5YzkzMmNjMjUyMzM3ZDBhMzBmYTE1YjAyNTAxMDA2NjY2MmJlYSIsImV4cCI6ODc5MDMwMDEzNzN9.sziyOWtRBtUoXoEPVYAXD6NDExE30Oef5Fz_iBPY574

[vagrant@storage0 ~]$ curl -sH "Authorization: BEARER eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTUwMjkxNDk3MywicXNoIjoiYzE2MmFjYzkwMjQyNzIxMjBiYWNmZmY3NzA5YzkzMmNjMjUyMzM3ZDBhMzBmYTE1YjAyNTAxMDA2NjY2MmJlYSIsImV4cCI6ODc5MDMwMDEzNzN9.sziyOWtRBtUoXoEPVYAXD6NDExE30Oef5Fz_iBPY574" -X GET http://192.168.10.100:8080/volumes  | python -m json.tool
{
    "volumes": [
        "6250047089da1709d8a3d864a040b2ad",
        "795280cbfc23b9e7c89363eb14dc4c58",
        "c97d6941304df8ea9cffb4aecd920414"
    ]
}

```
### To do
learn to use pyjwt directly

### References

* https://github.com/heketi/heketi/wiki/API#authentication

```
git remote -v
origin  https://github.com/heketi/vagrant-heketi.git (fetch)
origin  https://github.com/heketi/vagrant-heketi.git (push)

pwd
~ /heketi_project/vagrant-heketi/standalone

ls
roles     Vagrantfile site.yml README.md     up.sh
```
