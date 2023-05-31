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
