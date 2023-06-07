# ppos-repos-ostree

RPM package for PPOS repositories. 

## Requirements

```bash
sudo dnf install rpmdevtools
```

## Building

```bash
# Optionally run `rm -rf ~/rpmbuild/` to ensure we have a clean working directory. 
rpmdev-setuptree

cp -r SPECS/* ~/rpmbuild/SPECS/
cp -r SOURCES/* ~/rpmbuild/SOURCES/

rpmbuild -bs ~/rpmbuild/SPECS/ppos-repos-ostree.spec
rpmbuild -bb ~/rpmbuild/SPECS/ppos-repos-ostree.spec
```

The resulting rpm files are the located inside `~/rpmbuild/SRPMS/` and `~/rpmbuild/RPMS/`.

```bash
ls -l ~/rpmbuild/SRPMS/
ls -l ~/rpmbuild/RPMS/
```
