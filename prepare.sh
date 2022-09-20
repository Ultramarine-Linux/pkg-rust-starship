#!/bin/bash
set -x
spectool -g rust-starship.spec || true

FOLDER="$PWD"

# Extract the tarball to /tmp/src/
mkdir -p /tmp/src
tar -xzf ./starship-1.10.3.crate -C /tmp/src

pushd /tmp/src/* || exit

cargo vendor

tar -czvf "$FOLDER"/vendor.tar.gz vendor

#ls -la

#mv -v ./vendor.tar.gz "$FOLDER"/vendor.tar.gz


# tarball the .cargo folder

#tar -czf "$FOLDER"/cargo-config.tar.gz .cargo


popd || exit

rm -rf /tmp/src
set +x