from PyInstaller.utils.hooks import collect_all  

# 封装用的
def hook(hook_api):  
    packages = ['CDNDrive']  
    for package in packages:  
        datas, binaries, hiddenimports = collect_all(package)  
        # hook_api.add_datas(datas)  # 注释掉是因为通常用不到
        # hook_api.add_binaries(binaries)
        hook_api.add_imports(*hiddenimports)