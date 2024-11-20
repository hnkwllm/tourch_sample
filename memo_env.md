master pc
```
export MASTER_ADDR=192.168.1.100  # マスターPCのIPアドレス
export MASTER_PORT=29500          # 任意の空いているポート番号
export WORLD_SIZE=2               # マシンの総数
export RANK=0                     # マスターのランク
python sub.py
```

worker pc
```
export MASTER_ADDR=192.168.1.100  # マスターPCのIPアドレス
export MASTER_PORT=29500          # マスターPCのポート
export WORLD_SIZE=2               # マシンの総数
export RANK=1                     # ワーカーのランク
python sub.py
```