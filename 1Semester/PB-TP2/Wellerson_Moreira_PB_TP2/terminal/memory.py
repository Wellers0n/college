import psutil

mem = psutil.virtual_memory()
capacidade = round(mem.total/(1024*1024*1024), 2)
print("Capacidade total de MP:", capacidade, "GB")