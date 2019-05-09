# let
#   inherit (import <nixpkgs> {}) fetchFromGitHub;
#   nixpkgs_download = fetchFromGitHub {
#     owner = "NixOS";
#     repo = "nixpkgs-channels";
#     rev = "1bc5bf4beb759e563ffc7a8a3067f10a00b45a7d";
#     sha256 = "00gd96p7yz3rgpjjkizp397y2syfc272yvwxqixbjd1qdshbizmj";
#   };
# in
#   import nixpkgs_download {}
let
  inherit (import <nixpkgs> {}) fetchFromGitHub;
  nixpkgs_download = fetchFromGitHub {
    owner = "NixOS";
    repo = "nixpkgs-channels";
    rev = "6a3f5bcb061e1822f50e299f5616a0731636e4e7";
    sha256 = "1ib96has10v5nr6bzf7v8kw7yzww8zanxgw2qi1ll1sbv6kj6zpd";
  };
in
  import nixpkgs_download {}
