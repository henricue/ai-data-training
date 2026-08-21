#!/usr/bin/env bash

set -euo pipefail

destination=${1:?Anna asennettavan typst-tiedoston polku}
version=${2:?Anna asennettava Typst-versio}

if [[ -x "$destination" ]]; then
    echo "Typst on jo asennettu: $destination"
    exit 0
fi

case "$(uname -s)-$(uname -m)" in
    Darwin-arm64)
        target="aarch64-apple-darwin"
        ;;
    Darwin-x86_64)
        target="x86_64-apple-darwin"
        ;;
    Linux-aarch64|Linux-arm64)
        target="aarch64-unknown-linux-musl"
        ;;
    Linux-x86_64)
        target="x86_64-unknown-linux-musl"
        ;;
    *)
        echo "Typstin automaattista asennusta ei tueta tällä alustalla." >&2
        echo "Asenna Typst käsin: https://github.com/typst/typst#installation" >&2
        exit 1
        ;;
esac

archive="typst-${target}.tar.xz"
url="https://github.com/typst/typst/releases/download/v${version}/${archive}"
temporary_directory=$(mktemp -d)
trap 'rm -rf "$temporary_directory"' EXIT

echo "Asennetaan Typst ${version}..."
curl --fail --location --retry 3 --output "$temporary_directory/$archive" "$url"
tar -xJf "$temporary_directory/$archive" -C "$temporary_directory"
mkdir -p "$(dirname "$destination")"
install -m 0755 "$temporary_directory/typst-${target}/typst" "$destination"
