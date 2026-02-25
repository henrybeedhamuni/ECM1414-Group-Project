

## How to run the program
- 2 methods:
	- Open the terminal and use this command to change the current directory 
		`cd ~/ECM1414-Group-Project/Code` - changes current directory to code folder within submission, Path will need to be changed depending on where the submission folder is located
	- Use the python command to run the main file in the terminal:
		`python event_planner.py`
	- Once complete the user will get something like this output in the terminal which uses the small.txt file as input:
		========================================
		EVENT PLANNER - RESULTS
		========================================
		Input File: ../Input_Files/input_small.txt
		Available Time: 10 Hours
		Available Budget: £200
		 --- Standard Brute Force Algorithm --- 
		Selected Activities: 
		  Activity: Campus-Tour, Duration: 2 hours, Cost: £20, Enjoyment Level: 50
		  Activity: Game-Night, Duration: 3 hours, Cost: £80, Enjoyment Level: 120
		  Activity: Pizza-Workshop, Duration: 2 hours, Cost: £60, Enjoyment Level: 100
		  Activity: Hiking, Duration: 5 hours, Cost: £30, Enjoyment Level: 140
		Total Enjoyment: 410
		Total Time Used: 12 hours out of 10 hours.
		Total Cost: £190 out of £200
		
		Execution Time: 0.000014 Seconds
		
		
		 --- Enhanced Brute Force Algorithm --- 
		
		Selected Activities: 
			Activity: Game-Night, Duration: 3 hours, Cost: £80, Enjoyment Level: 120
			Activity: Pizza-Workshop, Duration: 2 hours, Cost: £60, Enjoyment Level: 100
			Activity: Hiking, Duration: 5 hours, Cost: £30, Enjoyment Level: 140
		Total Enjoyment: 360
		Total Time Used: 10 hours out of 10 hours.
		Total Cost: £170 out of £200
		
		Execution Time: 0.000009 Seconds
		
		
		 --- Standard Dynamic Programming Algorithm --- 
		
		Selected Activities: 
		  Activity: Game-Night, Duration: 3 hours, Cost: £80, Enjoyment Level: 120
		  Activity: Museum-Trip, Duration: 4 hours, Cost: £100, Enjoyment Level: 150
		  Activity: Pizza-Workshop, Duration: 2 hours, Cost: £60, Enjoyment Level: 100
		Total Enjoyment: 370
		Total Time Used: 9 hours out of 10 hours.
		Total Cost: £240 out of £200
		
		Execution Time: 0.000131 Seconds
		
		
		 --- Enhanced Dynamic Programming Algorithm --- 
		
		Selected Activities: 
		 Activity: Game-Night, Duration: 3 hours, Cost: £80, Enjoyment Level: 120
		 Activity: Pizza-Workshop, Duration: 2 hours, Cost: £60, Enjoyment Level: 100
		 Activity: Hiking, Duration: 5 hours, Cost: £30, Enjoyment Level: 140
		Total Enjoyment: 360
		Total Time Used: 10 hours out of 10 hours.
		Total Cost: £170 out of £200
		  
		Execution Time: 0.001419 Seconds
		
		  
		 --- Greedy Heuristic Algorithm --- 
		
		Selected Activities: 
		  Activity: Museum-Trip, Duration: 4 hours, Cost: £100, Enjoyment Level: 150
		  Activity: Hiking, Duration: 5 hours, Cost: £30, Enjoyment Level: 140
		Total Enjoyment: 290
		Total Time Used: 9 hours out of 10 hours.
		Total Cost: £130 out of £200
		
		Execution Time: 0.000012 Seconds
		

## All Dependencies:
- All imported modules:
	os (built-in)
	sys (built-in)
	time (built-in)
	from typing import List, Tuple (built-in)
	matplotlib (external module)
	numpy (external module)
	itertools (built-in)
	copy (built-in)

- To install numpy and matplotlib:
	- https://numpy.org/install/
		try: `pip install numpy` in the terminal, if not see the above link for trouble shooting.
	- https://matplotlib.org/stable/install/index.html
		try: `pip install matplotlib` in the terminal, if not see the above link for trouble shooting.

