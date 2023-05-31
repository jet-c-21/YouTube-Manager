# YouTube-Manager
YouTube Manger App

# Environment

### Create conda env
```shell
conda create -y --name=yt python=3.8 
```

### Remove conda env
```shell
conda env remove -y --name yt 
```

### add jupyter kernel
```shell
conda activate yt
pip install ipykernel
python -m ipykernel install --user --name yt --display-name "YouTube Manager"
```

### remove jupyter kernel
```shell
jupyter kernelspec uninstall -y yt 
```

### Fix CV2 import problem
```shell
rm /home/puff/anaconda3/envs/yt/lib/libstdc++.so.6
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/puff/anaconda3/envs/yt/lib/libstdc++.so.6
```
