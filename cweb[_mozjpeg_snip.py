if not os.path.exists(_final):
    os.makedirs(_final)
		for _k in m:
			__a=_k.split('.')
			__str='cwebp.exe -q 90 '+_init+str(_k)+' -o '+_final+str(__a[0])+'.webp'
			print (__str)
			os.system(__str)
else :
	print(' Not executing as final '+_final+' already directory already exists ')