- To install or update to python 3.12.10 (3.12.12 is not available through direct install as it was a minor bugfix release):
	- https://www.python.org/downloads/release/python-31210/
	If that doesn't work try a more current version: 3.14.3 is the most recent release
		https://www.python.org/downloads/release/python-3143/

- Tested on M4 MacBook Air RAM:16GB, Storage:16GB
	- Using a conda environment with  Python 3.12.12
	- Environment details:
		active environment : uni
		    active env location : /opt/homebrew/Caskroom/miniforge/base/envs/uni
		            shell level : 2
		       user config file : /Users/theo/.condarc
		 populated config files : /opt/homebrew/Caskroom/miniforge/base/.condarc
		                          /Users/theo/.condarc
		          conda version : 26.1.0
		    conda-build version : not installed
		         python version : 3.12.12.final.0
		                 solver : classic
		       virtual packages : __archspec=1=m1
		                          __conda=26.1.0=0
		                          __osx=26.3=0
		                          __unix=0=0
		       base environment : /opt/homebrew/Caskroom/miniforge/base  (writable)
		      conda av data dir : /opt/homebrew/Caskroom/miniforge/base/etc/conda
		  conda av metadata url : None
		           channel URLs : https://conda.anaconda.org/conda-forge/osx-arm64
		                          https://conda.anaconda.org/conda-forge/noarch
		          package cache : /opt/homebrew/Caskroom/miniforge/base/pkgs
		                          /Users/theo/.conda/pkgs
		       envs directories : /opt/homebrew/Caskroom/miniforge/base/envs
		                          /Users/theo/.conda/envs
		    temporary directory : /var/folders/dg/67nsf4zn4mb4z6n46fzknw8w0000gn/T
		               platform : osx-arm64
		             user-agent : conda/26.1.0 requests/2.32.5 CPython/3.12.12 Darwin/25.3.0 OSX/26.3
		                UID:GID : 501:20
		             netrc file : None
		           offline mode : False 
	- All installed modules:
		packages in environment at /opt/homebrew/Caskroom/miniforge/base/envs/uni:
		# Name        Version          Build                 Channel
		_openmp_mutex                4.5              7_kmp_llvm                    conda-forge
		_python_abi3_support         1.0              hd8ed1ab_2                    conda-forge
		absl-py                      2.4.0            pyhd8ed1ab_0                  conda-forge
		aom                          3.9.1            h7bae524_0                    conda-forge
		appnope                      0.1.4            pyhd8ed1ab_1                  conda-forge
		archspec                     0.2.5            pyhd8ed1ab_0                  conda-forge
		astroid                      4.0.3            py312h81bd7bf_0               conda-forge
		asttokens                    3.0.1            pyhd8ed1ab_0                  conda-forge
		astunparse                   1.6.3            pyhd8ed1ab_3                  conda-forge
		backports.zstd               1.3.0            py312h44dc372_0               conda-forge
		blinker                      1.9.0            pyhff2d567_0                  conda-forge
		boltons                      25.0.0           pyhd8ed1ab_0                  conda-forge
		brotli                       1.2.0            h7d5ae5b_1                    conda-forge
		brotli-bin                   1.2.0            hc919400_1                    conda-forge
		brotli-python                1.2.0            py312h0dfefe5_1               conda-forge
		bzip2                        1.0.8            hd037594_8                    conda-forge
		c-ares                       1.34.6           hc919400_0                    conda-forge
		ca-certificates              2026.1.4         hbd8a1cb_0                    conda-forge
		cached-property              1.5.2            hd8ed1ab_1                    conda-forge
		cached_property              1.5.2            pyha770c72_1                  conda-forge
		cairo                        1.18.4           h6a3b0d2_0                    conda-forge
		certifi                      2026.1.4         pyhd8ed1ab_0                  conda-forge
		cffi                         2.0.0            py312h1b4d9a2_1               conda-forge
		charset-normalizer           3.4.4            pyhd8ed1ab_0                  conda-forge
		click                        8.3.1            pyh8f84b5b_1                  conda-forge
		colorama                     0.4.6            pyhd8ed1ab_1                  conda-forge
		comm                         0.2.3            pyhe01879c_0                  conda-forge
		conda                        26.1.0           py312h81bd7bf_0               conda-forge
		conda-libmamba-solver        25.11.0          pyhd8ed1ab_0                  conda-forge
		conda-package-handling       2.4.0            pyh7900ff3_2                  conda-forge
		conda-package-streaming      0.12.0           pyhd8ed1ab_0                  conda-forge
		contourpy                    1.3.3            py312h3093aea_4               conda-forge
		cpp-expected                 1.3.1            h4f10f1e_0                    conda-forge
		cpython                      3.12.12          py312hd8ed1ab_2               conda-forge
		cycler                       0.12.1           pyhcf101f3_2                  conda-forge
		dav1d                        1.2.1            hb547adb_0                    conda-forge
		dbus                         1.16.2           h3ff7a7c_1                    conda-forge
		debugpy                      1.8.20           py312h6510ced_0               conda-forge
		decorator                    5.2.1            pyhd8ed1ab_0                  conda-forge
		dill                         0.4.1            pyhcf101f3_0                  conda-forge
		distro                       1.9.0            pyhd8ed1ab_1                  conda-forge
		exceptiongroup               1.3.1            pyhd8ed1ab_0                  conda-forge
		executing                    2.2.1            pyhd8ed1ab_0                  conda-forge
		filelock                     3.20.3           pyhd8ed1ab_0                  conda-forge
		flask                        3.1.2            pyhd8ed1ab_0                  conda-forge
		flatbuffers                  24.12.23         h28594ff_0                    conda-forge
		fluidsynth                   2.5.2            h2ab8666_0                    conda-forge
		fmt                          12.1.0           h403dcb5_0                    conda-forge
		font-ttf-dejavu-sans-mono    2.37             hab24e00_0                    conda-forge
		font-ttf-inconsolata         3.000            h77eed37_0                    conda-forge
		font-ttf-source-code-pro     2.038            h77eed37_0                    conda-forge
		font-ttf-ubuntu              0.83             h77eed37_3                    conda-forge
		fontconfig                   2.15.0           h1383a14_1                    conda-forge
		fonts-conda-ecosystem        1                0                             conda-forge
		fonts-conda-forge            1                hc364b38_1                    conda-forge
		fonttools                    4.61.1           py312h5748b74_0               conda-forge
		freetype                     2.14.1           hce30654_0                    conda-forge
		frozendict                   2.4.7            py312h4409184_0               conda-forge
		fsspec                       2026.1.0         pyhd8ed1ab_0                  conda-forge
		gast                         0.7.0            pyhd8ed1ab_0                  conda-forge
		giflib                       5.2.2            h93a5062_0                    conda-forge
		gmp                          6.3.0            h7bae524_2                    conda-forge
		gmpy2                        2.2.1            py312hee6aa52_2               conda-forge
		google-pasta                 0.2.0            pyhd8ed1ab_2                  conda-forge
		graphite2                    1.3.14           hec049ff_2                    conda-forge
		grpcio                       1.67.1           py312he4e58e5_2               conda-forge
		h2                           4.3.0            pyhcf101f3_0                  conda-forge
		h5py                         3.15.1           nompi_py312h4eecd6b_101       conda-forge
		harfbuzz                     12.2.0           haf38c7b_0                    conda-forge
		hdf5                         1.14.6           nompi_h51e7c0a_105            conda-forge
		hpack                        4.1.0            pyhd8ed1ab_0                  conda-forge
		hyperframe                   6.1.0            pyhd8ed1ab_0                  conda-forge
		icu                          75.1             hfee45f7_0                    conda-forge
		idna                         3.11             pyhd8ed1ab_0                  conda-forge
		importlib-metadata           8.7.0            pyhe01879c_1                  conda-forge
		iniconfig                    2.3.0            pyhd8ed1ab_0                  conda-forge
		ipykernel                    7.1.0            pyh5552912_0                  conda-forge
		ipython                      9.9.0            pyh53cf698_0                  conda-forge
		ipython_pygments_lexers      1.1.1            pyhd8ed1ab_0                  conda-forge
		isort                        7.0.0            pyhd8ed1ab_0                  conda-forge
		itsdangerous                 2.2.0            pyhd8ed1ab_1                  conda-forge
		jedi                         0.19.2           pyhd8ed1ab_1                  conda-forge
		jinja2                       3.1.6            pyhcf101f3_1                  conda-forge
		joblib                       1.5.3            pyhd8ed1ab_0                  conda-forge
		jsonpatch                    1.33             pyhd8ed1ab_1                  conda-forge
		jsonpointer                  3.0.0            pyhcf101f3_3                  conda-forge
		jupyter_client               8.8.0            pyhcf101f3_0                  conda-forge
		jupyter_core                 5.9.1            pyhc90fa1f_0                  conda-forge
		keras                        3.12.0           pyh753f3f9_0                  conda-forge
		kiwisolver                   1.4.9            py312hd8c8125_2               conda-forge
		krb5                         1.21.3           h237132a_0                    conda-forge
		lame                         3.100            h1a8c8d9_1003                 conda-forge
		lcms2                        2.18             hdfa7624_0                    conda-forge
		lerc                         4.0.0            hd64df32_1                    conda-forge
		libabseil                    20240722.0       cxx17_h07bc746_4              conda-forge
		libaec                       1.1.5            h8664d51_0                    conda-forge
		libarchive                   3.8.5            gpl_h6fbacd7_100              conda-forge
		libavif16                    1.3.0            hde9513d_3                    conda-forge
		libblas                      3.11.0           7_hc63b1ca_netlib             conda-forge
		libbrotlicommon              1.2.0            hc919400_1                    conda-forge
		libbrotlidec                 1.2.0            hc919400_1                    conda-forge
		libbrotlienc                 1.2.0            hc919400_1                    conda-forge
		libcblas                     3.11.0           7_hd5b1ab5_netlib             conda-forge
		libcurl                      8.18.0           he38603e_0                    conda-forge
		libcxx                       21.1.8           hf598326_1                    conda-forge
		libdeflate                   1.25             hc11a715_0                    conda-forge
		libedit                      3.1.20250104     pl5321hafb1f1b_0              conda-forge
		libev                        4.33             h93a5062_2                    conda-forge
		libexpat                     2.7.3            haf25636_0                    conda-forge
		libffi                       3.5.2            hcf2aa1b_0                    conda-forge
		libflac                      1.5.0            h6824b09_1                    conda-forge
		libfreetype                  2.14.1           hce30654_0                    conda-forge
		libfreetype6                 2.14.1           h6da58f4_0                    conda-forge
		libgcc                       15.2.0           hcbb3090_16                   conda-forge
		libgfortran                  15.2.0           h07b0088_16                   conda-forge
		libgfortran5                 15.2.0           hdae7583_16                   conda-forge
		libglib                      2.86.3           hfe11c1f_0                    conda-forge
		libgrpc                      1.67.1           h0a426d6_2                    conda-forge
		libiconv                     1.18             h23cfdf5_2                    conda-forge
		libintl                      0.25.1           h493aca8_0                    conda-forge
		libjpeg-turbo                3.1.2            hc919400_0                    conda-forge
		liblapack                    3.11.0           7_ha522803_netlib             conda-forge
		liblzma                      5.8.2            h8088a28_0                    conda-forge
		libmad                       0.15.1b          h1a8c8d9_1001                 conda-forge
		libmamba                     2.5.0            h7950639_0                    conda-forge
		libmamba-spdlog              2.5.0            h85b9800_0                    conda-forge
		libmambapy                   2.5.0            py312h55725b6_0               conda-forge
		libml_dtypes-headers         0.5.4            h707e725_0                    conda-forge
		libnghttp2                   1.67.0           hc438710_0                    conda-forge
		libogg                       1.3.5            h48c0fde_1                    conda-forge
		libopenblas                  0.3.31           openmp_he657e61_0             conda-forge
		libopus                      1.6.1            h1a92334_0                    conda-forge
		libpng                       1.6.54           h132b30e_0                    conda-forge
		libprotobuf                  5.28.3           h3bd63a1_1                    conda-forge
		libre2-11                    2024.07.02       h07bc746_2                    conda-forge
		libsndfile                   1.2.2            hf95f74e_2                    conda-forge
		libsodium                    1.0.20           h99b78c6_0                    conda-forge
		libsolv                      0.7.35           h5f525b2_0                    conda-forge
		libsqlite                    3.51.2           h1b79a29_0                    conda-forge
		libssh2                      1.11.1           h1590b86_0                    conda-forge
		libtensorflow_cc             2.18.0           cpu_hf321e49_1                conda-forge
		libtensorflow_framework      2.18.0           cpu_h2398287_1                conda-forge
		libtiff                      4.7.1            h4030677_1                    conda-forge
		libtorch                     2.6.0            cpu_generic_h16e2b10_1        conda-forge
		libusb                       1.0.29           hbc156a2_0                    conda-forge
		libuv                        1.51.0           h6caf38d_1                    conda-forge
		libvorbis                    1.3.7            h81086ad_2                    conda-forge
		libvulkan-loader             1.4.328.1        h49c215f_0                    conda-forge
		libwebp-base                 1.6.0            h07db88b_0                    conda-forge
		libxcb                       1.17.0           hdb1d25a_0                    conda-forge
		libxml2                      2.15.1           h9329255_0                    conda-forge
		libxml2-16                   2.15.1           h0ff4647_0                    conda-forge
		libzlib                      1.3.1            h8359307_2                    conda-forge
		llvm-openmp                  21.1.8           h4a912ad_0                    conda-forge
		lz4-c                        1.10.0           h286801f_1                    conda-forge
		lzo                          2.10             h925e9cb_1002                 conda-forge
		mamba                        2.5.0            h74094d2_0                    conda-forge
		markdown                     3.10.1           pyhcf101f3_0                  conda-forge
		markdown-it-py               4.0.0            pyhd8ed1ab_0                  conda-forge
		markupsafe                   3.0.3            py312h5748b74_0               conda-forge
		matplotlib                   3.10.8           py312h1f38498_0               conda-forge
		matplotlib-base              3.10.8           py312h605b88b_0               conda-forge
		matplotlib-inline            0.2.1            pyhd8ed1ab_0                  conda-forge
		mccabe                       0.7.0            pyhd8ed1ab_1                  conda-forge
		mdurl                        0.1.2            pyhd8ed1ab_1                  conda-forge
		menuinst                     2.4.2            py312h81bd7bf_0               conda-forge
		ml_dtypes                    0.4.0            py312hcd31e36_2               conda-forge
		mpc                          1.3.1            h8f1351a_1                    conda-forge
		mpfr                         4.2.1            hb693164_3                    conda-forge
		mpg123                       1.32.9           hf642e45_0                    conda-forge
		mpmath                       1.3.0            pyhd8ed1ab_1                  conda-forge
		msgpack-python               1.1.2            py312h84eede6_1               conda-forge
		munkres                      1.1.4            pyhd8ed1ab_1                  conda-forge
		namex                        0.1.0            pyhd8ed1ab_0                  conda-forge
		ncurses                      6.5              h5e97a16_3                    conda-forge
		nest-asyncio                 1.6.0            pyhd8ed1ab_1                  conda-forge
		networkx                     3.6.1            pyhcf101f3_0                  conda-forge
		nlohmann_json                3.12.0           h784d473_1                    conda-forge
		nlohmann_json-abi            3.12.0           h0f90c79_1                    conda-forge
		nomkl                        1.0              h5ca1d4c_0                    conda-forge
		numpy                        2.4.2            py312he281c53_0               conda-forge
		openjpeg                     2.5.4            hbfb3c88_0                    conda-forge
		openssl                      3.6.1            hd24854e_1                    conda-forge
		opt_einsum                   3.4.0            pyhd8ed1ab_1                  conda-forge
		optree                       0.18.0           py312h84eede6_0               conda-forge
		opusfile                     0.12             h5643135_2                    conda-forge
		packaging                    26.0             pyhcf101f3_0                  conda-forge
		pandas                       3.0.0            py312hae6be28_0               conda-forge
		parso                        0.8.5            pyhcf101f3_0                  conda-forge
		patsy                        1.0.2            pyhcf101f3_0                  conda-forge
		pcre2                        10.47            h30297fc_0                    conda-forge
		pexpect                      4.9.0            pyhd8ed1ab_1                  conda-forge
		pillow                       12.1.0           py312h4e908a4_0               conda-forge
		pip                          26.0             pyh8b19718_0                  conda-forge
		pixman                       0.46.4           h81086ad_1                    conda-forge
		platformdirs                 4.5.1            pyhcf101f3_0                  conda-forge
		pluggy                       1.6.0            pyhf9edf01_1                  conda-forge
		portaudio                    19.7.0           h5833ebf_0                    conda-forge
		portmidi                     2.0.8            haf25636_0                    conda-forge
		prompt-toolkit               3.0.52           pyha770c72_0                  conda-forge
		protobuf                     5.28.3           py312hd8f9ff3_0               conda-forge
		psutil                       7.2.2            py312hb3ab3e3_0               conda-forge
		pthread-stubs                0.4              hd74edd7_1002                 conda-forge
		ptyprocess                   0.7.0            pyhd8ed1ab_1                  conda-forge
		pure_eval                    0.2.3            pyhd8ed1ab_1                  conda-forge
		pybind11                     3.0.1            pyh7a1b43c_0                  conda-forge
		pybind11-abi                 11               hc364b38_1                    conda-forge
		pybind11-global              3.0.1            pyhc7ab6ef_0                  conda-forge
		pycosat                      0.6.6            py312h163523d_3               conda-forge
		pycparser                    2.22             pyh29332c3_1                  conda-forge
		pygame                       2.6.1            py312hb14fe3b_0               conda-forge
		pygments                     2.19.2           pyhd8ed1ab_0                  conda-forge
		pylint                       4.0.4            pyhcf101f3_0                  conda-forge
		pyparsing                    3.3.2            pyhcf101f3_0                  conda-forge
		pysocks                      1.7.1            pyha2e5f31_6                  conda-forge
		pytest                       9.0.2            pyhcf101f3_0                  conda-forge
		python                       3.12.12          h18782d2_2_cpython            conda-forge
		python-dateutil              2.9.0.post0      pyhe01879c_2                  conda-forge
		python-flatbuffers           25.9.23          pyh1e1bc0e_0                  conda-forge
		python-gil                   3.12.12          hd8ed1ab_2                    conda-forge
		python-tzdata                2025.3           pyhd8ed1ab_0                  conda-forge
		python_abi                   3.12             8_cp312                       conda-forge
		pytorch                      2.6.0            cpu_generic_py312_h8a1ee9d_1  conda-forge
		pytz                         2025.2           pyhd8ed1ab_0                  conda-forge
		pyzmq                        27.1.0           py312hd65ceae_0               conda-forge
		qhull                        2020.2           h420ef59_5                    conda-forge
		rav1e              
		re2                          2024.07.02       h6589ca4_2                    conda-forge
		readline                     8.3              h46df422_0                    conda-forge
		reproc                       14.2.5.post0     h5505292_0                    conda-forge
		reproc-cpp                   14.2.5.post0     h286801f_0                    conda-forge
		requests                     2.32.5           pyhcf101f3_1                  conda-forge
		rich                         14.3.2           pyhcf101f3_0                  conda-forge
		ruamel.yaml                  0.18.17          py312hb3ab3e3_2               conda-forge
		ruamel.yaml.clib             0.2.15           py312hb3ab3e3_1               conda-forge
		scikit-learn                 1.8.0            np2py312he5ca3e3_1            conda-forge
		scipy                        1.17.0           py312h0f234b1_1               conda-forge
		sdl2                         2.32.56          h248ca61_0                    conda-forge
		sdl2_image                   2.8.2            h376e2e1_1                    conda-forge
		sdl2_mixer                   2.6.3            h45fadf6_2                    conda-forge
		sdl2_ttf                     2.24.0           h443c5de_0                    conda-forge
		sdl3                         3.4.0            h6fa9c73_0                    conda-forge
		seaborn                      0.13.2           hd8ed1ab_3                    conda-forge
		seaborn-base                 0.13.2           pyhd8ed1ab_3                  conda-forge
		setuptools                   80.10.2          pyh332efcf_0                  conda-forge
		simdjson                     4.2.4            ha7d2532_0                    conda-forge
		six                          1.17.0           pyhe01879c_1                  conda-forge
		sleef                        3.9.0            hb028509_0                    conda-forge
		snappy                       1.2.2            hada39a4_1                    conda-forge
		spdlog                       1.17.0           ha0f8610_1                    conda-forge
		stack_data                   0.6.3            pyhd8ed1ab_1                  conda-forge
		statsmodels                  0.14.6           py312ha11c99a_0               conda-forge
		svt-av1                      4.0.0            h0cb729a_0                    conda-forge
		sympy                        1.14.0           pyh2585a3b_105                conda-forge
		tensorboard                  2.18.0           pyhd8ed1ab_1                  conda-forge
		tensorboard-data-server      0.7.0            py312h9536bd2_4               conda-forge
		tensorflow                   2.18.0           cpu_py312hb6b62e0_1           conda-forge
		tensorflow-base              2.18.0           cpu_py312h81ab8d0_1           conda-forge
		tensorflow-estimator         2.18.0           cpu_py312h5e86b3d_1           conda-forge
		termcolor                    3.3.0            pyhd8ed1ab_0                  conda-forge
		threadpoolctl                3.6.0            pyhecae5ae_0                  conda-forge
		tk                           8.6.13           h010d191_3                    conda-forge
		tomli                        2.4.0            pyhcf101f3_0                  conda-forge
		tomlkit                      0.14.0           pyha770c72_0                  conda-forge
		tornado                      6.5.4            py312h4409184_0               conda-forge
		tqdm                         4.67.2           pyh8f84b5b_2                  conda-forge
		traitlets                    5.14.3           pyhd8ed1ab_1                  conda-forge
		truststore                   0.10.4           pyhcf101f3_0                  conda-forge
		typing-extensions            4.15.0           h396c80c_0                    conda-forge
		typing_extensions            4.15.0           pyhcf101f3_0                  conda-forge
		tzdata                       2025c            hc9c84f9_1                    conda-forge
		unicodedata2                 17.0.0           py312h4409184_1               conda-forge
		urllib3                      2.6.3            pyhd8ed1ab_0                  conda-forge
		wcwidth                      0.5.3            pyhd8ed1ab_0                  conda-forge
		werkzeug                     3.1.5            pyhcf101f3_0                  conda-forge
		wheel                        0.46.3           pyhd8ed1ab_0                  conda-forge
		wrapt                        2.1.0            py312h2bbb03f_0               conda-forge
		xorg-libxau                  1.0.12           hc919400_1                    conda-forge
		xorg-libxdmcp                1.1.5            hc919400_1                    conda-forge
		yaml-cpp                     0.8.0            ha1acc90_0                    conda-forge
		zeromq                       4.3.5            h888dc83_9                    conda-forge
		zipp                         3.23.0           pyhcf101f3_1                  conda-forge
		zlib-ng                      2.3.2            hed4e4f5_1                    conda-forge
		zstandard                    0.25.0           py312h37e1c23_1               conda-forge
		zstd                         1.5.7            hbf9d68e_6                    conda-forge

