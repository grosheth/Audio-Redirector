let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (python-pkgs: [
      python-pkgs.pyaudio
      python-pkgs.numpy
      python-pkgs.matplotlib
    ]))
  ];
}
