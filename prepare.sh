#!/bin/bash
#dnf install -y cargo rustc

CRATE="starship-1.10.3"

# Create temp folder
TEMP=$(mktemp -d)

set -x
spectool -g rust-starship.spec || true

FOLDER="$PWD"

# Extract the tarball to /tmp/src/
mkdir -p $TEMP
tar -xzf ./$CRATE.crate -C $TEMP

ls -la $TEMP

pushd $TEMP/$CRATE || exit

cargo vendor

tar -czvf "$FOLDER"/vendor.tar.gz vendor

#ls -la

#mv -v ./vendor.tar.gz "$FOLDER"/vendor.tar.gz


# tarball the .cargo folder

#tar -czf "$FOLDER"/cargo-config.tar.gz .cargo


popd || exit

rm -rf $TEMP
set +x