- File Structure:
	-  ECM1414-Group-Project
		- Coursework Description Final.pdf
		- README.md
		- Code
			- event_planner.py
			- performance_analysis.py
			- README.md
			- algorithms
				- brute_force.py
				- dynamic.py
				- enhanced_brute_force.py
				- greedy_heuristic.py
				- dynamic_enhanced.py
			- Classes
				- Activity.py
			- utils
				- read_input_file.py
		- Documents
			- Report.pdf 
			- Group_Contribution_Statement.pdf 
			- to_do.md
			- Documentation for Brute Force.docx
			- Powerpoint.pptx
			- Documentation for Brute Force.txt
			- pseudocode for brute_force algorithm.txt
			- pseudocode_for_dp.txt
			- Documentation for dynamic algorithm.docx
			- Testing
				- Small_testing_bf/e.txt
				- Medium_testing_bf/e.txt
				- Large_testing_bf/e.txt
		- Input Files
			- input_small.txt
			- input_medium.txt
			- input_large.txt
			- input_5.txt
			- input_10.txt 
			- input_15.txt 
			- input_20.txt 
			- input_25.txt
			- input_26.txt  
			- input_27.txt 
			- input_28.txt
			- input_29.txt
			- input_100.txt 
			- input_200.txt 
			- input_500.txt
			- input_1000.txt 
		- Presentation:
			- Powerpoint.pptx
			- README.md