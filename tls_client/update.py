import requests


def get_lastest():
    response = requests.get(
        url="https://api.github.com/repos/bogdanfinn/tls-client/releases/latest"
    )
    data = response.json()

    return data["tag_name"].lstrip("v")


def update_dependencies():
    shared_library_version = get_lastest()
    print(f"Downloading tls-client shared libraries version: {shared_library_version}")

    github_download_url = f"https://github.com/bogdanfinn/tls-client/releases/download/v{shared_library_version}/{{}}"
    github_repo_filenames = [
        
        # Windows
        f"tls-client-windows-32-{shared_library_version}.dll",
        f"tls-client-windows-64-{shared_library_version}.dll",
        
        # MacOS
        f"tls-client-darwin-arm64-{shared_library_version}.dylib",
        f"tls-client-darwin-amd64-{shared_library_version}.dylib",
        
        # Linux
        f"tls-client-linux-alpine-amd64-{shared_library_version}.so",
        f"tls-client-linux-ubuntu-amd64-{shared_library_version}.so",
        f"tls-client-linux-arm64-{shared_library_version}.so"
    ]

    dependency_filenames = [
        
        # Windows
        "tls-client-32.dll",
        "tls-client-64.dll",

        # MacOS
        "tls-client-arm64.dylib",
        "tls-client-x86.dylib",
        
        # Linux
        "tls-client-amd64.so",
        "tls-client-x86.so",
        "tls-client-arm64.so"
    ]

    for github_filename, dependency_filename in zip(github_repo_filenames, dependency_filenames):
        response = requests.get(
            url=github_download_url.format(github_filename)
        )

        with open(f"tls_client/dependencies/{dependency_filename}", "wb") as f:
            f.write(response.content)

