import itertools
import argparse
import sys
import os 
from math import ceil 
from signature import *


def hex_group_formatter(iterable):
    chunks = [iter(iterable)] * 4
    return '   '.join(
        ' '.join(format(x, '0>2x') for x in chunk)
        for chunk in itertools.zip_longest(*chunks, fillvalue=0))

def hex_viewer(filename, chunk_size=16):
    template = ' {:<53}'
    with open(filename, 'rb') as stream:
        for chunk_count in itertools.count(0):
            chunk = stream.read(chunk_size)
            if not chunk:
                return
            yield template.format(
                hex_group_formatter(chunk)
				)

def file_out(string, header_signature):
	global out_file_cnt, unit
	out_file_cnt += 1
	out_file_name = 'file_out_' + str(out_file_cnt) + '.' + file_extension[header_signature]
	f = open(out_file_name,'wb+')   
	f.write(bytes.fromhex(string))
	f.close()
	out_file_size = os.path.getsize(out_file_name)
	print('[*] Out_file :', out_file_name,'  \t','Size :', size_return(out_file_size))

	
def size_return(bytes):
	size_result = str(bytes) + 'Byte'
	if (bytes > 1024):
		size_result = str(int(ceil(bytes/1024))) + 'KB'
	elif (bytes > 1024*1024):	
		size_result = str(int(ceil(bytes/(1024*1024)))) + 'MB'
	elif (bytes > 1024*1024*1024):	
		size_result = str(ceil(bytes/(1024*1024*1024))) + 'GB'
	elif (bytes > 1024*1024*1024*1024):	
		size_result = str(int(ceil(bytes/(1024*1024*1024*1024)))) + 'TB'
	return size_result
	
def usage():
	print("syntax: ./hiddenfile_find <file>")

	
if __name__ == '__main__':
	if(len(sys.argv) != 2):
		usage()
		exit()
	parser = argparse.ArgumentParser(description='Hexadeciaml viewer.')
	parser.add_argument('file', nargs='?', default=sys.argv[1], help='the file to process')
	args = parser.parse_args()
	
	file_size = os.path.getsize(sys.argv[1])

	print('\n[*] Input_file :', sys.argv[1],'\t','Size :', size_return(file_size),'\n')
	
	cnt = -1
	out_file_cnt = 0
	out_file_flag = 0
	string = ''

	for line in hex_viewer(args.file):
		string += line.replace("   ", " ")

	#print(hex(len(string)))
	#print(string[6373626-30:6373626])

	while (cnt < len(file_signature)-1):
		cnt += 1
		if (string.find(file_signature[cnt]) != -1):      
			file_index_start = string.index(file_signature[cnt])
			header_signature = string[file_index_start:file_index_start+len(file_signature[cnt])]
			footer_signature = file_header_footer[header_signature]
			out_file_flag = 1

			if(string[file_index_start:].find(footer_signature)!= -1):
				file_index_end = string[file_index_start:].index(footer_signature)+ file_index_start + len(footer_signature)
			else:
				out_file_flag = 0
				continue 
		
		#print(file_index_start)
		#print(file_index_end)
		#print(string[167280-20:167280])
		

		if (out_file_flag == 1):
			out_file_flag = 0

			new_file = string[file_index_start:file_index_end]
			#print(new_file)

			# 파일 추출
			file_out(new_file, header_signature)
			
			# 추출 파일 삭제
			next_index = file_index_end + 1
			string = string[:file_index_start] + string[next_index:]
			
			#print(string)
			cnt = -1
		
	#print(string)
	