let
  nixpkgs = import ./nixpkgs_version.nix;
  pypkgs = nixpkgs.python36Packages;
in
  nixpkgs.stdenv.mkDerivation rec {
    name = "similarity";
    env = nixpkgs.buildEnv { name=name; paths=buildInputs; };
    buildInputs = [
      pypkgs.pip
       pypkgs.python
       pypkgs.numpy
       pypkgs.scipy
       pypkgs.pandas
       pypkgs.cython
       pypkgs.matplotlib
       pypkgs.tkinter
       nixpkgs.pkgs.git
       pypkgs.jupyter
       pypkgs.toolz
  ];
    src = null;
    shellHook = ''
      SOURCE_DATE_EPOCH=$(date +%s)
      export PYTHONUSERBASE=$PWD/.local
      export USER_SITE=`python -c "import site; print(site.USER_SITE)"`
      export PYTHONPATH=$PYTHONPATH:$USER_SITE
      export PATH=$PATH:$PYTHONUSERBASE/bin

      jupyter nbextension install --py widgetsnbextension --user > /dev/null 2>&1
      jupyter nbextension enable widgetsnbextension --user --py > /dev/null 2>&1
      pip install jupyter_contrib_nbextensions --user > /dev/null 2>&1
      jupyter contrib nbextension install --user > /dev/null 2>&1
      jupyter nbextension enable spellchecker/main > /dev/null 2>&1

      # pip install --user -r requirements.txt

      pip install --user atomman

      # To install iprPy
      # cd ..
      # git clone https://github.com/lmhale99/iprPy.git
      # cd iprPy
      # pip install --user .

    '';
}
