let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (python-pkgs: [
      # python-pkgs.ffmpeg-python
      python-pkgs.pyaudio
      # python-pkgs.wave
    ]))
  ];
}
